import streamlit as st
import pandas as pd
import numpy as np
import pickle
from PIL import Image
import base64
from sklearn.base import BaseEstimator, TransformerMixin


# ====== 1. Tambahkan background dari file lokal ======
def set_bg_from_local(image_file):
    with open(image_file, "rb") as img:
        encoded = base64.b64encode(img.read()).decode()
    bg_img_style = f"""
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{encoded}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}
    </style>
    """
    st.markdown(bg_img_style, unsafe_allow_html=True)


# Panggil fungsi untuk menyetel background
set_bg_from_local("background.png")

# ====== 2. Judul aplikasi ======
st.title(f"{'PREDIKSI CHURN PELANGGAN'.center(100)}")
st.markdown(f"{'Masukkan data pelanggan berikut untuk memprediksi kemungkinan churn:'.center(100)}")

# ====== 3. Input pengguna ======
PreferredLoginDevice = st.radio("Preferred Login Device", ['Phone', 'Computer'])
PreferredPaymentMode = st.radio("Preferred Payment Mode", ['Debit Card', 'UPI', 'Credit Card', 'Cash on Delivery', 'E wallet'])
# Gender = st.radio("Gender", ['Male', 'Female'])
Gender = st.radio("Gender", ['Male', 'Female'])
PreferedOrderCat = st.radio("Prefered Order Category", ['Fashion', 'Grocery', 'Laptop & Accessory', 'Mobile', 'Mobile Phone','Others'])
MaritalStatus = st.radio("Marital Status", ['Single', 'Divorced', 'Married'])
CityTier = st.radio("City Tier", [1, 2, 3])
SatisfactionScore = st.radio("Satisfaction Score \n(1 = Sangat Tidak Puas, 2 = Tidak Puas, 3 = Cukup, 4 = Puas, 5 = Sangat Puas)", [1, 2, 3, 4, 5])

# Hanya Complain yang pakai checkbox
Complain = st.checkbox("Pernah Complain?")
Complain = 1 if Complain else 0


# ==== Slider dengan rentang yang disarankan ====
WarehouseToHome = st.slider("Jarak Warehouse ke Rumah (km)", min_value=5.0, max_value=36.0, value=10.0, step=0.5)
HourSpendOnApp = st.slider("Jam yang Dihabiskan di Aplikasi", min_value=0.0, max_value=4.0, value=2.5, step=0.1)
NumberOfDeviceRegistered = st.slider("Jumlah Perangkat Terdaftar", min_value=1, max_value=6, value=2)
NumberOfAddress = st.slider("Jumlah Alamat yang Digunakan", min_value=1, max_value=20, value=3)
OrderAmountHikeFromlastYear = st.slider("Kenaikan Jumlah Order Dari Tahun Lalu(%)", min_value=11.0, max_value=26.0, value=15.0, step=0.5)
OrderCount = st.slider("Jumlah Pesanan", min_value=1, max_value=16, value=3)
DaySinceLastOrder = st.slider("Hari Sejak Pesanan Terakhir", min_value=0, max_value=18, value=5, step=1)

# ====== 4. Data input pengguna ======
input_df = pd.DataFrame([{
    'PreferredLoginDevice': PreferredLoginDevice,
    'PreferredPaymentMode': PreferredPaymentMode,
    'Gender': Gender,
    'PreferedOrderCat': PreferedOrderCat,
    'MaritalStatus': MaritalStatus,
    'CityTier': CityTier,
    'SatisfactionScore': SatisfactionScore,
    'Complain': Complain,
    'WarehouseToHome': WarehouseToHome,
    'HourSpendOnApp': HourSpendOnApp,
    'NumberOfDeviceRegistered': NumberOfDeviceRegistered,
    'NumberOfAddress': NumberOfAddress,
    'OrderAmountHikeFromlastYear': OrderAmountHikeFromlastYear,
    'OrderCount': OrderCount,
    'DaySinceLastOrder': DaySinceLastOrder,
}])

# ====== 5. Load model ======
class OptBinningTransformer(BaseEstimator, TransformerMixin):
    def __init__(self, splits):
        self.splits = splits

    def fit(self, X, y=None):
        # Sudah fit splits di luar
        return self

    def transform(self, X):
        X_ = np.asarray(X)
        if X_.ndim == 1:
            X_ = X_.reshape(-1, 1)
        vals = X_[:, 0]
        return np.digitize(vals, bins=self.splits).reshape(-1, 1)
with open("xgb_model_skenario3rev02.pkl", "rb") as f:
    model = pickle.load(f)

# ====== 6. Prediksi ======
if st.button("Prediksi Churn"):
    proba = model.predict_proba(input_df)[0][1]

    if proba >= 0.404:
        st.error(f"🚨 Pelanggan diprediksi akan churn. Probability = {proba:.3f} ≥ Threshold(0.404)")
    else:
        st.success(f"✅ Pelanggan diprediksi tidak churn. Probability = {proba:.3f} < Threshold(0.404)")

