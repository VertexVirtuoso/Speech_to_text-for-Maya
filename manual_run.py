import subprocess
import maya.cmds as cmds
import os

def get_maya_audio():
    # Get the audio node in the Maya scene
    audio_nodes = cmds.ls(type='audio')
    if not audio_nodes:
        print("No audio nodes found in the scene.")
        return None
    audio_path = cmds.getAttr(f"{audio_nodes[0]}.filename")
    print(f"Retrieved Audio Path: {audio_path}")  # Print the path for debugging
    return audio_path

def get_script_directory():
    # Get the script directory using Maya's internalVar command
    script_dir = cmds.internalVar(userScriptDir=True)
    return script_dir

def call_audio_to_text_executable(audio_file_path):
    script_dir = get_script_directory()

    # Define the path to the executable and ffmpeg directory dynamically
    executable_path = os.path.join(script_dir, 'audio_to_text', 'audio_to_text.exe')
    ffmpeg_path = os.path.join(script_dir, 'audio_to_text', '_internal', 'ffmpeg')

    # Ensure ffmpeg binaries are accessible (optional if ffmpeg is bundled)
    os.environ["PATH"] += os.pathsep + ffmpeg_path

    # Call the executable with the audio file path as an argument
    try:
        result = subprocess.run([executable_path, audio_file_path], capture_output=True, text=True, check=True)
        print("Standard Output:\n", result.stdout)
        if result.stderr:
            print("Standard Error:\n", result.stderr)
    except subprocess.CalledProcessError as e:
        print(f"Subprocess failed with return code {e.returncode}")
        print(f"Standard Output:\n{e.stdout}")
        print(f"Standard Error:\n{e.stderr}")

# Example usage
audio_file_path = get_maya_audio()
if audio_file_path:
    call_audio_to_text_executable(audio_file_path)
