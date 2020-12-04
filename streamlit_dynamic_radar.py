import matplotlib.pyplot as plt
import streamlit as st
import time
import random
import plotly.express as px
import pandas as pd

placeholder = st.empty()
start_button = st.empty()

def animate():  
    df = pd.DataFrame(dict(
    r=[random.randint(0,22),
       random.randint(0,22),
       random.randint(0,22),
       random.randint(0,22),
       random.randint(0,22)],
    theta=['processing cost','mechanical properties','chemical stability',
           'thermal stability', 'device integration']))
    fig = px.line_polar(df, r='r', theta='theta', line_close=True)
    placeholder.write(fig)
    
if start_button.button('Start',key='start'):
    start_button.empty()
    if st.button('Stop',key='stop'):
        pass
    while True:
        animate()
        time.sleep(0.5)
