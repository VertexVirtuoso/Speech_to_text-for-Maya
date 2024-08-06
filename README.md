# audio_to_text-for-Maya
 A speech recognition tool for Maya, it writes on the command line what it's said in the scene's audio


To compile:

1. Get binaries for FFmpeg

    Windows: Download from FFmpeg for Windows
    macOS: Download from FFmpeg for macOS
    Linux: Install using your package manager (sudo apt-get install ffmpeg for Debian-based systems)

	After downloading, extract the binaries and place them in a directory (ffmpeg in this example).

2. Install Python Libraries Locally

	pip install SpeechRecognition pydub


3. Collect the Python Libraries
	Find the installed packages in your Python site-packages directory. This is typically located in:

    	Windows: C:\Users\<YourUsername>\AppData\Local\Programs\Python\PythonXX\Lib\site-packages
    	macOS/Linux: /usr/local/lib/pythonX.X/site-packages or /usr/lib/pythonX.X/site-packages

	You need to copy the SpeechRecognition, pydub, and their dependencies to your project directory.

4. Create the Directory Structure

```c
	/my_project
    |-- audio_to_text.py
    |-- ffmpeg/
        |-- ffmpeg.exe
        |-- ffplay.exe
        |-- ffprobe.exe
    |-- other_dependencies/
        |-- site-packages/
            |-- speech_recognition/
            |-- pydub/
            |-- ...
```

5. Create and Update the PyInstaller Spec File

	Create:

		pyinstaller --onefile --name audio_to_text audio_to_text.py

	Update spec file to:


```c
# -*- mode: python ; coding: utf-8 -*-


block_cipher = None

a = Analysis(
    ['audio_to_text.py'],
    pathex=['/path/to/my_project'],
    binaries=[('ffmpeg/ffmpeg.exe', 'ffmpeg'), ('ffmpeg/ffplay.exe', 'ffmpeg'), ('ffmpeg/ffprobe.exe', 'ffmpeg')],
    datas=[('other_dependencies/site-packages', 'site-packages')],
    hiddenimports=['pydub', 'speech_recognition'],
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='audio_to_text',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='audio_to_text',
)
```


6. Build the Executable with PyInstaller
	
	Run PyInstaller with the spec file to build the executable:

		pyinstaller audio_to_text.spec


7. The main.py file is the one needed to run the compiled executable in maya, assuming all the dependencies are in the maya scripts folder