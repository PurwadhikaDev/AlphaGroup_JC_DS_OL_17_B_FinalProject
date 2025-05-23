# Deskripsi Library

Notebook ini menggunakan berbagai library utama untuk analisis data, pemodelan machine learning, dan evaluasi model, di antaranya:

* **numpy, pandas**: manipulasi dan analisis data
* **matplotlib, seaborn**: visualisasi data
* **scikit-learn**: preprocessing, pipeline, model machine learning, dan evaluasi
* **imblearn**: penanganan data imbalanced (*SMOTE*, *EditedNearestNeighbours*)
* **lightgbm, xgboost**: algoritma boosting untuk klasifikasi
* **optbinning**: optimal binning pada fitur numerik
* **shap**: interpretasi model berbasis SHAP value
* **scipy**: analisis statistik dan uji inferensi
* **pickle, warnings, time, sys**: utilitas tambahan

Library di atas digunakan untuk membangun pipeline machine learning, eksplorasi data, penanganan data tidak seimbang, evaluasi model, serta interpretasi hasil prediksi.

---

# Ringkasan Isi Notebook

Notebook ini menyajikan pipeline komprehensif untuk analisis prediksi churn pelanggan e-commerce menggunakan machine learning dengan penekanan pada pencegahan data leakage. Berikut tahapan utama dalam notebook ini:

### 1. Data Cleaning & Persiapan

* Membersihkan data, menghapus duplikasi dan outlier.
* Melakukan normalisasi, konversi tipe data, dan imputasi nilai hilang menggunakan **Iterative Imputer**.

### 2. Feature Engineering & Binning

* Transformasi fitur numerik menggunakan **optbinning** untuk pembentukan bin optimal.
* Perhitungan **Weight of Evidence (WoE)** dan **Information Value (IV)** untuk seleksi fitur.

### 3. Feature Selection Berbasis Risiko Data Leakage

* Klasifikasi fitur menjadi: **Tidak Aman** (IV sangat tinggi, potensi *target leakage*), **Berisiko** (WoE ekstrem), dan **Aman** (nilai wajar).
* Evaluasi potensi data leakage pada fitur kategorikal.

### 4. Desain Skenario Pemodelan

* **Skenario 1**: Semua fitur digunakan (*baseline*).
* **Skenario 2**: Fitur tidak aman dihapus.
* **Skenario 3**: Fitur tidak aman dan berisiko dihapus.

### 5. Pembangunan Pipeline Machine Learning

* Pipeline otomatis meliputi preprocessing, binning, balancing data (*SMOTE*, *ENN*), dan training model.
* Model yang digunakan: **XGBoost, LightGBM, Random Forest, AdaBoost, Gradient Boosting**.

### 6. Hyperparameter Tuning & Evaluasi

* Optimasi model menggunakan **RandomizedSearchCV** dengan cross-validation, evaluasi menggunakan **F2-score**.
* Evaluasi performa model menggunakan **confusion matrix**, ROC, Precision-Recall, dan uji statistik **Wilcoxon**.

### 7. Interpretasi Model & Business Insight

* Analisis interpretabilitas menggunakan **SHAP** untuk identifikasi fitur penting.
* Insight bisnis mengenai strategi retensi, efisiensi promosi, dan segmentasi pelanggan.

### 8. Penyimpanan Model

* Model terbaik disimpan menggunakan **pickle**.

### 9. Kesimpulan & Saran

* Rangkuman performa model, batasan, insight EDA, dan rekomendasi strategi bisnis berbasis hasil analisis.
