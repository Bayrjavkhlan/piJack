import cv2
import threading
import sys
from face_recognition import FaceRecognition
from voice_assistant import VoiceAssistant
import commands  # your commands.py

stop_event = threading.Event()

def listen_voice(assistant):
    while not stop_event.is_set():
        text = assistant.recognize_speech()
        if text:
            print("Та хэлсэн нь:", text)
            assistant.check_commands(text)
        
        if "гарах" in text or "quit" in text or "exit" in text:
            stop_event.set()
            break

def main():
    cap = cv2.VideoCapture(0)
    face_recog = FaceRecognition()
    assistant = VoiceAssistant(language="mn-MN")

    # register your keywords
    assistant.add_command("гэрэл ас", commands.turn_on_light)
    assistant.add_command("гэрэл унт", commands.turn_off_light)

    # start voice thread
    voice_thread = threading.Thread(target=listen_voice, args=(assistant,), daemon=True)
    voice_thread.start()

    while not stop_event.is_set():
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.flip(frame, 1)
        face_detected, annotated_frame = face_recog.detect_face(frame)

        if face_detected:
            cv2.putText(annotated_frame, "Face Detected", (50, 50),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        cv2.imshow("Face Recognition", annotated_frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            stop_event.set()
            break

    cap.release()
    cv2.destroyAllWindows()
    sys.exit(0)

if __name__ == "__main__":
    main()
