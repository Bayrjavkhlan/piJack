# main.py
import cv2
from face_recognition import FaceRecognition

def main():
    cap = cv2.VideoCapture(0)  # use webcam (0 = default)
    face_recog = FaceRecognition()

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.flip(frame, 1)

        face_detected, annotated_frame = face_recog.detect_face(frame)

        if face_detected:
            cv2.putText(annotated_frame, "Face Detected", (50, 50),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        cv2.imshow("Face Recognition", annotated_frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):  # press q to quit
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
