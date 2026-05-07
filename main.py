from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
import yt_dlp
import threading
import os

class DownloaderApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=20, spacing=20)
        
        self.layout.add_widget(Label(text="YT Downloader v2.0", font_size='24sp', size_hint_y=None, height=100))
        
        self.url_input = TextInput(hint_text="Paste YouTube URL here", multiline=False, size_hint_y=None, height=100)
        self.layout.add_widget(self.url_input)
        
        self.status_label = Label(text="Ready")
        self.layout.add_widget(self.status_label)
        
        self.down_btn = Button(text="Download 720p", background_color=(0, 1, 0, 1), size_hint_y=None, height=120)
        self.down_btn.bind(on_release=self.start_download)
        self.layout.add_widget(self.down_btn)
        
        return self.layout

    def start_download(self, instance):
        url = self.url_input.text.strip()
        if not url:
            self.status_label.text = "Error: Paste a URL first!"
            return
        
        self.status_label.text = "Downloading..."
        threading.Thread(target=self.run_dlp, args=(url,), daemon=True).start()

    def run_dlp(self, url):
        try:
            # On Android, we save to the Downloads folder
            save_path = '/sdcard/Download/%(title)s.%(ext)s'
            ydl_opts = {
                'format': 'best[ext=mp4]/best',
                'outtmpl': save_path,
            }
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            self.status_label.text = "SUCCESS! Saved to Downloads"
        except Exception as e:
            self.status_label.text = f"Error: {str(e)}"

if __name__ == '__main__':
    DownloaderApp().run()
