import re
import streamlit as st

def check_password_strength(password):
    score = 0
    feedback = []
    
    # Length check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Make the password at least 8 characters long.")
    
    # Upper and lower case check
    if any(char.islower() for char in password) and any(char.isupper() for char in password):
        score += 1
    else:
        feedback.append("Include both uppercase and lowercase letters.")
    
    # Digit check
    if any(char.isdigit() for char in password):
        score += 1
    else:
        feedback.append("Add at least one digit (0-9).")
    
    # Special character check
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("Use at least one special character (!@#$%^&*).")
    
    # Strength evaluation
    if score == 4:
        return "Strong", "✅ Your password is strong!"
    elif score >= 3:
        return "Moderate", "⚠️ Your password is moderate. Consider improving it."
    else:
        return "Weak", "❌ Your password is weak! " + " ".join(feedback)

# Streamlit UI
st.title('🔐 Password Strength Meter By "*Muhammad Anis Meghani*"')

password = st.text_input("Enter your password:", type="password")

if password:
    strength, message = check_password_strength(password)
    st.subheader(f"Strength: {strength}")
    st.write(message)
