import streamlit as st
import numpy as np
import cv2
from PIL import Image
import os

from tensorflow.keras.models import load_model

model = load_model('modell.h5')

# Function to preprocess the uploaded image
def preprocess_image(img_path):
    img = cv2.imread(img_path)

    img_resized = cv2.resize(img, (224, 224))

    img_normalized = img_resized / 255.0

    img_normalized = np.expand_dims(img_normalized, axis=0)

    print(img_normalized.shape)  

    img_final = np.array(img_normalized)

    print(img_final)

    return img_final

# Function to make predictions
def predict(img_arr):
    prediction = model.predict(img_arr)
    return prediction

def save_uploaded_image(uploaded_image):
    try:
        with open(os.path.join('uploads',uploaded_image.name),'wb') as f:
            f.write(uploaded_image.getbuffer())
        return 1
    except:
        return 0

# Streamlit app
st.title('NSFW Classifier')
st.write('This is a simple NSFW image classifier. Please upload an image to classify it.')

# Upload image
uploaded_image = st.file_uploader('Choose an image...', type=['jpg'])


if uploaded_image is not None:
    # Save Image
    if save_uploaded_image(uploaded_image):
        pass
    else :
        st.header("File Upload Error")

    # Display uploaded image
    image = Image.open(uploaded_image)
    st.image(image, caption='Uploaded Image', use_column_width=True)

    img_path=os.path.join("uploads",uploaded_image.name)
    print(img_path)

    # Preprocess and classify the image
    if st.button('Classify'):  
        img_arr = preprocess_image(img_path)
        prediction = predict(img_arr)

        print(prediction[0][0])
        # Display prediction result
        if prediction[0][0] < 0.05:
            st.write('This image is not safe for work. (Violent)')
        elif (prediction[0][0] > 0.95):
            st.write('This image is not safe for work. (Adult_Content)')
        else:
            st.write('This image is safe for work.')