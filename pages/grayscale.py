import sys
sys.path.insert(1, '\\web_app1')
import streamlit as st
import functions
st.title("Color to Grayscale Converter")
uploaded_image = st.file_uploader("Upload Image")

with st.expander("Start Camera"):
    camera_image = st.camera_input("Camera")

if camera_image:
    gray_img = functions.convert_image_to_grayscale(camera_image)
    st.image(gray_img)
if uploaded_image:
    gray_img_file = functions.convert_image_to_grayscale(uploaded_image)
    st.image(gray_img_file)


