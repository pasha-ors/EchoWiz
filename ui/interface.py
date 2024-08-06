import tkinter as tk
import threading
import sys

sys.path.append("../logic")
from logic.echowiz import recognize_speech, speak_text


class SpeechRecognitionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Speech Recognition App")
        self.root.geometry("400x500")
        self.root.resizable(False, False)

        self.recognition_active = False
        self.create_widgets()

    def create_widgets(self):
        self.start_button = tk.Button(self.root, text="Start Recognition", command=self.start_recognition_thread)
        self.start_button.pack(pady=20)

        self.stop_button = tk.Button(self.root, text="Stop Recognition", command=self.stop_recognition)
        self.stop_button.pack(pady=10)

        self.info_label = tk.Label(self.root, text="Press the button and say something", wraplength=500)
        self.info_label.pack(pady=20)

        instruction_label = tk.Label(self.root, text="Instructions:", fg="blue", font=("Arial", 12, "bold"))
        instruction_label.pack(pady=10)

        info_text = (
            "1. Click the 'Start Recognition' button.\n"
            "2. Speak clearly into your microphone.\n"
            "3. Your speech will be recognized and displayed.\n"
            "4. Click 'Stop Recognition' to stop the recognition.\n"
        )
        info_text_label = tk.Label(self.root, text=info_text, fg="green", font=("Arial", 10))
        info_text_label.pack(pady=10)

    def start_recognition_thread(self):
        self.recognition_active = True
        self.recognition_thread = threading.Thread(target=self.recognition_loop)
        self.recognition_thread.start()

    def recognition_loop(self):
        while self.recognition_active:
            self.update_info_label("Listening...")
            text = recognize_speech()
            if not self.recognition_active:
                break
            if text:
                self.update_info_label(f"You said: {text}")
                speak_text(f"You said: {text}")
            else:
                self.update_info_label("Could not understand the audio, please try again.")

    def stop_recognition(self):
        self.recognition_active = False
        self.update_info_label("Recognition stopped.")

    def update_info_label(self, text):
        self.info_label.config(text=text)
