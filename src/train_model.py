import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score
import joblib

def train_and_evaluate_model(file_path: str):
    print(f"Loading data from: {file_path}")
    df = pd.read_csv(file_path, sep = ";")

    # On the X axis are the characteristics and on the Y axis what we want to predict
    X = df[["beds", "baths","sqft", "year_built"]]
    y = df["final_price"]

    # This function mixes houses and returns the first 4 parameters
    # The random_state is like a "seed", in order to make the tests reproducible
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 20, random_state = 1)

    # We initialize and train the model. The model is trained with the houses information and their price 
    model = LinearRegression()
    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    # we evaluate the performance
    mae = mean_absolute_error(y_test, predictions)
    r2 = r2_score(y_test, predictions)

    print(f"Mean Absolute Error: {mae:.2f}")
    print(f"R2 Score:{r2:.4f}")

    print("\n--- Learned Weights ---")
    # In model.coef_ we can find the multiplyers (beta0, beta1...) that are assigned to each characterístic
    # What the zip() function does is "merging" two lists, so we can print a characteristic and its associated coeficient
    # The intercept is the y-value at which the line of the graph starts, when all coefficients are 0
    for col, coef in zip(X.columns, model.coef_):
        print(f"{col}: ${coef:.2f} per unit")
    print(f"Intercept: ${model.intercept_:.2f}")

    # We store the trained model with joblib
    model_name = "austin_model.joblib"
    joblib.dump(model, f"{model_name}")
    print(f"\n Model saved to {model_name}")

if __name__ == "__main__":
    CSV_FILE = "Austin_houses_test.csv"
    train_and_evaluate_model(CSV_FILE)
    