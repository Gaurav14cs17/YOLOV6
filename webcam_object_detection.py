import cv2
import  time
from YOLOv6 import YOLOv6

# Initialize the webcam
video_path = 0
cap = cv2.VideoCapture(video_path)

width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)  # float
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)  # float
fps = cap.get(cv2.CAP_PROP_FPS)
save_path = "video.mp4"
vid_writer = cv2.VideoWriter(save_path, cv2.VideoWriter_fourcc(*"mp4v"), fps, (int(width), int(height)))

FPS = 0

# Initialize YOLOv6 object detector
model_path = "models/yolov6s.onnx"
yolov6_detector = YOLOv6(model_path, conf_thres=0.5, iou_thres=0.5)

cv2.namedWindow("Detected Objects", cv2.WINDOW_NORMAL)
while cap.isOpened():

    # Read frame from the video
    ret, frame = cap.read()
    t0 = time.time()
    if not ret:
        break

    # Update object localizer
    boxes, scores, class_ids = yolov6_detector(frame)

    combined_img = yolov6_detector.draw_detections(frame)

    FPS = (FPS + (1. / (time.time() - t0))) / 2
    result_frame = cv2.putText(combined_img, "FPS=%.2f" % (FPS), (0, 70), cv2.FONT_HERSHEY_SIMPLEX, 1,(0, 255, 0), 2)
    combined_img = cv2.putText(combined_img, "YoloV6", (0, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 25, 9), 2)
    vid_writer.write(combined_img)
    # else:
    cv2.namedWindow("yolox", cv2.WINDOW_NORMAL)
    cv2.imshow("yolox", result_frame)
    ch = cv2.waitKey(1)
    if ch == 27 or ch == ord("q") or ch == ord("Q"):
        break

    cv2.imshow("Detected Objects", combined_img)

    # Press key q to stop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
