import streamlit as st
import pickle

# Load model
m = pickle.load(open("m.pkl", "rb"))
cv = pickle.load(open("cv.pkl", "rb"))


st.set_page_config(page_title="Spam Classifier", page_icon="📧", layout="centered")


st.markdown("""
<style>
body {
    background-color: #f4f6f9;
}

.main {
    display: flex;
    justify-content: center;
}

.card {
    background-color: #ffffff;
    padding: 30px;
    border-radius: 15px;
    box-shadow: 0px 4px 20px rgba(0,0,0,0.1);
}

textarea {
    border-radius: 10px !important;
}

div.stButton > button {
    width: 100%;
    background-color: #4CAF50;
    color: white;
    border-radius: 10px;
    height: 50px;
    font-size: 16px;
}

</style>
""", unsafe_allow_html=True)

# Title
st.markdown("<h1 style='text-align:center;'> Spam Classifier</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;'>Detect spam messages </p>", unsafe_allow_html=True)

st.markdown("---")

# Input
message = st.text_area("Enter your message:", height=150)

# Button
if st.button("Check Message"):
    if message:
        vec = cv.transform([message])
        pred = m.predict(vec)

        st.markdown("---")

        if pred[0] == 1:
            st.error("🚨 This is a Spam Message")
        else:
            st.success("✅ This is NOT Spam")