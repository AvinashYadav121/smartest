import pickle
import json
import numpy as np

__locations = None
__model = None

def load_artifacts():
    global __locations
    global __model

    with open("predictor/estimator/ml/columns.pkl", "rb") as f:
        __locations = pickle.load(f)

    with open("predictor/estimator/ml/model.pkl", "rb") as f:
        __model = pickle.load(f)

def get_location_names():
    return __locations

def predict_price(location, sqft, bath, bhk):
    try:
        loc_index = __locations.index(location.lower())
    except:
        loc_index = -1

    x = np.zeros(len(__locations) + 3)
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index >= 0:
        x[loc_index + 3] = 1

    return round(__model.predict([x])[0], 2)
