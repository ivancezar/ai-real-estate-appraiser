import random
import pandas as pd

def generate_random_house():

    beds = random.randint(1,5)
    baths = random.choice([1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0])
    sqft = random.randint(500, 5000)
    zip_code = random.choice([78701, 78702, 78703, 78704, 78705])
    year_built = random.randint(1950, 2026)

    base_price = (sqft * 250) + (beds * 2000) + (baths * 15000)

    final_price = int(base_price * random.uniform(0.9, 1.1))

    return {
        "beds": beds,
        "baths": baths,
        "sqft": sqft,
        "zip_code": zip_code,
        "year_built": year_built,
        "final_price": final_price
    }

if __name__ == "__main__":
    print("Script started...")

    houses_list = []

    number_of_houses = 1000
    for _ in range(number_of_houses):
        house = generate_random_house()
        houses_list.append(house)
    
    #turn the dictionary list into a DataFrame (a table in pandas)
    df = pd.DataFrame(houses_list)

    #we save a csv file with all the generated houses
    #we use index = False to prevent having an extra column with the number of every row

    file_name = "Austin_houses_test.csv"
    df.to_csv(f"{file_name}", index=False, sep = ";")

    print("Data generation complete, Saved to " f"{file_name}")