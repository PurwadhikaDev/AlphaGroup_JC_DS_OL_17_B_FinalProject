# 📦 E-Commerce Customer Churn Prediction

# PART 1 : PREPROCESSING
## 🎯 Business Understanding

- Industri e-commerce sangat kompetitif, churn pelanggan menjadi ancaman nyata.
- Churn rate saat ini: 16.84% → jauh di atas rata-rata ideal industri (5–10%).
- Retensi lebih murah dan menguntungkan daripada akuisisi pelanggan baru.
- Target klasifikasi: 0 = tidak churn, 1 = churn.
- Tujuan: membangun model prediksi churn untuk mendukung strategi retensi.
- Pendekatan: eksplorasi data → model klasifikasi → intervensi proaktif.
- Metrik utama: **F2-Score** untuk meminimalkan **False Negatives** (FN).
- Stakeholders utama: pelanggan, vendor, investor, pesaing, payment gateway.

## 🧹 Data Preparation

- Hapus duplikasi dan outlier.
- Imputasi nilai hilang:
  - Numerik: Iterative Imputer + XGBoost.
  - Kategorikal: modus.
- Transformasi numerik: OptBinning + WoE/IV.
- Klasifikasi fitur:
  - Aman
  - Berisiko (WoE ekstrem)
  - Tidak aman (IV tinggi → potensi leakage)
---
# PART 2: EDA
## 📊 Exploratory Data Analysis (EDA)

- Distribusi fitur numerik dan kategorikal dianalisis.
- Fitur dengan hubungan kuat ke churn: `Complain`, `OrderCount`, `SatisfactionScore`, `WarehouseToHome`.
- Ketimpangan kelas: churn hanya 16.84% → perlu balancing.
- Ditemukan anomali pada `SatisfactionScore` (skala terbalik).
- Pola churn muncul pada pelanggan pasif, lokasi jauh, dan metode pembayaran eksternal.

---
# PART 3: MACHINE LEARNING
## 🤖 Machine Learning

- Tiga skenario model:
  - Semua fitur (baseline)
  - Drop fitur tidak aman
  - Drop fitur tidak aman + berisiko
- Model yang digunakan: XGBoost, LightGBM, Random Forest, AdaBoost, Gradient Boosting.
- Pipeline mencakup preprocessing, binning, encoding, SMOTE/ENN, dan evaluasi.
- Hyperparameter tuning dengan RandomizedSearchCV + Stratified K-Fold.
- Evaluasi dengan F2-score, confusion matrix, ROC, PR curve, dan uji Wilcoxon.
- Interpretasi model dilakukan dengan SHAP untuk menjelaskan fitur penting.

## ✅ Kesimpulan

- Model terbaik: **XGBoost**, threshold optimal = 0.404.
- F2-score = 0.911 | Recall = 92% | Akurasi = 97%
- Distribusi prediksi:
  - TP = 166
  - FP = 21
  - FN = 15
  - TN = 891
- Model efektif mengurangi churn dan siap dipakai di sistem produksi.

## ⚠️ Batasan

- Beberapa fitur tidak memiliki rentang wajar, perlu pembatasan:
  - WarehouseToHome: 5–36 km
  - OrderCount: 1–16 pesanan
  - DaySinceLastOrder: 0–18 hari
- Identifikasi leakage hanya berbasis WoE/IV (belum pakai timestamp).
- Fitur berpotensi leakage:
  - `Tenure`
  - `CashbackAmount`
  - `CouponUsed`
  - `OrderCount`
  - `OrderAmountHikeFromlastYear`
  - `DaySinceLastOrder`

## 💰 Efisiensi Biaya Promosi

- Skenario tanpa model: semua pelanggan → biaya Rp109,3 juta.
- Skenario pakai model: hanya 187 pelanggan target → biaya Rp18,7 juta.
- Efisiensi biaya promosi: **Rp90,6 juta (82.89%)**

## 💡 Insight Bisnis

- Perkuat personalisasi (UI/UX, rekomendasi, bundle).
- Perbaiki logistik: pengiriman cepat & transparan.
- Diversifikasi metode pembayaran → hindari churn karena opsi terbatas.
- Targetkan segmen elektronik & fashion dengan pendekatan yang relevan.
- Gunakan chatbot, survey, dan CS responsif untuk kurangi churn akibat komplain.

## 🛡️ Saran

- Hindari fitur yang mengandung informasi "masa depan".
- Sertakan timestamp atau snapshot data historis untuk validasi waktu fitur.
- Lakukan verifikasi data sebelum digunakan dalam model produksi.
- Prioritaskan fitur yang relevan dan aman untuk prediksi prospektif.
