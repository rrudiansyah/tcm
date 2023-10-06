import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
sns.set(style='dark')

st.header('Bike Sharing Dashboard :sparkles:')

datetime_columns = ["Tgl Permohonan Lab", "Tgl Hasil dilaporkan", "tanggal"]

all_df = pd.read_csv("dashboard/all_data.csv")

for column in datetime_columns:
    all_df[column] = pd.to_datetime(all_df[column])

min_date = all_df["Tgl Permohonan Lab"].min()
max_date = all_df["Tgl Permohonan Lab"].max()

with st.sidebar:
    # Menambahkan logo perusahaan
    st.image("https://github.com/dicodingacademy/assets/raw/main/logo.png")

    # Mengambil start_date & end_date dari date_input
    start_date, end_date = st.date_input(
        label='Rentang Waktu', min_value=min_date,
        max_value=max_date,
        value=[min_date, max_date]
    )
