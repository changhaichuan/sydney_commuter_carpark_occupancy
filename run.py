import os 
import streamlit as st
from src.data_ingestion import *
from src.plot import *

API_KEY = os.environ.get("API_KEY")

#### Dashboard Starts Here ####
st.title("Sydney Commuter Car Park Real-time Occupancy")

# Ask user to select car park
carpark_dict = get_carpark_dict(api_key=API_KEY)
carpark_dict = {k: v for k, v in carpark_dict.items() if not 'historical' in v}
carpark_dict = dict(sorted(carpark_dict.items(), key=lambda x: x[1], reverse=True))
facility_name = st.selectbox("Select Car Park", list(carpark_dict.values()))
facility_id = [k for k, v in carpark_dict.items() if v == facility_name][0]

# Display real-time vaccancy
real_time_data = get_real_time_carpark_data(api_key=API_KEY, facility_id=facility_id)
display_real_time_vaccancy(real_time_data)

# Ask user to select date to see historical data
event_date = st.date_input("Select date to see historical data", value=None)

# Display historical data if date is selected
if event_date:
        history_data = get_historical_carpark_data(api_key=API_KEY, facility_id=facility_id, event_date=event_date)
        plot_historical_data(history_data)
