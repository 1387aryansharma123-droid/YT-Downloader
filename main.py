name: Build Android APK
on: 
  push:
    branches: [ main ]
  workflow_dispatch:

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Build with Buildozer
        uses: ArtemSBulgakov/buildozer-action@v1
        with:
          buildozer_version: stable
          command: buildozer android debug
          repository_display_name: MedicalApp

      - name: Upload APK
        uses: actions/upload-artifact@v4
        with:
          name: MedicalApp-APK
          path: bin/*.apk
