import streamlit as st

# Page title and header
st.title("Real-time Plastic Waste Segmentation on Edge Devices")
st.subheader("Optimize AI Models for Mobile and Edge Deployment")

# Introduction section
st.markdown("""
Plastic waste segmentation involves identifying and categorizing plastic waste in real-time using edge devices like mobile phones, Raspberry Pi, or Nvidia Jetson Nano.
To achieve this, we use lightweight models that are optimized for performance and speed.
Below, you can find steps to implement this solution and download pre-trained models in **TFLite**, **TensorRT**, and **ONNX** formats.
""")

# Implementation steps
st.markdown("### Steps to Implement:")
st.markdown("""
1. **Model Optimization:** Convert a trained model (e.g., TensorFlow or PyTorch) to formats like TFLite, TensorRT, or ONNX for edge device compatibility.
2. **Edge Deployment:**
   - Use **TensorFlow Lite Interpreter** for mobile or embedded systems.
   - Use **TensorRT Runtime** for Nvidia GPUs like Jetson Nano.
   - Use **ONNX Runtime** for cross-platform support.
3. **Real-Time Inference:** Integrate the model with edge device hardware for on-the-fly segmentation.
4. **Testing and Performance Tuning:** Evaluate latency, accuracy, and power consumption.
""")

# Download model section
st.markdown("### Pre-Trained Models")
st.markdown("Access pre-trained models via the following links:")

# Links to models
yolo11l_tflite = "https://github.com/OmdenaAI/JaipurIndia_GangesRiverPlasticInterceptor/releases/download/V0.0.1/yolov11L_float16.tflite"
yolo11x_tflite = "https://github.com/OmdenaAI/JaipurIndia_GangesRiverPlasticInterceptor/releases/download/V0.0.1/yolov11x_float16.tflite"
yolo5x_engine = "https://github.com/OmdenaAI/JaipurIndia_GangesRiverPlasticInterceptor/releases/download/V0.0.1/yolov5x.engine"

st.markdown(f"""
- [Download YOLOv11 Large in TFLite]({yolo11l_tflite})  
- [Download YOLOv11 Extra-Large in TFLite]({yolo11x_tflite})  
- [Download YOLOv5 Extra-Large in TensorRT Model]({yolo5x_engine})
""")

# ONNX Models Section
st.markdown("### Pre-Trained ONNX Models")
st.markdown("""
ONNX (Open Neural Network Exchange) is a cross-platform format that supports multiple deep learning frameworks like PyTorch, TensorFlow, and Scikit-learn. ONNX models can be run on various platforms and are compatible with runtime engines like **ONNX Runtime**.

Below are some pre-trained ONNX models for plastic waste segmentation that can be used on a variety of edge devices, including platforms such as Nvidia Jetson Nano, Raspberry Pi, and even cloud servers.

""")

# Links to ONNX models
yolo11l_onnx = "https://github.com/OmdenaAI/JaipurIndia_GangesRiverPlasticInterceptor/releases/download/V0.0.1/yolov11L.onnx"
yolo11x_onnx = "https://github.com/OmdenaAI/JaipurIndia_GangesRiverPlasticInterceptor/releases/download/V0.0.1/yolov11x.onnx"
yolo5x_onnx = "https://github.com/OmdenaAI/JaipurIndia_GangesRiverPlasticInterceptor/releases/download/V0.0.1/yolov5x.onnx"

st.markdown(f"""
- [Download YOLOv11 Large in ONNX]({yolo11l_onnx})  
- [Download YOLOv11 Extra-Large in ONNX]({yolo11x_onnx})  
- [Download YOLOv5 Extra-Large in ONNX]({yolo5x_onnx})
""")

# Edge device compatibility
st.markdown("### Compatible Edge Devices")
st.markdown("""
- **Mobile Devices:** Android (via TensorFlow Lite), iOS, Microcontrollers, Raspberry Pi
- **Embedded Systems:** Raspberry Pi, Nvidia Jetson Nano, Nvidia Jetson Xavier NX
- **Cross-Platform:** Supports both Linux and Windows through ONNX Runtime
""")

st.markdown("For more details, visit the [documentation](https://www.tensorflow.org/lite), [Nvidia TensorRT resources](https://developer.nvidia.com/tensorrt), or [ONNX Runtime](https://onnxruntime.ai/).")
