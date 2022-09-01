import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

@st.cache
def load_data():
    exercise = pd.read_csv('./exercise.csv')
    calories = pd.read_csv('./calories.csv')

    calories_info = pd.concat([exercise,calories['Calories']],axis=1)

    calories_info.replace({'Gender':{'male':1,'female':0}},inplace=True)
    return calories_info

calories_info = load_data() 


def show_explore_page():
       st.title('Welcome to the exploration database page for Calories Predictor')

       st.write("""### KAGGLE DATASET FOR CALORIES BURNT """)

       st.write("""### Mean number of calories burnt on the basis of age:  :""")

       data = calories_info.groupby(['Age'])['Calories'].mean().sort_values(ascending=True)

       st.line_chart(data)

       st.write("""### Mean number of calories burnt on the basis of gender (0 indicates women, while 1 indicates men)  :""")

       data = calories_info.groupby(['Gender'])['Calories'].mean().sort_values(ascending=True)

       st.bar_chart(data)

