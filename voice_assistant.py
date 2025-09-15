import speech_recognition as sr  

class VoiceAssistant:
    def __init__(self, language="mn-MN"):
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        self.language = language

    def recognize_speech(self):
        with self.microphone as source:
            print("Яриад үзээрэй...")  # "Speak something..."
            self.recognizer.adjust_for_ambient_noise(source)
            audio = self.recognizer.listen(source)
            print("Дуу хоолой бичигдлээ.")  # "Audio captured."

        try:
            text = self.recognizer.recognize_google(audio, language=self.language)
            return text
        except sr.UnknownValueError:
            return "Уучлаарай, ойлгож чадсангүй."  # Could not understand
        except sr.RequestError:
            return "Интернет холболтоо шалгана уу."  # Check internet
