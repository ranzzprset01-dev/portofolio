import streamlit as st
import base64
import os

st.markdown(
    """
    <style>
    [data-testid="stSidebar"] {
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 50%, #15803d 100%);
        border-right: 10px solid #22c55e; /* Aksen hijau neon sesuai tema config Anda */
    }

    [data-testid="stSidebar"] * {
        color: #f8fafc; /* Warna teks putih */
    }

    [data-testid="stSidebar"] [data-testid="stWidgetLabel"] {
        background_color: #22c55e;
        color: black !important;
        border-radius: 8px;
        font-weight: bold; 
    }
    [data-testid="stSidebar"] [data-testid="stWidgetLabel"] + div[role="radiogruop"] label[data-checked="true"] {
        background_color: #22c55e;
        color: black !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 50%, #15803d 100%);
    }
    /* Style tambahan untuk mempercantik tabel */
    .biodata-table {
        width: 100%;
        border-collapse: collapse;
        color: #f8fafc;
        font-family: sans-serif;
    }
    .biodata-table td {
        padding: 12px;
        border-bottom: 1px solid rgba(255, 255, 255, 0.1);
    }
    .label-kolom {
        font-weight: bold;
        color: #22c55e; /* Aksen hijau neon sesuai tema config Anda */
        width: 30%;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("<h1 style='text-align: center;'>HALAMAN KEMAMPUAN<h1>", unsafe_allow_html=True)
st.write("SELAMAT DATANG DIHALAMAN KEMAMPUAN, INI ADALAH KEMAMPUAN SAYA SENDIRI")
st.page_link("home.py", label="kembali ke beranda")
st.markdown("### **MY ABILITY/KEMAMPUAN**")

col1, col2 = st.columns([1, 2])

with col1:
    st.image("pages/alightmotion.webp", width=400)

with col2:
    tabel_html = """
    <table class="biodata-table">
        <tr>
            <td class="label-kolom">Kemampuan</td>
            <td>Editing foto & Video alightmotion, keyflow, wink, capcut, JJ, animation</td>
        </tr>
        <tr>
            <td class="label-kolom">Hobi</td>
            <td>bermain gitar, badminton, ngoding & editing</td>
        </tr>
    </table>
    """
    st.markdown(tabel_html, unsafe_allow_html=True)