from djitellopy import Tello
import cv2
import math 
from ultralytics import YOLO

# Verbindung zur Drohne herstellen
tello = Tello()
tello.connect()
tello.streamon()  # Starte das Video-Streaming der Drohne

# Modell initialisieren
model = YOLO("yolo-Weights/yolov8n.pt")

# Klassenbezeichnungen
classNames = ["person", "bicycle", "car", "motorbike", "aeroplane", "bus", "train", "truck", "boat",
              "traffic light", "fire hydrant", "stop sign", "parking meter", "bench", "bird", "cat",
              "dog", "horse", "sheep", "cow", "elephant", "bear", "zebra", "giraffe", "backpack", "umbrella",
              "handbag", "tie", "suitcase", "frisbee", "skis", "snowboard", "sports ball", "kite", "baseball bat",
              "baseball glove", "skateboard", "surfboard", "tennis racket", "bottle", "wine glass", "cup",
              "fork", "knife", "spoon", "bowl", "banana", "apple", "sandwich", "orange", "broccoli",
              "carrot", "hot dog", "pizza", "donut", "cake", "chair", "sofa", "pottedplant", "bed",
              "diningtable", "toilet", "tvmonitor", "laptop", "mouse", "remote", "keyboard", "cell phone",
              "microwave", "oven", "toaster", "sink", "refrigerator", "book", "clock", "vase", "scissors",
              "teddy bear", "hair drier", "toothbrush"
              ]

# Hauptloop
while True:
    frame = tello.get_frame_read().frame
    results = model(frame, stream=True)

    # Koordinaten
    for r in results:
        boxes = r.boxes

        for box in boxes:
            # Bounding Box
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2) # Zu int-Werten konvertieren

            # Bounding Box auf das Bild zeichnen
            cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 255), 3)

            # Vertrauen
            confidence = math.ceil((box.conf[0]*100))/100
            print("Vertrauen --->",confidence)

            # Klassenname
            cls = int(box.cls[0])
            print("Klassenname -->", classNames[cls])

            # Objektdetails
            org = [x1, y1]
            font = cv2.FONT_HERSHEY_SIMPLEX
            fontScale = 1
            color = (255, 0, 0)
            thickness = 2

            cv2.putText(frame, classNames[cls], org, font, fontScale, color, thickness)

    cv2.imshow('Drohnenkamera', frame)
    if cv2.waitKey(1) == ord('q'):
        break

# Verbindung zur Drohne trennen
tello.streamoff()
tello.land()
tello.end()

cv2.destroyAllWindows()
