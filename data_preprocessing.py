import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import joblib

# Veriyi oku
df = pd.read_csv("https://raw.githubusercontent.com/erkansirin78/datasets/master/Churn_Modelling.csv")

# Kullanılmayacak sütunları çıkar
df.drop(['RowNumber', 'CustomerId', 'Surname'], axis=1, inplace=True)

# Giriş ve hedef değişkenleri ayır
X = df.drop('Exited', axis=1)
y = df['Exited']

# Özellik türlerini belirt
categorical_features = ['Geography', 'Gender']
numerical_features = ['CreditScore', 'Age', 'Tenure', 'Balance', 'NumOfProducts', 'EstimatedSalary']

# Ön işleme adımı
preprocessor = ColumnTransformer(
    transformers=[
        ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_features),
        ('num', StandardScaler(), numerical_features)
    ]
)

# Random Forest modeli için pipeline
model = RandomForestClassifier(random_state=42)

pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('classifier', model)
])

# Eğitim/test ayrımı
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# ✅ 1. 5-kat çapraz doğrulama
print("5-Kat Çapraz Doğrulama Sonuçları (Accuracy):")
cv_scores = cross_val_score(pipeline, X_train, y_train, cv=5, scoring='accuracy')
print(f"Her katman için skorlar: {cv_scores}")
print(f"Ortalama doğruluk: {np.mean(cv_scores):.4f}")

# ✅ 2. GridSearchCV ile hiperparametre optimizasyonu
param_grid = {
    'classifier__n_estimators': [50, 100],
    'classifier__max_depth': [5, 10, None],
    'classifier__min_samples_split': [2, 5]
}

grid_search = GridSearchCV(pipeline, param_grid, cv=5, scoring='f1', n_jobs=-1, verbose=1)
grid_search.fit(X_train, y_train)

print(f"\nEn iyi parametreler: {grid_search.best_params_}")

# En iyi model ile tahmin yap
best_model = grid_search.best_estimator_
y_pred = best_model.predict(X_test)

print("\nTest Seti Performansı:")
print(classification_report(y_test, y_pred))

# Modeli kaydet
joblib.dump(best_model, 'churn_model.joblib')
print("\nModel başarıyla 'churn_model.joblib' dosyasına kaydedildi.")