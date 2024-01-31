# import libraries
import pandas as pd
import numpy as np
import streamlit as st
import joblib
from PIL import Image

# import pickle
import pickle

with open('model.pkl', 'rb') as file:
        model_premi = pickle.load(file)


def run():
    # Load All Files
    # set the title
    st.title("Prediksi Harga Premi Asuransi Kesehatan")
    st.write('---')

    image = Image.open('EDApict.png')
    st.image(image, caption='')

        
    with st.form(key='form parameter'):
        Age = st.number_input(label='Usia Tertanggung?', min_value=1,max_value=65)
        Weight = st.number_input(label='Berat Badan Tertanggung?', min_value=1,max_value=200)
        BloodPressureProblems = st.selectbox(label='Apakah ada Tekanan Darah?', options=[0, 1])
        AnyTransplants = st.selectbox(label='Apakah ada Penyakit Transplantasi Organ?', options=[0, 1])
        AnyChronicDiseases = st.selectbox(label='Apakah ada Penyakit Parah?', options=[0, 1])
        HistoryOfCancerInFamily = st.selectbox(label='Apakah ada Histori Penyakit Cancer di Keluarga?', options=[0, 1])
        NumberOfMajorSurgeries = st.selectbox(label='Apakah Pernah Operasi Besar?', options=[0, 1])
        submit = st.form_submit_button("Predict")

    st.write('Prediksi Harga Premi Asuransi')

    data_inf = pd.DataFrame({
        'Age' : Age,
        'Weight' : Weight,
        'BloodPressureProblems' : BloodPressureProblems,
        'AnyTransplants' : AnyTransplants,
        'AnyChronicDiseases' : AnyChronicDiseases,
        'HistoryOfCancerInFamily' : HistoryOfCancerInFamily,
        'NumberOfMajorSurgeries' : NumberOfMajorSurgeries,
        }, index=[0])

    st.table(data_inf)

    if submit:
        prediction =  model_premi.predict(data_inf)

        # if prediction[0] == 0:
        #     prediction = 'Lancar'
        # else:
        #     prediction = 'Gagal Bayar'

        st.subheader('Prediksi Harga Premi')
        st.subheader(prediction)

if __name__ == "_name_":
     run()