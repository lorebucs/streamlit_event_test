from streamlit_plotly_events import plotly_events
import streamlit as st

import plotly.graph_objs as go

import pandas as pd
import numpy as np
import time


@st.cache(show_spinner=False)
def load_data(csv_path):
    data = pd.read_csv(csv_path)
    return data

data_load_state = st.text('Loading data...')
start_time = time.time()
df = load_data("./data/machine_0.csv")
data_load_state.text(f"Loaded in {time.time() - start_time} s.")


signal = list(df["signal_0"].values)

window_size = 200
center = st.slider(
     'Window center',
     100, 2900, 100)
st.write('Window:', center-100, center+100)


fig = go.Figure()
fig.add_trace(go.Scatter(x=list(np.arange(center-100, center+100, 1)),
                         y=signal[center-100:center+100], 
                         mode='lines+markers')
)
fig.update_layout(modebar_remove=['zoom', 'pan'])
fig.update_layout(dragmode='select', uirevision='foo')
fig.update_xaxes(rangeslider_visible=True)

selected_points = plotly_events(fig, select_event=True)
st.write(selected_points)
