import streamlit as st
import pandas as pd
import numpy as np
import time
import joblib
from streamlit_extras.switch_page_button import switch_page
# from tensorflow import keras
from keras.models import load_model


def get_predict(size, fuel, distance, desibel, airflow, frequency):
    # def get_predict():

    user_input = pd.DataFrame({
        'SIZE': [size],
        'FUEL': [fuel],
        'DISTANCE': [distance],
        'DESIBEL': [desibel],
        'AIRFLOW': [airflow],
        'FREQUENCY': [frequency]
    })

    if fuel == 'gasoline':
        user_input['gasoline'] = [1]
        user_input['kerosene'] = [0]
        user_input['lpg'] = [0]
        user_input['thinner'] = [0]
    else:
        user_input['gasoline'] = [0]
        user_input['kerosene'] = [1] if fuel == 'kerosene' else [0]
        user_input['lpg'] = [1] if fuel == 'lpg' else [0]
        user_input['thinner'] = [1] if fuel == 'thinner' else [0]

    data = user_input.drop('FUEL', axis=1)
    # test = pd.DataFrame({
    #     'SIZE': [2],
    #     # 'FUEL': [fuel],
    #     'DISTANCE': [10],
    #     'DESIBEL': [42],
    #     'AIRFLOW': [2],
    #     'FREQUENCY': [70],
    #     'gasoline': [1],
    #     'kerosone': [0],
    #     'lpg': [0],
    #     'thinner': [0]

    # })

    columns_to_normalize = ['DISTANCE', 'DESIBEL', 'AIRFLOW', 'FREQUENCY']

    scaler = joblib.load('model/minmax-model')
    model = load_model('model/ann-model.h5')

    data[columns_to_normalize] = scaler.transform(
        data[columns_to_normalize])

    # Convert the input features to a NumPy array
    # x_new = data.values

    prediction = model.predict(data)

    threshold = 0.5

    # Convert probabilities to binary labels using the threshold
    predicted_labels = (prediction > threshold).astype(int)
    # prediction = prediction > 0.5

    return predicted_labels


def main():

    st.set_page_config(
        page_title="Aplikasi Prediksi Keberhasilan Alat Pemadam Kebaran Berbasis Gelombang Suara ",
        page_icon="👨‍🚒", initial_sidebar_state="collapsed")

    st.markdown(
        """
        <style>
            [data-testid="collapsedControl"] {
                display: none
            }
        </style>
        """, unsafe_allow_html=True,
    )
    if st.button("👈 Kembali ke Home"):
        switch_page('app')

    st.image("assets/banner.png")

    st.header("Home Page")
    st.write("Masukkan beberapa parameter yang digunakan untuk alat pemadam kebakaran berbasis gelombang suara")

    col1, col2 = st.columns(2)

    with col1:
        size = st.selectbox(
            'Ukuran nyala api',
            (1, 2, 3, 4, 5))
        fuel = st.selectbox(
            'Bahan Bakar', ('gasoline', 'kerosene', 'thinner', 'lpg'))
        distance = st.text_input('Distance (cm)')
    with col2:
        desibel = st.text_input('Desibel (db)')
        airflow = st.text_input('Airflow (m/s)')
        frequency = st.text_input('Frequency (Hz)')

    if st.button("Prediksi Sekarang"):
        if size and fuel and distance and desibel and airflow and frequency:

            prediction_result = get_predict(
                size, fuel, distance, desibel, airflow, frequency)

            if prediction_result == 1:
                st.success('Hasil Prediksi =  Api Padam!', icon="✅")
            else:
                st.warning('Hasil Prediksi =  Api tidak Padam!', icon="❌")

        else:
            time.sleep(0.5)
            st.toast('Masukkan semua isian pada form', icon='🤧')


if __name__ == '__main__':
    main()
