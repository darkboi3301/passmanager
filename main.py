#basic streamlit app implement login and logout
import streamlit as st
import pandas as pd
import numpy as np
import time
import os
import random
import string
import re
from password_strength import PasswordStats

st.set_page_config(page_title="password manager", page_icon=":smiley:", layout="centered", initial_sidebar_state="expanded")

login_status = False

def checkpass(username, password):
    if username == "admin" and password == "admin":
        return True
    else:
        return False
    
def GetPassStrength(password):

    weak = 'weak'
    med = 'medium'
    strong = 'strong'

    if len(password) >12:
        st.success('password is greater than 12 characters which is enchancing your security')

    elif len(password) <6:
        st.warning('password is too short It must be minimum 6 characters')

    elif len(password) >=6:
        if password.lower()== password or password.upper()==password or password.isalnum()==password:
            st.write('password is', weak)
        elif password.lower()== password and password.upper()==password or password.isalnum()==password:
            st.write('password is', med)
        else:
            password.lower()== password and password.upper()==password and password.isalnum()==password
            st.write('password is', strong)

if login_status == False:
    st.title("Password Manager")
    st.header("Login")
    st.subheader("Enter your credentials")
    username = st.text_input("Username")
    password = st.text_input("Password", type='password')
    if checkpass(username, password):
        login_status = True
        st.success("Logged in as {}".format(username))
    else:
        st.warning("Wrong username/password")
    
    if login_status == True:
        menu_option = st.sidebar.selectbox("Menu", ["Password Generator", "Password Quality Checker", "Password Manager"])

        if menu_option == "Password Generator":
            st.subheader("Password Generator")
            st.write("This is the password generator")
            # generate password with lenght as user input using all pritable characters
            passlen = st.slider("Password Length", 5, 25, 10)
            password = ''.join(random.choices(string.printable, k=passlen))
            st.write("Your password is: ", password)

        elif menu_option == "Password Quality Checker":
            st.subheader("Password Quality Checker")
            st.write("This is the password quality checker")
            # check password quality use complex methods
            password = st.text_input("Enter your password", type='password')
            GetPassStrength(password)

            

