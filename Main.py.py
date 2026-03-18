
import streamlit as st
import random
import string

st.title("🔐 Password Generator")

# User Inputs
length = st.number_input("Enter password length", min_value=4, value=8)

include_numbers = st.checkbox("Include numbers")
include_symbols = st.checkbox("Include symbols")

# Generate Button
if st.button("Generate Password"):

    characters = string.ascii_letters
    password = []

    # Ensure at least one from selected types
    if include_numbers:
        characters += string.digits
        password.append(random.choice(string.digits))

    if include_symbols:
        characters += string.punctuation
        password.append(random.choice(string.punctuation))

    # Always include at least one letter
    password.append(random.choice(string.ascii_letters))

    # Fill remaining length
    while len(password) < length:
        password.append(random.choice(characters))

    random.shuffle(password)
    password = "".join(password)

    # Display password
    st.subheader("Generated Password:")
    st.code(password)

    # Strength Checker
    has_length = len(password) >= 8
    has_digit = any(char.isdigit() for char in password)
    has_symbol = any(char in string.punctuation for char in password)

    st.subheader("Password Strength:")

    if has_length and has_digit and has_symbol:
        st.success("Strong Password ✅")
    elif has_length and (has_digit or has_symbol):
        st.warning("Medium Password ⚠️")
    else:
        st.error("Weak Password ❌")

    # File Handling (Save password)
    with open("passwords.txt", "a") as file:
        file.write(password + "\n")

    st.info("Password saved to file 📁")
