from ultralytics import YOLO

# Load the model and run the tracker with a custom configuration file
model = YOLO('yolov8n.pt')
results = model.track(source="traffic.mp4, tracker='custom_tracker.yaml')