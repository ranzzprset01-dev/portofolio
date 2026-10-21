import streamlit as st

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

st.markdown("<h1 style='text-align: center;'>HALAMAN BERANDA<h1>", unsafe_allow_html=True)

st.set_page_config(
    page_title="My portofolio",
    page_icon="🏘️home",
    layout="wide",
    
)
col1, col2, col3, col4, col5 = st.columns([2, 1, 2, 1, 2])

with col1:
    st.image("PORTOFOLIO/pages/OIP.webp", width=200)
    st.page_link("pages/kemampuan.py", label="lihat kemampuan", use_container_width=True)
    st.page_link("pages/profil.py", label="lihat profil", use_container_width=True)
    st.page_link("pages/sosmed.py", label="lihat sosmed", use_container_width=True)
with col3:
    st.video("PORTOFOLIO/pages/my video.mp4",width=1000, autoplay=True, muted=False, loop=True)
with col5:
    st.image("PORTOFOLIO/pages/unduhan.jpeg", width=200)
    st.image("PORTOFOLIO/pages/unduhan.webp", width=200)
