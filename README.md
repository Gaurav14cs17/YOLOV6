# ONNX YOLOv6 Object Detection
 ![!YOLOv6 Model](https://github.com/Gaurav14cs17/YOLOV6/blob/main/doc/img/Slide1.jpg)
 
 16 FPS on cpu INTEL i7

![!YOLOv6 detection video](https://github.com/Gaurav14cs17/YOLOV6/blob/main/doc/img/yolov6s_video.gif)

# Important
- About the YOLOv6 name: https://github.com/meituan/YOLOv6/blob/main/docs/About_naming_yolov6.md

# Requirements

 * Check the **requirements.txt** file. 
 * For ONNX, if you have a NVIDIA GPU, then install the **onnxruntime-gpu**, otherwise use the **onnxruntime** library.
 * Additionally, **pafy** and **youtube-dl** are required for youtube video inference.
 

### ONNX Runtime
For Nvidia GPU computers:
`pip install onnxruntime-gpu`

Otherwise:
`pip install onnxruntime`


# Pytorch model
The original Pytorch model can be found in this repository: [YOLOv6 Repository](https://github.com/meituan/YOLOv6)
 
# Examples

 * **Image inference**:
 ```
 python image_object_detection.py
 ```
 
 * **Webcam inference**:
 ```
 python webcam_object_detection.py
 ```



# References:
* YOLOv6 model: https://github.com/meituan/YOLOv6
* ONNX Model : https://github.com/ibaiGorordo/ONNX-YOLOv6-Object-Detection
