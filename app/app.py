import streamlit as st
import boto3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta
import plotly.express as px
import plotly.graph_objects as go
from PIL import Image
import numpy as np
from streamlit_option_menu import option_menu
import uuid
import json
from  dashboard import  show_dashboard as display
from growth import manage_child_profile
import milestone 
import doctor_portal
from show_analytics import analytics
from home import Home_Page
from appointments import book1 
import Symptoms



# Configure page settings
st.set_page_config(page_title="KidsCare Pro", page_icon="👶", layout="wide")

# Custom CSS for better styling
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .stButton>button {
        width: 100%;
        border-radius: 5px;
        height: 3em;
        background-color: #ff6b6b;
        color: white;
    }
    .stats-card {
        padding: 1rem;
        border-radius: 0.5rem;
        background-color: #f8f9fa;
        box-shadow: 0 0.15rem 1.75rem 0 rgba(58, 59, 69, 0.15);
        margin: 1rem 0;
    }
    </style>
""", unsafe_allow_html=True)

def login_page():
    st.sidebar.title("Login")
    username = st.sidebar.text_input("Username")
    password = st.sidebar.text_input("Password", type="password")
    user_type = st.sidebar.selectbox("Login as", ["Parent", "Doctor"])
    
    if st.sidebar.button("Login"):
        if username and password:  # Add proper authentication logic
            st.session_state['logged_in'] = True
            st.session_state['username'] = username
            st.session_state['user_type'] = user_type
            return True
    return False
    
  

# Main Navigation
def main_navigation():
    with st.sidebar:
        selected = option_menu(
            menu_title="Main Menu",
            options=["Home_Page","Health-predictor","book_appointment","Dashboard", "Child Profile", "Milestones", "Analytics", "Doctor's Portal"],
            icons=["house", "person", "heart", "graph-up", "trophy", "hospital"],
            menu_icon="cast",
            default_index=0,
        )
    return selected

# Dashboard
def show_dashboard1(username):
   display(username)

# Child Profile Management
def manage_child_profile1():
    manage_child_profile()
    

# Analytics Dashboard
def show_analytics():
    analytics()


# Milestones Tracking
def track_milestones():
    milestone.milestone_tracker()

# Doctor's Portal
def doctors_portal1():
    doctor_portal.doctor()

def book():
    book1()
   

def main():
    if 'logged_in' not in st.session_state:
        st.session_state['logged_in'] = False
        st.session_state['username'] = None
        st.session_state['user_type'] = None

    if not st.session_state['logged_in']:
        Home_Page()
        if st.button("Login"):  # Temporary login button for testing
            st.session_state['logged_in'] = True
            st.session_state['username'] = "Test User"  # Replace with actual username from login logic
            st.experimental_rerun()
    else:
        selected = main_navigation()

        if selected == "Home_Page":
            Home_Page()
        elif selected == "Dashboard":
            show_dashboard1(st.session_state['username'])
        elif selected == "Health-predictor":
            Symptoms.disp()
        elif selected == "book_appointment":
            book()
        elif selected == "Child Profile":
            manage_child_profile1()
        elif selected == "Analytics":
            show_analytics()
        elif selected == "Milestones":
            track_milestones()
        elif selected == "Doctor's Portal":
            doctors_portal1()

        # Logout button in sidebar
        if st.sidebar.button("Logout"):
            st.session_state['logged_in'] = False
            st.session_state['username'] = None
            st.session_state['user_type'] = None
            st.experimental_rerun()
# Run the application
if __name__ == "__main__":
    main()
