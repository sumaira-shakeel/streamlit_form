import streamlit as st

# Custom CSS styling
st.markdown("""
    <style>
        body {
            background-color: #f7f9fc;
        }
        .stTextInput > div > div > input {
            background-color: #ffffff;
            padding: 10px;
            border-radius: 8px;
            border: 1px solid #ccc;
        }
        .stSelectbox > div > div {
            background-color: #ffffff;
            border-radius: 8px;
            padding: 5px;
        }
        .stButton button {
            background-color: #4CAF50;
            color: white;
            font-size: 16px;
            padding: 10px 24px;
            border: none;
            border-radius: 8px;
            transition: background-color 0.3s ease;
        }
        .stButton button:hover {
            background-color: #45a049;
        }
        .output-box {
            background-color: #e0f7fa;
            padding: 20px;
            border-radius: 15px;
            margin-top: 20px;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
        }
    </style>
""", unsafe_allow_html=True)

# Form inputs
st.markdown("<h2 style='color:#2e86c1;'> 📄 Student Information Form</h2>", unsafe_allow_html=True)
name = st.text_input("Enter your name: ")
Fname = st.text_input("Enter your Father name: ")
add = st.text_input("Enter your address:")
classdata = st.selectbox("Enter your class", ['1st', '2nd', '3rd', '4th'])

# Submit button
button = st.button("Submit")

# Output display
if button:
    st.markdown(f"""
        <div class="output-box">
            <h3 style="color:#00695c;"> ℹ️ Submission Details:</h3>
            <p><strong>Name:</strong> {name}</p>
            <p><strong>Class:</strong> {classdata}</p>
            <p><strong>Father Name:</strong> {Fname}</p>
            <p><strong>Address:</strong> {add}</p>
        </div>
    """, unsafe_allow_html=True)
