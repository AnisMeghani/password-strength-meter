import re
import streamlit as st

def check_password_strength(password):
    criteria = {
        "At least 8 characters long": len(password) >= 8,
        "Includes uppercase and lowercase letters": any(char.islower() for char in password) and any(char.isupper() for char in password),
        "Contains at least one digit (0-9)": any(char.isdigit() for char in password),
        "Has at least one special character (!@#$%^&*)": re.search(r"[!@#$%^&*]", password) is not None
    }
    
    score = sum(criteria.values())
    
    # Strength evaluation
    if score == 4:
        strength = "Strong"
        message = "✅ Your password is strong!"
    elif score >= 3:
        strength = "Moderate"
        message = "⚠️ Your password is moderate. Consider improving it."
    else:
        strength = "Weak"
        message = "❌ Your password is weak! Try meeting more criteria."
    
    return strength, message, criteria

# Streamlit UI
st.title('🔐 Password Strength Meter By "*Muhammad Anis Meghani*"')

password = st.text_input("Enter your password:", type="password", key="password_input")

st.write("### Password Requirements:")

if "password_input" in st.session_state:
    current_password = st.session_state.password_input
    strength, message, criteria = check_password_strength(current_password)
    
    st.subheader(f"Strength: {strength}")
    st.write(message)
    
    for requirement, met in criteria.items():
        color = "green" if met else "red"
        st.markdown(f"<span style='color:{color}; font-weight:bold;'>{'✅' if met else '❌'} {requirement}</span>", unsafe_allow_html=True)