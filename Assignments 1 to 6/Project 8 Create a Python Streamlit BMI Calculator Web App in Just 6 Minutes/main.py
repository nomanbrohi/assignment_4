import streamlit as st
import pandas as pd

st.title("BMI Calculator")

height = st.slider("Select your Height in CM: ", 1, 250, 70)
weight = st.slider("Select your weight in KG:", 1, 300, 30)

bmi = weight / ((height/100) ** 2)

st.write(f"Your BMI = {bmi:.2f} ")

listCategory = ["Underweight", "Normal Weight", "Overweight","Moderate", "Severe", "Very Severe" ]
tag =" 🟢 "

if bmi < 18.5:
    listCategory[0] = tag + " " + listCategory[0]
elif 18.5 <= bmi < 24:
    listCategory[1] = tag + " " + listCategory[1]
elif 24 <= bmi < 30:
    listCategory[2] = tag + " " + listCategory[2]
elif 30 <= bmi < 35:
    listCategory[3] = tag + " " + listCategory[3]
elif 35 <= bmi < 40:
    listCategory[4] = tag + " " + listCategory[4]
else:
    listCategory[5] = tag + " " + listCategory[5]

st.write("***BMI Categories***")

for i in listCategory:
    st.write(i)