import os
import shutil
import maya.cmds as cmds
import sys

def install_scripts_and_shelf(script_dir):
    print("Script Directory:", script_dir)

    # Define the source paths relative to the script location
    source_path_audio_to_text = os.path.join(script_dir, "audio_to_text")

    # Define the destination paths
    destination_path = cmds.internalVar(userScriptDir=True)
    icon_path = cmds.internalVar(userBitmapsDir=True)

    # Print paths for debugging
    print("Source Path Audio to Text:", source_path_audio_to_text)
    print("Destination Path:", destination_path)
    print("Icon Path:", icon_path)

    # Copy the audio_to_text folder to the Maya script folder
    try:
        if os.path.exists(source_path_audio_to_text):
            dest_audio_to_text = os.path.join(destination_path, "audio_to_text")
            if os.path.exists(dest_audio_to_text):
                shutil.rmtree(dest_audio_to_text)
            shutil.copytree(source_path_audio_to_text, dest_audio_to_text)
    except Exception as e:
        print(f"Error copying audio_to_text folder: {e}")

    # Construct the relative path to the imgs folder
    imgs_path = os.path.join(script_dir, "imgs")

    # Copy images to the Maya icons folder
    try:
        for file_name in os.listdir(imgs_path):
            if file_name.endswith(".png"):
                shutil.copy(os.path.join(imgs_path, file_name), icon_path)
    except Exception as e:
        print(f"Error copying image files: {e}")

    # Get the current shelf name
    current_shelf = cmds.tabLayout("ShelfLayout", q=True, selectTab=True)

    try:
        cmds.shelfButton(parent=current_shelf, label="Audio to Text", image="your_icon_image.png",
                         command='import audio_to_text.main; audio_to_text.main.run()', sourceType="python")
    except Exception as e:
        print(f"Error creating 'Audio to Text' shelf button: {e}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        script_dir = sys.argv[1]
    else:
        script_dir = os.path.dirname(__file__)
    
    print("Executing from directory:", script_dir)
    install_scripts_and_shelf(script_dir)
