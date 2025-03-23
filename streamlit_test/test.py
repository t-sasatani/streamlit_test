import cv2
import streamlit as st

if __name__ == '__main__':
    input_num = st.number_input('Input a number', value=0)

    result = input_num ** 2
    st.write(f'The square of {input_num} is {result}')
