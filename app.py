import streamlit as st
from predict_page import show_predict_page
from explore_page import show_explore_page

page = st.sidebar.selectbox("Explore or Predict",('Predict Calorie Count','Explore the Construction'))

if page == 'Predict Calorie Count':
    show_predict_page()
else:
    show_explore_page()    


st.sidebar.write('If you like my work, do check me out at [LinkedIn](https://www.linkedin.com/in/mudit-nema-242a85210/)  ')
st.sidebar.write('[Github](https://github.com/MuditNema)')
st.sidebar.write('You can contact me at muditnema14@gmail.com')