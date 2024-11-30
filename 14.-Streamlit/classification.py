import streamlit as st 
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

@st.cache
def load_data():
    data, target, feature_names, target_names = load_iris(return_X_y=True, return_feature_names=True, return_target_names=True)
    df = pd.DataFrame(data, columns=feature_names)
    df['species'] = target
    return df, target_names

df, target_name = load_data()

print(df.head())
st.write(df.head())
