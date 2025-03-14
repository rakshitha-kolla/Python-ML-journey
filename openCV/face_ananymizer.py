import cv2
import mediapipe as mp
import argparse
import numpy as np


def process_img(img, face_detection):
    """Detects faces and applies a blur effect to anonymize them."""
    if img is None:
        print("Error: Received an empty image!")
        return None

    H, W, _ = img.shape
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    out = face_detection.process(img_rgb)

    if out.detections:
        for detection in out.detections:
            location_data = detection.location_data
            bbox = location_data.relative_bounding_box

            # Convert relative coordinates to absolute
            x1, y1, w, h = int(bbox.xmin * W), int(bbox.ymin * H), int(bbox.width * W), int(bbox.height * H)

            # Ensure bounding box is within image limits
            x1, y1 = max(0, x1), max(0, y1)
            w, h = min(W - x1, w), min(H - y1, h)

            # Apply blur if the face region is valid
            if w > 0 and h > 0:
                img[y1:y1 + h, x1:x1 + w] = cv2.GaussianBlur(img[y1:y1 + h, x1:x1 + w], (51, 51), 0)

    return img


# Argument parsing for mode selection
args = argparse.ArgumentParser()
args.add_argument("--mode", default="webcam", help="Choose between 'webcam', 'image', or 'video'")
args.add_argument("--filepath", default=None, help="Path to image or video file")
args = args.parse_args()

# Initialize MediaPipe Face Detection
mp_face_detection = mp.solutions.face_detection
with mp_face_detection.FaceDetection(model_selection=0, min_detection_confidence=0.5) as face_detection:
    if args.mode == "image":
        img = cv2.imread(args.filepath)
        if img is None:
            print(f"Error: Unable to load image from {args.filepath}")
            exit()

        img = process_img(img, face_detection)
        cv2.imwrite("face_anonymized.jpg", img)
        cv2.imshow("Face Anonymized", img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    elif args.mode == "video":
        cap = cv2.VideoCapture(args.filepath)
        if not cap.isOpened():
            print(f"Error: Unable to open video file {args.filepath}")
            exit()

        ret, frame = cap.read()
        output_video = cv2.VideoWriter("output_video.mp4", cv2.VideoWriter_fourcc(*"MP4V"), 25,
                                       (frame.shape[1], frame.shape[0]))

        while ret:
            frame = process_img(frame, face_detection)
            output_video.write(frame)
            ret, frame = cap.read()

        cap.release()
        output_video.release()

    elif args.mode == "webcam":
        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            print("Error: Unable to access the webcam")
            exit()

        while True:
            ret, frame = cap.read()
            if not ret or frame is None:
                print("Error: Unable to read from webcam!")
                break

            frame = process_img(frame, face_detection)
            cv2.imshow("Face Anonymizer", frame)

            if cv2.waitKey(25) & 0xFF == ord("z"):
                break

        cap.release()
        cv2.destroyAllWindows()
