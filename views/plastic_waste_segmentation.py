import os
import uuid
import shutil
import streamlit as st
import cv2
import numpy as np

from PIL import Image
from yoloseg.YOLOSeg import YOLOSeg
from yoloseg.utils import pad_and_resize
from utils.utils import convert_to_mp4

# Define a cached function to load the YOLOSeg model
@st.cache_resource
def load_model(model_path, conf_thres=0.2, iou_thres=0.3):
    return YOLOSeg(model_path, conf_thres=conf_thres, iou_thres=iou_thres)

# Load the Model
base_dir = os.getcwd()
model_path = os.path.join(base_dir, "assets", "yolov11L.onnx")
yoloseg = load_model(model_path)

st.markdown("<h3 style='text-align: center;'>Plastic Waste Segmentation</h3>", unsafe_allow_html=True)

# Toggle between image and video segmentation
segmentation_type = st.radio(
    "Select Segmentation Type:",
    ("Image Segmentation", "Video Segmentation"),
    horizontal=True
)

temp_folder = os.path.join(base_dir, "temp")
os.makedirs(temp_folder, exist_ok=True)

try:
    if segmentation_type == "Image Segmentation":
        st.write("### Upload an Image")
        uploaded_image = st.file_uploader(
            "Choose an image file", type=["jpg", "jpeg", "png"])

        if uploaded_image:
            # Add a button to trigger segmentation
            if st.button("Run Segmentation"):
                # Initialize progress bar
                progress_bar = st.progress(0)
                progress_status = st.empty()

                # Step 1: Read the uploaded image
                progress_status.text("Loading image...")
                image = Image.open(uploaded_image)
                img = np.array(image)
                progress_bar.progress(20)

                # Step 2: Resize the input image
                progress_status.text("Resizing image...")
                input_img = pad_and_resize(img, (640, 640))
                progress_bar.progress(50)

                # Step 3: Perform segmentation
                progress_status.text("Performing segmentation...")
                boxes, scores, class_ids, masks = yoloseg(input_img)
                combined_img = yoloseg.draw_masks(input_img)
                progress_bar.progress(100)
                progress_status.text("Segmentation completed!")
                progress_bar.empty()

                # Display the uploaded image
                st.markdown("<h4 style='text-align: center;'>Input Image</h4>", unsafe_allow_html=True)
                st.image(image, use_container_width=True)

                st.markdown("---")

                # Display the segmented image
                st.markdown("<h4 style='text-align: center;'>Segmented Image</h4>", unsafe_allow_html=True)
                st.image(combined_img, use_container_width=True)

    elif segmentation_type == "Video Segmentation":
        st.write("### Upload a Video")
        uploaded_video = st.file_uploader("Choose a video file", type=["mp4"])

        if uploaded_video:
            # Add a button to trigger segmentation
            if st.button("Run Segmentation"):
                progress_status = st.empty()
                progress_status.text("Processing video...")

                # Save uploaded video to temp folder
                video_path = os.path.join(temp_folder, f"uploaded_video_{uuid.uuid4()}.mp4")
                with open(video_path, "wb") as video_file:
                    video_file.write(uploaded_video.read())

                # Load the video
                cap = cv2.VideoCapture(video_path)
                fps = cap.get(cv2.CAP_PROP_FPS)
                width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
                height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
                frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

                # Define codec and output path
                output_path = os.path.join(temp_folder, f"segmented_video_{uuid.uuid4()}.mp4")
                fourcc = cv2.VideoWriter_fourcc(*'mp4v')
                out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

                # Process video frame-by-frame
                progress_bar = st.progress(0)
                processed_frames = 0

                while cap.isOpened():
                    ret, frame = cap.read()
                    if not ret:
                        break

                    # Step 1: Prepare frame for segmentation
                    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                    input_frame = pad_and_resize(frame_rgb, (640, 640))

                    # Step 2: Perform segmentation
                    boxes, scores, class_ids, masks = yoloseg(input_frame)
                    combined_frame = yoloseg.draw_masks(input_frame, mask_alpha=0.4)

                    # Step 3: Resize and save segmented frame
                    combined_frame_resized = cv2.resize(combined_frame, (width, height))
                    combined_frame_bgr = cv2.cvtColor(combined_frame_resized, cv2.COLOR_RGB2BGR)
                    out.write(combined_frame_bgr)

                    # Update progress
                    processed_frames += 1
                    progress_bar.progress(processed_frames / frame_count)

                # Finalize processing
                cap.release()
                out.release()
                progress_bar.progress(100)
                progress_status.text("Segmentation completed!")
                progress_bar.empty()

                # Convert to final format if needed
                final_video_path = os.path.join(temp_folder, f"final_video_{uuid.uuid4()}.mp4")
                convert_to_mp4(output_path, final_video_path)
                st.video(final_video_path)

finally:
    # Clean up the temporary folder
    shutil.rmtree(temp_folder, ignore_errors=True)
