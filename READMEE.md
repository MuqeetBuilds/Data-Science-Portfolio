# ✈️ Flight Price Prediction Algorithm

### 🎯 Objective
Built a Machine Learning regression model to predict the exact ticket price of domestic flights based on booking timing, airline, and route. 

### 🛠️ Tech Stack & Methodology
* **Language:** Python
* **Libraries:** Pandas, NumPy, Scikit-Learn
* **Feature Engineering:** Applied One-Hot Encoding to convert categorical text data (Airlines, Cities) into mathematical vectors.
* **Model Used:** Random Forest Regressor (Ensemble Bootstrap Aggregation with 100 decision trees).

### 📊 Results & Evaluation
The model was evaluated against an unseen testing set (20% of total data) to ensure no overfitting occurred. 
* **R-Squared ($R^2$) Score:** `0.9512` (The model successfully explains 95.1% of the variance in ticket pricing).
* **Mean Absolute Error (MAE):** `₹521.97` (Predictions are accurate within ~500 INR of the true real-time price).

### 💡 Business Impact
This model can be deployed on a travel aggregator application (like Expedia or MakeMyTrip) to notify users if the current flight price is artificially inflated or represents a good deal, saving consumers money.
