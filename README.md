# 📦 E-Commerce Customer Churn Prediction

## 1. Business Understanding

### 1.1 Context
Industri e-commerce sangat kompetitif, dan pelanggan dapat dengan mudah berpindah platform jika tidak puas. Maka, penting untuk memahami dan mengantisipasi churn (berhentinya pelanggan menggunakan layanan).  
**Target:**
- 0: Tidak churn
- 1: Churn  
Churn rate saat ini: **16.84%**

### 1.1.1 Market Overview
E-commerce berkembang pesat, terutama pasca-COVID-19, dengan CAGR global mencapai **6.23%** (2025–2030). Pertumbuhan signifikan terjadi di Asia-Pasifik, didorong oleh meningkatnya kelas menengah dan penetrasi digital.

### 1.1.2 Potential Stakeholders
- Pelanggan
- Pegawai retail
- Vendor
- Shareholders & investors
- Pesaing
- Payment gateway

### 1.2 Problem Statement
Tingkat churn saat ini melebihi ambang ideal industri (5–10%). Kehilangan pelanggan lebih mahal dibanding mempertahankannya. Meningkatkan retensi 5% dapat menaikkan profit hingga 95%.

### 1.3 Goals
Mengembangkan model prediksi churn untuk mengidentifikasi pelanggan berisiko dan mendukung strategi retensi.

### 1.4 Analytics Approach
- Eksplorasi data & identifikasi pola
- Bangun model klasifikasi
- Prediksi risiko churn
- Lakukan intervensi proaktif

### 1.5 Metric Evaluation
- Fokus utama: **minimalkan False Negative (FN)**
- **F2-Score** digunakan karena menekankan recall sambil tetap memperhatikan precision.

### 1.6 Limitation and Benefits
✅ **Manfaat**:
- Target biner mudah diinterpretasi
- Kombinasi fitur numerik & kategorikal

⚠️ **Batasan**:
- Tidak ada timestamp
- Beberapa satuan nilai tidak jelas
- Potensi bias dari proporsi unik

---

## 2. Data Preparation

- Hapus duplikat & outlier
- Imputasi:
  - Numerik: Iterative Imputer + XGBoost
  - Kategorikal: modus
- Binning fitur numerik: OptBinning
- Perhitungan WoE & IV
- Klasifikasi fitur:
  - Aman
  - Berisiko
  - Tidak Aman (berpotensi leakage)

---

## 3. Exploratory Data Analysis (EDA)

- Univariate: distribusi tiap fitur
- Feature vs Churn: hubungan keluhan, pesanan, dan durasi penggunaan
- Anomali: SatisfactionScore pakai skala Likert terbalik
- Imbalance: churn hanya 16.84% → perlu balancing
- Pola bisnis:
  - Jarak jauh → churn
  - Pelanggan pasif & pengeluh → churn

---

## 4. Machine Learning

### 4.1 Skenario Pemodelan
- **S1**: Semua fitur
- **S2**: Drop fitur tidak aman
- **S3**: Drop fitur tidak aman & berisiko

### 4.2 Pipeline & Model
- Preprocessing: imputasi, binning, encoding
- Balancing: SMOTE, ENN
- Model: XGBoost, LightGBM, RF, AdaBoost, Gradient Boosting

### 4.3 Evaluasi
- Cross-validation + RandomizedSearchCV
- Metrik utama: **F2-Score**
- Evaluasi: confusion matrix, ROC, PR-curve, Wilcoxon test
- Interpretasi model: **SHAP analysis**

---

## 5. Kesimpulan

### 5.1 Performa Model
- Model terbaik: **XGBoost** dengan threshold **0.404**
- **F2-score**: 0.911 | **Recall churn**: 92% | **Akurasi**: 97%
- Distribusi:
  - TP = 166 | FP = 21 | FN = 15 | TN = 891

### 5.2 Batasan Model

#### 5.2.1 Rentang Nilai Ideal Fitur
| Fitur                        | Rentang Ideal     |
|-----------------------------|-------------------|
| WarehouseToHome             | 5 – 36 km         |
| HourSpendOnApp              | 0 – 4 jam         |
| NumberOfDeviceRegistered    | 1 – 6 perangkat   |
| NumberOfAddress             | 1 – 20 alamat     |
| OrderAmountHikeFromlastYear | 11 – 26           |
| OrderCount                  | 1 – 16 pesanan    |
| DaySinceLastOrder           | 0 – 18 hari       |

#### 5.2.2 Identifikasi Fitur Berisiko Leakage
- **Tidak Aman**: `Tenure` (IV 1.759, WoE ekstrem)
- **Beresiko**: `CashbackAmount`, `CouponUsed` (WoE > 1.5)
- **Aman**: `WarehouseToHome`, `OrderCount`, dsb.

### 5.3 Efisiensi Promosi

**Skenario:**
- Tanpa model → Rp109.300.000 (semua diberi promosi)
- Dengan model → Rp18.700.000 (hanya 187 pelanggan)

**Efisiensi**: Rp90.600.000 (→ 82.89%)

### 5.4 Insight dari EDA

- **Personalisasi** UI/UX & rekomendasi produk
- **Optimasi logistik** untuk pelanggan jauh
- **Diversifikasi pembayaran** (hindari ketergantungan UPI)
- **Target segmen** elektronik & fashion → strategi spesifik
- **Survey feedback** & CS responsif untuk pelanggan komplain

---

## 6. Saran

Beberapa fitur menunjukkan indikasi **leakage** karena dapat merepresentasikan informasi *pasca-churn*:

| Fitur                  | Potensi Leakage |
|------------------------|-----------------|
| Tenure                | Durasi sampai churn |
| CashbackAmount        | Retensi akhir? |
| CouponUsed            | Intervensi pasca-churn? |
| OrderAmountHike       | Cerminkan pola akhir? |
| OrderCount            | Jika tidak dibatasi waktu |
| DaySinceLastOrder     | Terkesan "tidak aktif" setelah churn |

### 🛡️ Rekomendasi:
- Pastikan semua fitur **dicatat sebelum** churn.
- Sertakan **timestamp atau snapshot waktu**.
- Hindari fitur dengan data "masa depan" untuk menjaga keabsahan prediksi.

---
