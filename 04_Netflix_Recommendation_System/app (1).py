import streamlit as st
import pandas as pd
import time

# 1. Premium Page Config (Wide Layout)
st.set_page_config(page_title="StreamFlix AI", page_icon="🍿", layout="wide")

# 2. Inject Custom CSS (The Netflix Dark Theme & Movie Cards)
st.markdown("""
<style>
    /* Dark background */
    .stApp {
        background-color: #0E0E0E;
        color: white;
    }
    /* Sleek Movie Card Design */
    .movie-card {
        background-color: #1A1A1A;
        padding: 30px;
        border-radius: 15px;
        text-align: center;
        box-shadow: 0 10px 20px rgba(229, 9, 20, 0.2);
        border: 1px solid #333;
        transition: transform 0.3s;
    }
    .movie-card:hover {
        transform: scale(1.05);
        border: 1px solid #E50914; /* Netflix Red Border on Hover */
    }
    .movie-title {
        color: #E50914;
        font-size: 26px;
        font-weight: 900;
        margin-bottom: 10px;
    }
    .movie-score {
        font-size: 18px;
        color: #A9A9A9;
    }
</style>
""", unsafe_allow_html=True)

# 3. Load the Brain (Our Predicted Matrix)
df_preds = pd.read_csv('04_Netflix_Recommendation_System/movie_predictions.csv', index_col=0)

# 4. App Header
st.markdown("<h1 style='text-align: center; color: #E50914; font-size: 50px;'>STREAMFLIX AI</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: white;'>Your personalized SVD Recommendation Engine</h4>", unsafe_allow_html=True)
st.divider()

# 5. The Sidebar (User Selection)
st.sidebar.image("https://upload.wikimedia.org/wikipedia/commons/0/08/Netflix_2015_logo.svg", width=150)
st.sidebar.title("👤 Profile Selection")
user_list = df_preds.index.tolist()
selected_user = st.sidebar.selectbox("Who is watching?", user_list)

# 6. The "Recommend" Button
if st.sidebar.button("🎬 Generate Recommendations", use_container_width=True):
    
    # Dramatic loading effect!
    with st.spinner('Analyzing your watch history via Matrix Factorization...'):
        time.sleep(1.5) # Pauses for 1.5 seconds to feel like heavy AI processing!
    
    st.success(f"Top Matches for **{selected_user}**")
    
    # Get predictions, sort them, pick top 3
    user_ratings = df_preds.loc[selected_user]
    top_3 = user_ratings.sort_values(ascending=False).head(3)
    
    # 7. DISPLAY AS 3 COLUMNS (Movie Cards)
    col1, col2, col3 = st.columns(3)
    cols = [col1, col2, col3]
    
    for i, (movie, score) in enumerate(top_3.items()):
        # Clip score between 1.0 and 5.0
        display_score = max(1.0, min(5.0, score))
        
        # Build the HTML for the card
        card_html = f"""
        <div class="movie-card">
            <div class="movie-title">{movie}</div>
            <div class="movie-score">⭐ {display_score:.1f} / 5.0 Match</div>
        </div>
        """
        # Put the card inside the column
        with cols[i]:
            st.markdown(card_html, unsafe_allow_html=True)
            
    st.balloons()
