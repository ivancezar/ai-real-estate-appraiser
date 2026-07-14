import pandas as pd

def load_and_inspect_data(file_path: str):

    print(f"Loading data from: {file_path}")

    # pandas configuration to display numbers in normal format with 2 decimals
    pd.set_option('display.float_format', lambda x: '%.2f' % x)

    # we read the data
    df = pd.read_csv(file_path, sep=";")

    # we print the first 5 rows to check the strcture. It is the same command as in R

    print("\n --- First 5 rows ---")
    print(df.head())

    # Statistical summary automatized by pandas

    print("\n --- Statistical Summary ---")
    print(df.describe())


    print("\n --- Correlation Matrix ---")
    # let's select only the columns we are interested in
    cols = ["beds", "baths", "sqft", "year_built", "final_price"]
    print(df[cols].corr())
    
if __name__ == "__main__":
    CSV_FILE = "Austin_houses_test.csv"
    load_and_inspect_data(CSV_FILE)
    