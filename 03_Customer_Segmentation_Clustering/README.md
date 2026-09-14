# 🛍️ E-Commerce Customer Segmentation Engine

🔗 **Live Web App:** [Click here to use the app!](PUT_YOUR_STREAMLIT_LINK_HERE)

### 🎯 Objective
Built an Unsupervised Machine Learning clustering engine to automatically group unlabeled e-commerce customers into distinct behavioral segments for targeted marketing campaigns.

### 🛠️ Tech Stack & Methodology
* **Language & UI:** Python, Streamlit
* **Libraries:** Scikit-Learn, Pandas, NumPy
* **Step 1 (Standardization):** Applied `StandardScaler` to normalize customer metrics (Age, Income, Spending, etc.) to prevent high-variance features from dominating the distance calculations.
* **Step 2 (Dimensionality Reduction):** Applied **PCA (Principal Component Analysis)** to reduce the 5-dimensional dataset down to 2 dimensions for visualization, successfully retaining **74% of the original variance**.
* **Step 3 (Clustering):** Deployed **K-Means Clustering** ($K=4$) to identify hidden customer "tribes" based on physical distance to centroids.

### 📊 Business Impact
The model successfully clustered users into 4 highly actionable marketing segments:
1. **The VIPs** (Target with premium products)
2. **The Bargain Hunters** (Target with discounts)
3. **The Sleeping Giants** (Target with re-engagement emails)
4. **The Window Shoppers** (Target with urgency/flash sales)
This allows the marketing team to optimize ad spend by showing the right products to the right people.
