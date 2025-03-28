import streamlit as st
import requests
from datetime import datetime

st.title("TaxiFareModel front")

st.markdown('''
Remember that there are several ways to output content into your web page...

Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the `st.` functions
''')

st.header("Select Ride Parameters")

# 1. Input parameters
pickup_date = st.date_input("Pickup Date", value=datetime.today())
pickup_time = st.time_input("Pickup Time", value=datetime.now().time())
pickup_datetime = f"{pickup_date} {pickup_time}"

pickup_longitude = st.number_input("Pickup Longitude", value=-73.985428)
pickup_latitude = st.number_input("Pickup Latitude", value=40.748817)
dropoff_longitude = st.number_input("Dropoff Longitude", value=-73.985428)
dropoff_latitude = st.number_input("Dropoff Latitude", value=40.748817)
passenger_count = st.number_input("Passenger Count", min_value=1, max_value=10, value=1)

# 2. API parameters dictionary
params = {
    "pickup_datetime": pickup_datetime,
    "pickup_longitude": pickup_longitude,
    "pickup_latitude": pickup_latitude,
    "dropoff_longitude": dropoff_longitude,
    "dropoff_latitude": dropoff_latitude,
    "passenger_count": passenger_count
}

# 3. API call
url = 'https://taxifare.lewagon.ai/predict'
if st.button("Get Fare Prediction"):
    response = requests.get(url, params=params)
    if response.status_code == 200:
        prediction = response.json()["fare"]
        st.success(f"Predicted Fare: ${prediction:.2f}")
    else:
        st.error("Failed to retrieve prediction from API")
