import cv2
import streamlit as st
import time

# Set the desired FPS
desired_fps = 20
frame_interval = 1.0 / desired_fps

st.title('Webcam')

placeholder1 = st.empty()
placeholder2 = st.empty()
fps_display = st.empty()

cap = cv2.VideoCapture(0)

# Check if the webcam is opened correctly
if not cap.isOpened():
    st.error("Could not open the webcam.")
else:
    last_frame_time = time.time()

    # Loop for capturing and displaying frames
    while True:
        current_time = time.time()
        time_since_last_frame = current_time - last_frame_time

        # Check if it's time to capture the next frame
        if time_since_last_frame >= frame_interval:
            ret, frame = cap.read()
            if not ret:
                st.error("Cannot receive frame (stream end?). Exiting ...")
                break

            frame1 = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame2 = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # Update frames in the streamlit placeholders
            placeholder1.image(frame1, channels='RGB')
            placeholder2.image(frame2, channels='GRAY')

            # Update the time of the last frame
            last_frame_time = current_time

            # Display actual FPS
            actual_fps = 1.0 / time_since_last_frame
            fps_display.text(f"Actual FPS: {actual_fps:.2f}")

cap.release()