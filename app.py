import streamlit as st

st.set_page_config(
    page_title="Meenal | Data Science Portfolio",
    page_icon="📊",
    layout="wide"
)

# ---- HEADER ----
st.title("👋 Hi, I'm Meenal")
st.subheader("Data Science | Machine Learning | Healthcare AI")

st.write("""
Integrated MSc Data Science student with hands-on experience in machine learning,
deep learning, and healthcare AI. Interested in ML internships and research roles.
""")

st.divider()

# ---- PROJECTS ----
st.header("🚀 Projects")

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("🩺 Retinal Disease Diagnosis")
    st.write("""
    Multi-modal deep learning system using fundus images,
    OCT scans, and clinical data with explainability.
    """)
    st.markdown(
        "[🔗 GitHub Repo](https://github.com/YOUR-USERNAME/multi-modal-retinal-diagnosis)"
    )

with col2:
    st.subheader("🧠 Brain Tumor Detection")
    st.write("""
    CNN-based classification of MRI brain scans into
    tumor and non-tumor categories.
    """)
    st.markdown(
        "[🔗 GitHub Repo](https://github.com/YOUR-USERNAME/brain-tumor-detection-cnn)"
    )

with col3:
    st.subheader("🏏 IPL Match Outcome Prediction")
    st.write("""
    Machine learning model predicting IPL match outcomes
    using historical match data and feature engineering.
    """)
    st.markdown(
        "[🔗 GitHub Repo](https://github.com/YOUR-USERNAME/ipl-match-outcome-prediction)"
    )

st.divider()

# ---- SKILLS ----
st.header("🛠 Skills")
st.write("""
- Python  
- Machine Learning  
- Deep Learning  
- Computer Vision  
- Healthcare AI  
- Pandas, NumPy, Scikit-learn  
""")

st.divider()

# ---- CONTACT ----
st.header("📫 Contact")
st.write("📧 Email: meenalpriyadharshini7@gmail.com")
st.write("💻 GitHub: https://github.com/YOUR-USERNAME")
st.write("🔗 LinkedIn: https://www.linkedin.com/in/meenal-priyadharshni-84b740351")
