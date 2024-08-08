import sys
import speech_recognition as sr
from pydub import AudioSegment

def audio_to_text(audio_file):
    recognizer = sr.Recognizer()

    audio_format = audio_file.split('.')[-1]
    if audio_format != 'wav':
        sound = AudioSegment.from_file(audio_file)
        audio_file = audio_file.replace(audio_format, 'wav')
        sound.export(audio_file, format='wav')

    with sr.AudioFile(audio_file) as source:
        audio_data = recognizer.record(source)

    try:
        text = recognizer.recognize_google(audio_data)
        return text
    except sr.UnknownValueError:
        return "Google Speech Recognition could not understand the audio"
    except sr.RequestError as e:
        return f"Could not request results from Google Speech Recognition service; {e}"

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python audio_to_text.py <path_to_audio_file>")
        sys.exit(1)

    audio_file_path = sys.argv[1]
    print(audio_to_text(audio_file_path))
