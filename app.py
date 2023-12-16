import streamlit as st
from streamlit_extras.switch_page_button import switch_page


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
    st.image("assets/banner.png")

    st.header("Selamat Datang 👋")
    st.write("Dataset yang digunakan pada projek ini adalah record data hasil uji coba pemadaman api menggunakan alat pemadam berbasis gelombang suara. Proses pengujian ini terdapat beberapa parameter yang digunakan pada alat tersebut sehingga parameter ini mempengaruhi hasil akhir yang diujikan yaitu api akan padam atau tidak. Tujuan dari projek ini adalah untuk melakukan klasifikasi berdasarkan dataset yang digunakan menggunakan salah satu algoritma yaitu Artificial Neural Network (ANN).")

    if st.button("Mulai Prediksi 👉"):
        switch_page('prediction')


if __name__ == '__main__':
    main()
