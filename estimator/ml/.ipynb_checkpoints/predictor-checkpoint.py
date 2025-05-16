import pickle
import numpy as np

# Load the model
model = pickle.load(open("estimator/ml/model.pkl", "rb"))

# This must be the *exact same* list used during training, in same order
locations = pickle.load(open("estimator/ml/columns.pkl", "rb"))  # load the full list

def predict_price(location, sqft, bath, bhk):
    try:
        loc_index = locations.index(location.lower()) if location.lower() in locations else locations.index("other")
    except ValueError:
        loc_index = locations.index("other")

    x = np.zeros(len(locations) + 3)
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    x[3 + loc_index] = 1  # one-hot encode the location

    return round(model.predict([x])[0], 2)
