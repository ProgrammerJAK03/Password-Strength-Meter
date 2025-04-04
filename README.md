```markdown
# Password Strength Meter

A web application built using **Streamlit** that allows users to check the strength of their passwords and generate strong random passwords. The app provides a real-time **gauge meter** to visually display the strength of the entered password and gives suggestions for improvement.

---

## Features

- **Password Input**: Users can enter a password, and the app checks its strength.
- **Strength Meter**: Real-time **gauge meter** that shows password strength from 0 to 100.
- **Password Generation**: Generate a random password that meets security criteria.
- **Password History**: View the last 10 generated passwords with timestamps.
- **Password Copy**: Copy passwords to the clipboard with a simple click.
- **Customizable Design**: Attractive and modern UI with **colorful themes**.

---

## Installation

To run the app locally, follow the steps below.

### 1. Set Up Virtual Environment (Optional but Recommended)

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

If `requirements.txt` doesn't exist, you can install the necessary packages manually:

```bash
pip install streamlit plotly pyperclip
```

### 3. Run the App

```bash
streamlit run Password_Strength_Meter.py
```

The app will open in your browser at `http://localhost:8501`.

---

## App Walkthrough

### 1. Password Input
- Enter your password in the input field.
- The app will check the password's strength in real-time.
  
### 2. Password Strength Meter
- The app displays a **gauge meter** that shows the strength of the password.
- The meter changes color depending on the strength (Red for weak, Orange for moderate, Green for strong).

### 3. Password Generation
- You can click on the **"Generate Password"** button to get a random strong password.
- The password is added to the password history.

### 4. Password History
- The **last 10 passwords** generated are stored along with the **timestamp** and can be viewed by clicking the **"Show Preview Passwords"** checkbox.
- You can also **copy** any password from the history by clicking the **copy button**.

---

## Tech Stack

- **Streamlit**: A powerful framework for creating interactive web apps in Python.
- **Plotly**: For creating the **gauge meter** to display password strength.
- **Pyperclip**: For clipboard operations (copying the password).

