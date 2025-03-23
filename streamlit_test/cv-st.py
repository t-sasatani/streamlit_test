import  cv2
import streamlit as st

st.title('Webcam')

placeholder1 = st.empty()
placeholder2 = st.empty()

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame1 = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame2 = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    placeholder1.image(frame1, channels='RGB')
    placeholder2.image(frame2, channels='GRAY')

cap.release()