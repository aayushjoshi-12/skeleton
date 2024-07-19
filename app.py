from ultralytics import YOLO
import cv2 as cv
from util import draw_skeleton

model = YOLO("yolov8n-pose.pt")

cap = cv.VideoCapture(0)
while True:
    ret, frame = cap.read()
    results = model(frame)
    frame = draw_skeleton(frame, results[0].keypoints) 
    # TODO add functionality to not shut when there is no person
    cv.imshow("frame", frame)
    if cv.waitKey(1) == ord("q"):
        break

cap.release()
cv.destroyAllWindows()
