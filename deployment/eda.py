# import library
import pandas as pd
import streamlit as st

# library for visualization
from PIL import Image

def run():
# set the title
    st.title('Premi Asuransi Kesehatan')

    # set subheader
    st.subheader('Halaman ini menampilkan hasil EDA')

    # upload gambar
    image = Image.open('EDApict.png')
    st.image(image, caption='')

    # garis horizontal
    st.write('---')

    # subjudul
    st.write ('## DataFrame')

    #loading dataset
    df = pd.read_csv('Medicalpremium.csv')

    # menampilkan dafatrame
    st.dataframe(df)
    st.write('---')

    # visualisasi
    st.write('## EDA')

    st.subheader('Perbandingan Premi Asuransi Kesehatan dengan Usia Tertanggung')
    image = Image.open('eda1.png')
    st.image(image, caption='Premi Asuransi Kesehatan berdasarkan Usia')

    with st.expander('Explanation'):
        st.caption('Dari grafik ini terlihat bahwa Usia mempengaruhi harga rata - rata premi Asuransi Kesehatan, semakin besar nilai premi tertanggung dikarenakan usia tertanggung lebih tua')
    
    st.subheader('perbandingan Harga Premi Asuransi dengan Riwayat Cancer di Keluarga')
    image = Image.open('eda2.png')
    st.image(image, caption='Premi Asuransi Kesehatan berdasarkan Cancer')

    with st.expander('Explanation'):
        st.caption('Harga rata - rata premi untuk tertanggung yang memiliki riwayat Cancer di keluarga jauh lebih besar daripada yang tidak memiliki riwayat cancer di keluarga')

    st.subheader('Perbandingan Harga Premi Asuransi dengan Riwayat Penyakit Akut')
    image = Image.open('eda3.png')
    st.image(image, caption='Premi Asuransi Kesehatan berdasarkan Riwayat Penyakit Akut')

    with st.expander('Explanation'):
        st.caption('Harga rata - rata premi untuk tertanggung yang memiliki riwayat penyakit akut seperti asma jauh lebih besar daripada yang tidak memiliki riwayat penyakit akut')

    st.subheader('Perbandingan Harga Premi Asuransi dengan Riwayat Transplantasi Organ')
    image = Image.open('eda4.png')
    st.image(image, caption='Premi Asuransi kesehatan berdasarkan Riwayat Transplantasi Organ')

    with st.expander('Explanation'):
        st.caption('Harga rata - rata premi untuk tertanggung yang memiliki riwayat transplantasi organ jauh lebih besar daripada yang tidak ada riwayat transplantasi organ')

    st.subheader('Perbandingan Harga Premi Asuransi dengan Frekuensi Operasi Besar')
    image = Image.open('eda5.png')
    st.image(image, caption='Harga Premi Asuransi Kesehatan berdasarkan Frekuensi Operasi Besar')

    with st.expander('Explanation'):
        st.caption('Riwayat operasi besar mempengaruhi harga premi asuransi tertanggung dan semakin banyaknya operasi yang telah dilalui maka semakin besar harga premi tertanggung')
        
    st.subheader('Perbandingan Harga Premi Asuransi dengan Penyakit Tekananan Darah')
    image = Image.open('eda6.png')
    st.image(image, caption='Harga Premi Asuransi Kesehatan berdasarkan Riwayat Penyakit Tekanan Darah')

    with st.expander('Explanation'):
        st.caption('Harga rata - rata premi untuk tertanggung yang memiliki riwayat penyakit tekanan darah tinggi jauh lebih besar daripada yang tidak ada riwayat penyakit tekanan darah tinggi')
    
    st.subheader('Hubungan korelasi antara Usia, Harga Premi, dan Transplantasi Organ')
    image = Image.open('eda7.png')
    st.image(image, caption='Hubungan antara Usia, Harga Premi, dan Transplantasi Organ')

    with st.expander('Explanation'):
        st.caption('Usia berkolerasi linier dengan Harga Premium, adanya Transplantasi Organ membuat harga premi tertanggung jauh lebih mahal walaupun usia tertanggung masih muda')

if __name__=="__main__":
    run()
