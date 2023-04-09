import streamlit as st
from matplotlib import image
import pandas as pd
import plotly.express as px

import os

# absolute path to this file
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# absolute path to this file's root directory
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
# absolute path of directory_of_interest
dir_of_interest = os.path.join(PARENT_DIR, "resources")
IMAGE_PATH1 = os.path.join(dir_of_interest, "images", "images.png")
IMAGE_PATH2 = os.path.join(dir_of_interest, "images", "weight.jpg")


st.title("What causes over weight?")
img1 = image.imread(IMAGE_PATH1)
st.image(img1, width=400)
st.write("Overweight and obesity are typically caused by a combination of genetic, environmental, and lifestyle factors. Some of the most common factors that contribute to overweight include:")
st.write("""
**Unhealthy diet**: Consuming a diet high in calories, saturated and trans fats, sugar, and processed foods can lead to weight gain.

**Lack of physical activity**: Sedentary lifestyles and lack of exercise can contribute to weight gain and obesity.

**Genetics**: Certain genes and inherited traits can make it easier for some people to gain weight.

**Medical conditions**: Hormonal imbalances, hypothyroidism, and other medical conditions can lead to weight gain.

**Medications**: Some medications, such as antidepressants and steroids, can contribute to weight gain.

**Psychological factors**: Stress, anxiety, depression, and other mental health conditions can contribute to overeating and weight gain.

**Sleep**: Inadequate sleep and sleep disorders such as sleep apnea can contribute to weight gain.""") 

st.title("Age and Weight Sheet")

img2 = image.imread(IMAGE_PATH2)
st.image(img2)