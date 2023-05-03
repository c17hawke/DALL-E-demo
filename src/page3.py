import streamlit as st
import openai
from PIL import Image
from src.utils import get_width_height, resize_image

def page3():
    st.title("OpenAI DALL·E Image Variation")
    st.info("""#### NOTE: you can download image by \
    right clicking on the image and select save image as option""")

    with st.form(key='form'):
        uploaded_file = st.file_uploader("Choose an image file", type=['png', 'jpg'])
        size = st.selectbox('Select size of the images', 
                            ('256x256', '512x512', '1024x1024'))
        num_images = st.selectbox('Enter number of images to be generated', (1,2,3,4))
        submit_button = st.form_submit_button(label='Submit')

    if submit_button:
        if uploaded_file is not None:

            image = Image.open(uploaded_file)
            
            st.image(image, caption="Uploaded image", use_column_width=True)
            
            width, height = get_width_height(size)
            image = resize_image(image, width, height)
            
            response = openai.Image.create_variation(
                    image=image,
                    n = num_images,
                    size=size,
                )
            
            for idx in range(num_images):
                image_url = response["data"][idx]["url"]

                st.image(image_url, caption=f"Generated image: {idx+1}",
                         use_column_width=True)
