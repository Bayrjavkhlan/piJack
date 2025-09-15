import speech_recognition as sr
from google_ai_api import ask_google_ai  # import your Google API wrapper

class VoiceAssistant:
    def __init__(self, language="mn-MN"):
        self.recognizer = sr.Recognizer()
        self.language = language
        self.commands_map = {}  # keyword -> function
        self.ai_keyword = "хосоо"  # special trigger word

    def add_command(self, keyword, function):
        self.commands_map[keyword.lower()] = function

    def recognize_speech(self):
        with sr.Microphone() as source:  # <-- initialize here
            print("Яриад үзээрэй...")
            self.recognizer.adjust_for_ambient_noise(source)
            audio = self.recognizer.listen(source)
            print("Дуу хоолой бичигдлээ.")

        try:
            text = self.recognizer.recognize_google(audio, language=self.language)
            return text.lower()
        except sr.UnknownValueError:
            return ""
        except sr.RequestError as e:
            print("Error with Google Speech API:", e)
            return ""

    def check_commands(self, text):
        # Check normal commands
        for keyword, func in self.commands_map.items():
            if keyword in text:
                func()

        # Check AI keyword
        if self.ai_keyword in text:
            prompt = text.replace(self.ai_keyword, "").strip()
            if prompt:
                print("Sending question to Gemini AI...")
                answer = ask_google_ai(prompt)
                print("Gemini says:", answer)
            else:
                print("Хоосон асуулт байна.")
