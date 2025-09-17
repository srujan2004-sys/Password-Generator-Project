import streamlit as st
import string
import secrets


def generate_password(length=12, use_letters=True, use_digits=True, use_symbols=True):
    """Generate a secure random password."""
    characters = ""
    if use_letters:
        characters += string.ascii_letters
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        return None

    return "".join(secrets.choice(characters) for _ in range(length))


def check_strength(password: str) -> str:
    """Check basic strength of the password."""
    if not password:
        return "No password generated"

    length = len(password)
    categories = sum([
        any(c.islower() for c in password),
        any(c.isupper() for c in password),
        any(c.isdigit() for c in password),
        any(c in string.punctuation for c in password)
    ])

    if length >= 12 and categories == 4:
        return "Strong"
    elif length >= 8 and categories >= 3:
        return "Medium"
    else:
        return "Weak"


# Streamlit App
st.set_page_config(page_title="Password Generator", layout="centered")

st.title("Password Generator")
st.write("Generate strong, random passwords with customizable options.")

# Sidebar options
st.sidebar.header("Settings")
length = st.sidebar.slider("Password Length", min_value=4, max_value=32, value=12, step=1)
use_letters = st.sidebar.checkbox("Include Letters (a-z, A-Z)", value=True)
use_digits = st.sidebar.checkbox("Include Numbers (0-9)", value=True)
use_symbols = st.sidebar.checkbox("Include Symbols (!@#$...)", value=True)

# Generate button
if st.button("Generate Password"):
    password = generate_password(length, use_letters, use_digits, use_symbols)
    if password:
        st.success(f"Your Password: {password}")
        st.info(f"Strength: {check_strength(password)}")
    else:
        st.error("Please select at least one character set.")
