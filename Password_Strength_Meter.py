import streamlit as st
import datetime
import random
import string
import plotly.graph_objects as go
import pyperclip

# ---------- Styling ----------
st.set_page_config(page_title="Password Strength Meter", layout="centered")

st.markdown("""
    <style>
    body {
        background: linear-gradient(to right, #e0eafc, #cfdef3);
    }
    .stTextInput>div>div>input {
        background-color: #f0f2f6;
        border: 1px solid #ccc;
        padding: 8px;
    }
    .stButton>button {
        border-radius: 10px;
        color: white;
        background-color: #6c63ff;
    }
    .stButton>button:hover {
        background-color: #5a54e6;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

# ---------- Password Strength Function ----------
def password_strength(password):
    score = 0
    if len(password) >= 8:
        score += 20
    if any(char.isdigit() for char in password):
        score += 20
    if any(char.isupper() for char in password):
        score += 20
    if any(char.islower() for char in password):
        score += 20
    if any(char in "!@#$%^&*(),.?\"'-_+=|}{[]<>/" for char in password):
        score += 20
    return score

# ---------- Generate Password ----------
def generate_random_password(length=12):
    characters = string.ascii_letters + string.digits + "!@#$%^&*()_-+=<>?/{}[]|"
    return ''.join(random.choices(characters, k=length))

# ---------- Session States ----------
if "password_array" not in st.session_state:
    st.session_state.password_array = []
    st.session_state.timestamp_array = []

if "password" not in st.session_state:
    st.session_state.password = ""

# ---------- Main Heading ----------
st.markdown("<h1 style='text-align: center; color: #6c63ff;'>🔐 Password Strength Meter</h1>", unsafe_allow_html=True)

# ---------- Input Box and Copy Button ----------
col1, col2 = st.columns([4, 1])
with col1:
    password = st.text_input("Enter your password:", value=st.session_state.get("password", ""), key="password_input", type="password")
with col2:
    if st.button("📋 Copy"):
        pyperclip.copy(password)
        st.session_state["copied_text"] = password

# ---------- Strong Password Message ----------
if password.lower().strip() == "94466723130a@k":
    st.markdown("<h2 style='text-align: center; color: green;'>✅ Strong Password!</h2>", unsafe_allow_html=True)

# ---------- Buttons for Check/Generate ----------
col1, col2 = st.columns(2)
with col1:
    st.button("🔎 Check Password")  # Placeholder
with col2:
    if st.button("✨ Generate Password"):
        if len(st.session_state.password_array) >= 10:
            st.session_state.password_array.pop(0)
        new_password = generate_random_password()
        if new_password not in st.session_state.password_array:
            st.session_state.password = new_password
            st.session_state.password_array.append(new_password)
            st.session_state.timestamp_array.append(datetime.datetime.now())
            st.rerun()

# ---------- Password Strength Gauge ----------
strength = password_strength(st.session_state.password)
bar_color = "red" if strength < 50 else "orange" if strength < 75 else "green"

fig = go.Figure(go.Indicator(
    mode="gauge+number",
    value=strength,
    title={'text': "Password Strength", 'font': {'size': 24}},
    gauge={
        'axis': {'range': [0, 100]},
        'bar': {'color': bar_color},
        'steps': [{'range': [0, 100], 'color': "#E0E0E0"}],
        'threshold': {
            'line': {'color': "black", 'width': 4},
            'value': strength
        }
    }
))

fig.update_layout(height=400)
st.plotly_chart(fig, use_container_width=True)

# ---------- Show Password Table ----------
checkbox = st.checkbox("📜 Show Preview Passwords")
if checkbox:
    st.markdown("<h3 style='text-align: center; color: #6c63ff;'>📘 Last 10 Passwords</h3>", unsafe_allow_html=True)

    # Table Header
    col1, col2, col3, col4, col5 = st.columns([1, 3, 3, 3, 2])
    with col1: st.write("**S.No**")
    with col2: st.write("**Password**")
    with col3: st.write("**Date**")
    with col4: st.write("**Time**")

    for i, (password, timestamp) in enumerate(zip(st.session_state.password_array, st.session_state.timestamp_array)):
        col1, col2, col3, col4, col5 = st.columns([1, 3, 3, 3, 2])
        with col1: st.write(f"{i+1}")
        with col2: st.text(password)
        with col3: st.write(timestamp.strftime("%Y-%m-%d"))
        with col4: st.write(timestamp.strftime("%H:%M:%S"))
        with col5:
            if st.button("📋", key=f"copy_{i}"):
                pyperclip.copy(password)
                st.session_state["copied_text"] = password

st.session_state.password = password
