import streamlit as st
import pickle
import numpy as np
import xgboost

model=pickle.load(open('xgmodel2.pkl','rb'))

st.image("flights.jpg")
st.title("Flight Fare Prediction")
#irline	Source	Destination	Total_Stops	Journey_day	Journey_month	rounded_hours
#for airline
airline_display=('IndiGo', 'Air India', 'Jet Airways', 'SpiceJet',
       'Multiple carriers', 'GoAir', 'Vistara', 'Air Asia',
       'Vistara Premium economy', 'Multiple carriers Premium economy',
       'Trujet')
airline_options=list(range(len(airline_display)))
airline=st.selectbox("Select Airline",airline_options,format_func=lambda x:airline_display[x])

#for source
source_display=('Banglore', 'Kolkata', 'Delhi', 'Chennai', 'Mumbai')
source_options=list(range(len(source_display)))
source=st.selectbox("Select Source",source_options,format_func=lambda x:source_display[x])

#for destination
destination_display=('New Delhi', 'Banglore', 'Cochin', 'Kolkata', 'Delhi', 'Hyderabad')
destination_options=list(range(len(destination_display)))
destination=st.selectbox("Select Destination",destination_options,format_func=lambda x:destination_display[x])

#for total stops
stops_display=('Non-stop', '2 stops', '1 stop', '3 stops', '4 stops')
stops_options=list(range(len(stops_display)))
stops=st.radio("Total Stops",stops_options,format_func=lambda x:stops_display[x])

date=st.number_input("Journey date",min_value=1,max_value=30)
month=st.number_input("Journey month",min_value=1,max_value=12)
hours=st.number_input("No. of hours",min_value=1,max_value=24)

if st.button("Submit"):
       result=model.predict(np.array([[airline,source,destination,stops,date,month,hours]]))[0]
       st.write("The price prediction is " + str(result))