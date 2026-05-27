import streamlit as st
import pickle
import numpy as np
from streamlit_option_menu import option_menu

# Page Configuration
st.set_page_config(
    page_title="House Price Prediction",
    page_icon="🏠",
    layout="wide"
)

# Load Model
model = pickle.load(open("model.pkl", "rb"))
# Custom CSS Styling
st.markdown(
    """
    <style>

    .main {
        background-color: #f5f7fa;
    }

    .title {
        font-size: 45px;
        font-weight: bold;
        color: #1f4e79;
        text-align: center;
        margin-bottom: 10px;
    }
.subtitle {
        font-size: 20px;
        color: gray;
        text-align: center;
        margin-bottom: 40px;
    }

    .stButton>button {
        width: 100%;
        background-color: #1f77b4;
        color: white;
        font-size: 18px;
        border-radius: 10px;
        height: 3em;
        border: none;
    }
    
    .stButton>button:hover {
        background-color: #135e96;
        color: white;
    }

    .prediction-box {
        padding: 20px;
        border-radius: 10px;
        background-color: #d4edda;
        color: #155724;
        font-size: 28px;
        text-align: center;
        font-weight: bold;
        margin-top: 20px;
    }
</style>
    """,
    unsafe_allow_html=True
)

# Sidebar Menu
with st.sidebar:
    selected = option_menu(
        menu_title="Main Menu",
        options=["Home", "Prediction", "About"],
        icons=["house", "graph-up", "info-circle"],
        default_index=0,
    )

# Home Page
if selected == "Home":

    st.markdown('<div class="title">🏠 House Price Prediction System</div>', unsafe_allow_html=True)

    st.markdown(
        '<div class="subtitle">Machine Learning Project using Linear Regression</div>',
        unsafe_allow_html=True
    )
    col1, col2 = st.columns(2)

    with col1:
        st.image(
            "https://images.unsplash.com/photo-1568605114967-8130f3a36994",
            use_container_width=True
        )

    with col2:
        st.write("### Project Overview")

        st.write(
            """
            This project predicts house prices using Machine Learning.

            ### Features Used:
            - Area
            - Bedrooms
            - Bathrooms
            - Stories
            - Parking
        ### Technologies Used:
                    - Python
                    - Streamlit
                    - Scikit-learn
                    - NumPy
                    - Pandas
                    """
        )
# Prediction Page
elif selected == "Prediction":

    st.markdown('<div class="title">📈 Predict House Price</div>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        area = st.number_input("Enter Area (sq ft)", min_value=0)

        bedrooms = st.number_input("Enter Number of Bedrooms", min_value=0)

        bathrooms = st.number_input("Enter Number of Bathrooms", min_value=0)

    with col2:
        stories = st.number_input("Enter Number of Stories", min_value=0)

        parking = st.number_input("Enter Parking Spaces", min_value=0)

    st.write("")

    if st.button("Predict House Price"):
        features = np.array([[area, bedrooms, bathrooms, stories, parking]])

        prediction = model.predict(features)

        st.markdown(
            f'<div class="prediction-box">Predicted Price: ₹ {prediction[0]:,.2f}</div>',
            unsafe_allow_html=True
        )
elif selected == "About":

    st.markdown('<div class="title">ℹ About Project</div>', unsafe_allow_html=True)

    st.write(
        """
        ## House Price Prediction Project

        This Machine Learning project predicts house prices based on various features.

        ### Algorithm Used
        - Linear Regression

        ### Project Workflow
        1. Data Collection
        2. Data Preprocessing
        3. Model Training
        4. Prediction
        5. Deployment using Streamlit
        
    ### Developed Using
            - Python
            - Streamlit
            - Scikit-learn
            - NumPy
            - Pandas

            ### Developed By
            Student Machine Learning Project
            """
    )
