import joblib

def estimate_house_value():

    # We load the trained model
    model = joblib.load("austin_model.joblib")

    # For now the houses are defined manually, just to test
    # Format: [beds, baths, sqft, year_built]
    new_house = [[3, 2.5, 1800, 2015]]

    # We use [0] because the result of model.predict is stored in an array, and we want the first (and only) output value
    estimated_price = model.predict(new_house)[0]
    
    print(f"Estimated Market Value: ${estimated_price:.2f}")

if __name__ == "__main__":
    estimate_house_value()