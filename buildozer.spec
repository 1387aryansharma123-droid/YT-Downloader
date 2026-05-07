[app]
title = YT Downloader
package.name = ytdlapp
package.domain = org.arpit

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,ttf
version = 0.1

# Updated requirements for your specific project
requirements = python3, kivy==2.3.0, yt-dlp, certifi, requests

orientation = portrait

# Permissions needed for internet and saving videos
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE

# Technical Build Settings
android.archs = arm64-v8a, armeabi-v7a
android.ndk = 26b
android.sdk = 34
android.api = 34
android.minapi = 21

[buildozer]
log_level = 2