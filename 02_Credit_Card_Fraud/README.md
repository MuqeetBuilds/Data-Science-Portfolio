# 🕵️‍♂️ Credit Card Fraud Detection AI

### 🎯 Objective
Built a Machine Learning classification model and interactive web application to detect fraudulent credit card transactions in real-time.

### 🛠️ Tech Stack & Methodology
* **Language & UI:** Python, Streamlit
* **Libraries:** Scikit-Learn, XGBoost, Imbalanced-Learn (SMOTE)
* **Data Engineering:** Solved severe class imbalance (99.9% Safe vs 0.1% Fraud) by applying **SMOTE** (Synthetic Minority Over-sampling Technique) to generate synthetic fraud data for model training.
* **Model Selection:** Conducted a cage-match evaluation between Logistic Regression, Support Vector Machines (SVM), and XGBoost. 

### 📊 Results & Evaluation
Traditional accuracy metrics are invalid for imbalanced data, so the models were evaluated strictly using a **Confusion Matrix** (Focusing on True Positives and False Negatives).
* **Winning Model:** `XGBoost Classifier`
* The model successfully identified complex fraud patterns while minimizing the false blocking of innocent customers.

### 🚀 Deployment
The finalized XGBoost model was serialized using `joblib` and deployed as an interactive front-end web application using **Streamlit Community Cloud**. Users can adjust transaction parameters and receive real-time fraud probability scores.
