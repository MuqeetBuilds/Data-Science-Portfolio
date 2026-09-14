# 🍿 StreamFlix AI: Recommendation Engine

🔗 **Live Web App:** [Click here to get your movie recommendations!](PUT_YOUR_STREAMLIT_LINK_HERE)

### 🎯 Objective
Built a Netflix-style recommendation engine that predicts personalized movie ratings for users based on sparse viewing history. 

### 🛠️ Tech Stack & Methodology
* **Language & UI:** Python, Streamlit (with Custom CSS Injection)
* **Libraries:** Scikit-Learn (TruncatedSVD), Pandas, NumPy
* **The Problem:** Real-world recommendation matrices suffer from extreme sparsity (the "Cold Start Problem"), meaning 99% of the user-movie grid is filled with `NaN`s (unknowns).
* **The Math:** Applied **Singular Value Decomposition (SVD)** to factorize the sparse matrix into lower-dimensional hidden "Vibes" (e.g., Action, Romance). The model then performed an inverse transformation to mathematically fill in the blanks, predicting exact 1-to-5 star ratings for unwatched movies.

### 💻 UI / UX Design
The Streamlit front-end was upgraded using custom HTML/CSS to simulate a premium streaming platform. It features a dark-mode theme, interactive hover-zoom movie cards, and asynchronous loading spinners to enhance user experience.

### 📊 Business Impact
Recommendation engines are the core of platforms like Netflix, Amazon, and Spotify. By serving highly accurate, personalized content, this algorithm directly increases user retention, watch time, and subscription loyalty.
