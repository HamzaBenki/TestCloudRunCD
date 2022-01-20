from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import joblib
import pandas as pd
import numpy as np
import datetime
import pytz

app = FastAPI()

@app.get("/")
def root():
    return "Hello from Cloud Run CD"

@app.get("/predict")
def predict(pickup_datetime, pickup_longitude, pickup_latitude,
            dropoff_longitude, dropoff_latitude, passenger_count):
   # create a datetime object from the user provided datetime
    input_datetime = pickup_datetime
    input_datetime = datetime.strptime(input_datetime, "%Y-%m-%d %H:%M:%S")

    #localize the user datetime with NYC timezone
    eastern = pytz.timezone("US/Eastern")
    localized_pickup_datetime = eastern.localize(input_datetime, is_dst=None)

# localize the datetime to UTC
    utc_pickup_datetime = localized_pickup_datetime.astimezone(pytz.utc)

# format the datetime
    formatted_pickup_datetime = utc_pickup_datetime.strftime(
        "%Y-%m-%d %H:%M:%S UTC")

    values = {
        "key": '2013-07-06 17:18:00.000000119',
        "pickup_datetime": formatted_pickup_datetime,
        "pickup_longitude": pickup_longitude,
        "pickup_latitude": pickup_latitude,
        "dropoff_longitude": dropoff_longitude,
        "dropoff_latitude": dropoff_latitude,
        "passenger_count": passenger_count
    }

    X_pred_DataFrame = pd.DataFrame(values, index=[0])
    X_pred_DataFrame['pickup_datetime'] = X_pred_DataFrame[
        'pickup_datetime'].astype(object)

#Loading the saved model with joblib
    model = joblib.load('model.joblib')

#make prediction
    prediction = model.predict(X_pred_DataFrame)[0]

    return {
        'prediction':prediction
        }
