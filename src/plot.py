import streamlit as st
import pandas as pd
import plotly.express as px

def display_real_time_vaccancy(data):
    """Displays real-time car park occupancy information"""
    st.header(f"{data['facility_name']}")
    st.write(f"Data last updated at {data['MessageDate']}" )
    col_1, col_2 = st.columns(2)
    with col_1:
        st.metric("Total Spaces", data["spots"])
    with col_2:
        st.metric("Vaccancy", int(data["spots"]) - int(data["occupancy"]["total"]))

def plot_historical_data(data):
    """Plots historical car park occupancy data using Plotly"""
    timestamps = [pd.to_datetime(x["MessageDate"]) for x in data]
    occupancies = [x["occupancy"]["total"] for x in data]

    fig = px.line(x=timestamps, y=occupancies)
    fig.add_shape(type="line",
                  x0=timestamps[0],
                  y0=data[0]["spots"],
                  x1=timestamps[-1],
                  y1=data[0]["spots"],
                  line=dict(color="red", width=2, dash="dash"))
    fig.update_layout(
        title=data[0]["facility_name"],
        xaxis_title="Time",
        yaxis_title="Occupied Spaces"
    )
    st.plotly_chart(fig) 