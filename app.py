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

# Display a simple text
st.write('This is a simple text')
st.write('This is another text')

# Create a simple dataframe

df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})

# Display the dataframe
st.write("Here is the dataframe")
st.write(df)

# Create a line chart
chart_datat = pd.DataFrame(np.random.randn(20, 3), columns=['a', 'b', 'c'])
st.line_chart(chart_datat)

