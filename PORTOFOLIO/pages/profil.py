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

def pasang_background(cyberpunk_image_path):
    with open(cyberpunk_image_path, "rb") as f:
        data_url = base64.b64encode(f.read()).decode("utf-8")
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/webp;base64,{data_url}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

pasang_background("pages/cyberpunk.webp")

st.markdown(
    """
    <style>
    .label-kolom {
        font-weight: bold;
        color: #22c55e; /* Aksen hijau neon sesuai tema config Anda */
        width: 50%;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("<h1 style='text-align: center;'>HALAMAN PROFIL/DATA DIRI<h1>", unsafe_allow_html=True)
st.page_link("home.py", label="kembali ke beranda")

# Membuat 2 kolom dengan rasio lebar (1 untuk foto : 2 untuk tabel biodata)
col1, col2 = st.columns([1, 2])

with col1:
    # Memasukkan foto ke kolom kiri
    st.image("PORTOFOLIO/pages/Proyek Baru 140.jpg", width="stretch")

with col2:
    st.markdown("### **BIODATA MAHASISWA**")

    tabel_html = """
    <style>
    .label-kolom {
        color: #22c55e; /* Aksen hijau neon sesuai tema config Anda */
        font-weight: bold;
        background-color: rgba(0, 0, 0, 0.5);
        padding: 8px;
        border-radius: 5px;
    }
    .value-kolom {
        color: #f8fafc; /* Warna teks putih */
        background-color: rgba(0, 0, 0, 0.5);
        padding: 8px;
        border-radius: 5px;
    }
    </style>
    <table class="biodata-table">
        <tr>
            <td class="label-kolom">NAMA</td>
            <td class="value-kolom">: RANDI PRASETYO</td>
        </tr>
        <tr>
            <td class="label-kolom">NIM</td>
            <td class="value-kolom">: 25111068</td>
        </tr>
        <tr>
            <td class="label-kolom">PRODI</td>
            <td class="value-kolom">: SISTEM INFORMASI</td>
        </tr>
        <tr>
            <td class="label-kolom">MATKUL</td>
            <td class="value-kolom">: PEMROGRAMMAN BERBASIS PLATFORM</td>
        </tr>
    </table>
    """
    st.markdown(tabel_html, unsafe_allow_html=True)
