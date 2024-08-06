import speech_recognition as sr
import pyttsx3

def recognize_speech():
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    with microphone as source:
        print("Say something...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        speech_text = recognizer.recognize_google(audio, language="en-US")
        print(f"You said: {speech_text}")
        return speech_text
    except sr.UnknownValueError:
        print("Could not understand the audio")
        return None
    except sr.RequestError as e:
        print(f"Error with the recognition service; {e}")
        return None

def speak_text(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)  # Speech rate
    engine.setProperty('volume', 1)  # Volume (0.0 to 1.0)
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    text = ""
    while True:
        text = recognize_speech()
        if str(text).lower() == "goodbye":
            if text:
                speak_text("It was nice talking to you")
                break
        else:
            if text:
                speak_text(f"You said: {text}")
