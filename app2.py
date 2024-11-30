import streamlit as st 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots


# tile of the application

st.title('Hello Streamlit')

name = st.text_input("Enter your name: ")

age = st.slider("Select your age:", 1, 100,25)

st.write(f"You age is {age}")

options = ['Python', 'Java', 'C++', 'Ruby', 'Go']
choice = st.selectbox('Choose a programming language', options)
st.write(f'You selected: {choice}')

if name:
    st.write(f"Your name is {name}")

uploaded_file = st.file_uploader("Choose a CSV file:, type='CSV'")

if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    st.write(data)