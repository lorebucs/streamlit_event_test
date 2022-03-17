from streamlit_plotly_events import plotly_events
import plotly.figure_factory as ff
import plotly.graph_objs as go
import streamlit as st
import pandas as pd
import numpy as np
import time


csv_path = "./data/machine_0.csv"

if "data" not in st.session_state:
    loading_status = st.text("Loading data...")
    start_time = time.time()
    st.session_state["data"] = pd.read_csv(csv_path)
    loading_status.text(f"Loaded in {time.time() - start_time} s.")


# Previous attempt using chaching (replaced with session_state)
# @st.cache(show_spinner=False)
# def load_data(csv_path):
#     data = pd.read_csv(csv_path)
#     return data
#df = load_data("./data/machine_0.csv")


signal = list(st.session_state["data"]["signal_0"].values)

window_size = 200
half_win_size = window_size // 2
center = st.slider(
     'Window center',
     half_win_size, len(signal)-half_win_size, half_win_size)
st.write('Window:', center-half_win_size, center+half_win_size)


fig = go.Figure()
fig.add_trace(go.Scatter(x=list(np.arange(center-half_win_size, center+half_win_size)),
                         y=signal[center-half_win_size : center+half_win_size], 
                         mode='lines+markers')
)
fig.update_layout(modebar_remove=['zoom', 'pan'])
fig.update_layout(dragmode='select', uirevision='foo')
fig.update_xaxes(rangeslider_visible=True)

selected_points = plotly_events(fig, select_event=True)
st.write(selected_points)


# Add hardcoded histogram (without session_state)
x1 = [0,1,2,1,2,3,4,5,6,7,8,7,6,5,4,3,2,3,2,1,2,1]
x2 = [0,1,0,1,0,1,2,0,1,2,1,3,4,3,4,3,4,5,4,5,6,5,6,7,6,7,8,9]
x3 = [9,9,8,8,7,7,6,5,5,4,3,3,3,2,2,1,1]

hist_data = [x1, x2, x3]
group_labels = ['Group 1', 'Group 2', 'Group 3']
fig_0 = ff.create_distplot(
    hist_data, group_labels, bin_size=[.1, .25, .5])
st.plotly_chart(fig_0, use_container_width=True)
