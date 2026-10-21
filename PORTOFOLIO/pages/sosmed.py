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
        width: 50%;
    }
    </style>
    """,
    unsafe_allow_html=True
)
st.markdown("### **MEDIA SOSIAL**")

st.page_link("home.py", label="Kembali ke beranda", use_container_width=True)

col1, col2, col3 = st.columns([0.8, 1.5, 1])

with col1:
    st.image("pages/TIKTOK.webp", width=150)
    st.image("pages/INSTAGRAM.webp", width=150)

with col2:
    st.write("=====================================")
    st.link_button("TIKTOK : @bgranzzprset", url="https://www.tiktok.com/@bgranzzprset")    
    st.write("TIKTOK : @bgranzzprset")
    st.write("=====================================")
    st.link_button("INSTAGRAM : @bgranzzprset", url="https://www.instagram.com/bgranzzprset/")
    st.write("INSTAGRAM : @bgranzzprset")
    st.write("=====================================")