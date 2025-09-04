import torch

model = torch.hub.load('ultralytics/yolov5', 'yolov5s')

def detect_person(frame):
    results = model(frame)
    return results.xyxy[0]  # bounding boxes