# Churn Prediction API with FastAPI

Bu proje, bir bankanın müşterilerinin bankadan ayrılıp ayrılmayacağını (`churn`) tahmin eden bir makine öğrenmesi modeli geliştirmeyi ve bu modeli bir REST API olarak FastAPI ile yayınlamayı amaçlamaktadır.

---

## 📁 Proje İçeriği

- `data_preprocessing.py`: Veri temizleme, eğitim ve model kaydetme dosyası
- `main.py`: FastAPI uygulaması
- `models.py`: Pydantic veri modelleri
- `requirements.txt`: Gerekli Python kütüphaneleri
- `churn_model.joblib`: Eğitilmiş model (çıktı)
- `Churn_Modelling.csv`: Girdi veri seti

---

## 🛠️ Kurulum

### 1. Gerekli araçlar

- Python 3.8+ (Conda/venv ile önerilir)
- FastAPI, scikit-learn, pandas, joblib
- Sanal makine üzerinde SSH erişimi sağlanmalı

### 2. Ortamı oluştur

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt