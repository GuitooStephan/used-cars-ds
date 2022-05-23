import joblib
import json
import uvicorn
import numpy as np
import pandas as pd
from pydantic import BaseModel
from used_cars.inference import make_predictions
from fastapi import FastAPI, File, UploadFile
from fastapi import FastAPI
from Car import Car

app = FastAPI(title='Car Price Prediction', version='1.0',
              description='')

db = SessionLocal()

@app.get('/')
@app.get('/home')
def read_home():
    return {'message': 'Thank you for using our car price prediction app'}

# When the feature values are received through a file

@app.post("/predict")
def predict(csv_file:UploadFile):
    user_data_df = pd.read_csv(csv_file.file,encoding='latin-1')
    
    predictions = make_predictions(user_data_df)
    user_data_df = user_data_df.fillna("")
    f_df = user_data_df.join(pd.DataFrame(predictions,columns=['Price']))
    
    return f_df.values.tolist()

# When the feature values are received through a request

@app.post("/predictSingle")
def predict(req:Car):
    dateCrawled:req.dateCrawled
    name:req.name
    name:req.name
    offerType:req.offerType
    abtest:req.abtest
    vehicleType:req.vehicleType
    yearOfRegistration:req.yearOfRegistration
    gearbox:req.gearbox
    powerPS:req.powerPS
    model:req.model
    kilometer:req.kilometer
    monthOfRegistration:req.monthOfRegistration
    fuelType:req.fuelType
    brand:req.brand
    notRepairedDamage:req.notRepairedDamage
    dateCreated:req.dateCreated
    nrOfPictures:req.nrOfPictures
    postalCode:req.postalCode
    lastSeen:req.lastSeen
  
    predictions = make_predictions(user_data_df)
    user_data_df = user_data_df.fillna("")
    f_df = user_data_df.join(pd.DataFrame([predictions[0]],columns=['Price']))
    
    return f_df.values.tolist()


@app.get('/predHistory')
def get_all_preds():
    pass

#@app.post('/predict')
#def add_pred(userdf,car:Car):
#    pass

    
if __name__ == '__main__':
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)