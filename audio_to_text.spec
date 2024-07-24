# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['audio_to_text.py'],
    pathex=[r"C:\Users\iguez\OneDrive\Documents\maya\scripts\myScripts\audio_to_text"],
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
