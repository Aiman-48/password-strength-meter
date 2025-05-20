import streamlit as st

def check_password(password):
    score = 0
    tips = [] #list

    if len(password) >= 8:
        score += 1
    else:
        tips.append("🔴 use at least 8 characters")
    if any(c.isupper() for c in password): #c means character c.uppercase hai ya nhi 
        score += 1
    else:
        tips.append("🟠 include upper letter")
    if any(c.islower() for c in password): #c means character c.lowercase hai ya nhi 
        score += 1
    else:
        tips.append("🟠 include lower letter")

    if any(c.isdigit() for c in password): #c means character c.uppercase hai ya nhi 
        score += 1
    else:
        tips.append("🟡 add a number digits (0-9)") 
    if any(c in "@#$%^&*!" for c in password):
        score += 1
    else:
        tips.append("🟡 use a special charachter (@#$%^&*!) ")      

    return score, tips    

def main():
    st.title("password strength meter 🔐")
    password = st.text_input("Enter password 🔑", type="password")

    if password:
        score, tips = check_password(password)

        if score == 5:
            st.success("✅strong password secure and safe")
        elif score == 3 or score == 4:
            st.warning("⚠️moderate password! improve it")

        else:
            st.error("❌weak password ! follow these steps:")   

        for tip in tips:
            st.write(tip)     



main()              
