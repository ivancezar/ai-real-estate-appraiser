import pandas as pd

def clean_dataset():

    # Loading the CSV file into a Pandas DataFrame
    df = pd.read_csv("real_estate_dataset.csv")

    initial_total = len(df)

    # Drop rows with missing values in important columns (drop not available)
    df = df.dropna(subset=['Beds', 'Baths', 'Sqft', 'Price'])

    # Some data contain "+", so we eliminate it
    df['Baths'] = df['Baths'].astype(str).str.replace('+', '').astype(float)
    df['Beds'] = df['Beds'].astype(str).str.replace('+', '').astype(float)

    # Convert numeric columns to integers
    df['Beds'] = df['Beds'].astype(int)
    df['Sqft'] = df['Sqft'].astype(int)
    df['Price'] = df['Price'].astype(int)

    # Filtering outliers and invalid data

    df = df[df['Beds'] > 0]
    df = df[df['Price'] > 50000]
    df = df[df['Sqft'] > 300]

    # We save the rows without numeration

    df.to_csv('cleaned_real_estate_dataset.csv', index=False)

    final_total = len(df)

    print(f"Initial raw properties: {initial_total}")
    print(f"Clean properties ready for ML: {final_total}")


if __name__ == "__main__":
    clean_dataset()