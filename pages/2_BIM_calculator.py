import streamlit as st
from matplotlib import image
import os

# absolute path to this file
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# absolute path to this file's root directory
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
# absolute path of directory_of_interest
dir_of_interest = os.path.join(PARENT_DIR, "resources")
IMAGE_PATH1 = os.path.join(dir_of_interest, "images", "download.jpg")
st.title("BMI")
img1 = image.imread(IMAGE_PATH1)
st.image(img1, width=400)

st.header("What is BMI Calculator?")
st.write("""
BMI calculator is a tool that helps to determine a person's body mass index (BMI). BMI is a measure of body fat based on height and weight. The formula used to calculate BMI is weight (in kilograms) divided by height (in meters) squared.

A BMI calculator typically asks for the individual's weight and height and then calculates their BMI automatically. The resulting number is then compared to standardized BMI categories to determine whether the person is underweight, normal weight, overweight, or obese. The BMI categories are as follows:

**Underweight**: BMI below 18.5

**Normal weight**: BMI between 18.5 and 24.9

**Overweight**: BMI between 25 and 29.9

**Obese**: BMI 30 or higher

It's important to note that BMI is not always an accurate measure of body fat and does not take into account factors such as muscle mass or body composition. Additionally, BMI should be used in conjunction with other health indicators, such as waist circumference and overall health status, to determine a person's overall health risk.
""")

st.header("Calculate your BMI")
weight= st.number_input("Enter your Weight in KG", step=0.1)
height=st.number_input("Enter your Height in Meters", step=0.1)
bmi = weight/(height)**2
st.success(f"your BMI is{bmi}")