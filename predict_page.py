import streamlit as st
import pickle
import numpy as np

def load_model():
    with open('saved_steps.pkl','rb') as file:
        data = pickle.load(file)
    return data

data = load_model()

regressor_model = data['model']

def show_predict_page():
    st.title('Calories burnt predictor')

    st.write("""### We need some information by you to predict calories burnt""")

    gender =('male','female')
    #genderOptions will containt the value for gender ( male or female)
    genderOptions = st.selectbox("Gender",gender)

    ageNumber = st.slider("Age",1,150,25)

    heightValue = st.text_input('Height (in cm)')

    weightValue = st.text_input('Weight (in kgs)')

    durationValue = st.text_input('Duration (in minutes)')

    tempValue = st.text_input('Body Temperature (in Celsius)')

    heartRateValue = st.text_input('Heart Rate (in seconds)')
    ok = st.button("Calculate calories burned")

    if ok:
        genderNumber = 0
        if genderOptions == "male":
            genderNumber = 1
        #X will be used to calculate the number of calories burnt
        X = np.array([[float(genderNumber),int(ageNumber),float(heightValue),float(weightValue),float(durationValue),float(heartRateValue),float(tempValue)]])

        Calories_burnt = regressor_model.predict(X)
        st.subheader(f"The estimated number of calories burned are : {Calories_burnt[0]:.3f}")
 