# face_recognition.py
import cv2
import mediapipe as mp

class FaceRecognition:
    def __init__(self):
        self.mp_face_detection = mp.solutions.face_detection
        self.mp_drawing = mp.solutions.drawing_utils
        self.face_detection = self.mp_face_detection.FaceDetection(
            model_selection=0,  # 0 = short-range (2m), 1 = long-range (5m)
            min_detection_confidence=0.6
        )

    def detect_face(self, frame):
        """Detects faces in the given frame and returns True if found."""
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.face_detection.process(frame_rgb)

        if results.detections:
            for detection in results.detections:
                self.mp_drawing.draw_detection(frame, detection)  # draw box
            return True, frame
        return False, frame
