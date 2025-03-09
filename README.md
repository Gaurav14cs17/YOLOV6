---

# ONNX YOLOv6 Object Detection

![YOLOv6 Model](https://github.com/Gaurav14cs17/YOLOV6/blob/main/doc/img/Slide1.jpg)

**16 FPS on CPU (Intel i7)**

![YOLOv6 Detection Video](https://github.com/Gaurav14cs17/YOLOV6/blob/main/doc/img/yolov6s_video.gif)

---

## About YOLOv6
YOLOv6 is a state-of-the-art object detection model designed for real-time applications. This repository provides an **ONNX implementation** of YOLOv6, enabling efficient inference on both CPU and GPU devices.

For more details about the YOLOv6 name and its origins, please refer to the official documentation:  
[About the YOLOv6 Name](https://github.com/meituan/YOLOv6/blob/main/docs/About_naming_yolov6.md)

---

## Requirements
To run the ONNX YOLOv6 model, ensure you have the following dependencies installed:

### Python Libraries
- Install the required libraries from the `requirements.txt` file:
  ```bash
  pip install -r requirements.txt
  ```

### ONNX Runtime
- **For NVIDIA GPU users**: Install the GPU version of ONNX Runtime for accelerated inference:
  ```bash
  pip install onnxruntime-gpu
  ```
- **For CPU users**: Install the CPU version of ONNX Runtime:
  ```bash
  pip install onnxruntime
  ```

### Additional Libraries
- For YouTube video inference, install `pafy` and `youtube-dl`:
  ```bash
  pip install pafy youtube-dl
  ```

---

## PyTorch Model
The original PyTorch implementation of YOLOv6 can be found in the official repository:  
[YOLOv6 Repository](https://github.com/meituan/YOLOv6)

---

## Usage

### Image Inference
To perform object detection on an image, run:
```bash
python image_object_detection.py
```

### Webcam Inference
To perform real-time object detection using a webcam, run:
```bash
python webcam_object_detection.py
```

---

## Performance
- **16 FPS on CPU (Intel i7)**: The ONNX model achieves real-time performance on a standard CPU.
- **GPU Acceleration**: For even faster inference, use the `onnxruntime-gpu` library with an NVIDIA GPU.

---

## Examples
- **Image Inference**: Detect objects in static images.
- **Webcam Inference**: Perform real-time object detection using a webcam.
- **YouTube Video Inference**: Detect objects in YouTube videos (requires `pafy` and `youtube-dl`).

---

## References
- **YOLOv6 Model**: [YOLOv6 GitHub Repository](https://github.com/meituan/YOLOv6)
- **ONNX Model**: [ONNX YOLOv6 Object Detection](https://github.com/ibaiGorordo/ONNX-YOLOv6-Object-Detection)

---

## License
This project is open-source and available under the MIT License. For more details, see the [LICENSE](LICENSE) file.

---

## Contributing
Contributions are welcome! If you find any issues or have suggestions for improvement, please open an issue or submit a pull request.

---
