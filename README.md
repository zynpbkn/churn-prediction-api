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

3. Veri setini indir

 https://raw.githubusercontent.com/erkansirin78/datasets/master/Churn_Modelling.csv

🚀 Model Eğitimi
Aşağıdaki komutu çalıştırarak modeli eğitin ve kaydedin:

data_preprocessing.py

Bu işlem:

5 kat çapraz doğrulama ile değerlendirme yapar.

GridSearchCV ile hiperparametreleri optimize eder.

Eğitilmiş modeli churn_model.joblib olarak kaydeder.

🌐 API’yi Çalıştırma

main:app --host 0.0.0.0 --port 8000

API’yi tarayıcıda test etmek için:

http://<VM_IP_ADRESİ>:8000/docs

📬 API Kullanımı
Endpoint: POST /prediction/churn
🔸 Örnek İstek:

{
  "CreditScore": 619,
  "Geography": "France",
  "Gender": "Female",
  "Age": 42,
  "Tenure": 2,
  "Balance": 0.0,
  "NumOfProducts": 1,
  "HasCrCard": 1,
  "IsActiveMember": 1,
  "EstimatedSalary": 101348.88
}
🔸 Örnek Yanıt:

{
  "churn_prediction": 0
}
🧪 API Testi (alternatif olarak curl ile)

curl -X POST "http://<VM_IP_ADRESİ>:8000/prediction/churn" \
  -H "Content-Type: application/json" \
  -d '{
    "CreditScore": 619,
    "Geography": "France",
    "Gender": "Female",
    "Age": 42,
    "Tenure": 2,
    "Balance": 0.0,
    "NumOfProducts": 1,
    "HasCrCard": 1,
    "IsActiveMember": 1,
    "EstimatedSalary": 101348.88
  }'
📝 Notlar
Port 8000 dış erişime açık olmalı (VirtualBox port yönlendirme yapılandırılmalı).

Model ve encoder'lar yerel diske joblib ile kaydedilir ve yüklenir.

models.py dosyası Swagger arayüzü için örnek veri sağlar.

Hatalı veri gönderildiğinde API 400/500 hatası döner.

