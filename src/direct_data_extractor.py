import requests
import csv
import time

def extract_all_houses():
    print("Inicialiting data extraction")

    # This is our digital disguise, by sending this headers, Python says to the server that is a web browser (user-agent)
    # that comes from Realtor search page (referer). T(rdc-client-name) is the custom heder used by Realtor to identify the
    # bot accesing the API

    headers = {
        'accept': '*/*',
        'accept-language': 'es-ES,es;q=0.9,en;q=0.8',
        'content-type': 'application/json',
        'origin': 'https://www.realtor.com',
        'rdc-client-name': 'WEB_SRP_ORACLE',
        'rdc-client-version': '0.0.1',
        'referer': 'https://www.realtor.com/realestateandhomes-search/78640',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36 OPR/131.0.0.0',
    }

    # Creates a file with write mode. newline = '' prevents windows adding blank rows between data. 
    with open('real_estate_dataset.csv', mode='w', newline='', encoding='utf-8') as csv_file:
        
        # Creates a writer object to format out text into CSV format and writes the first row, the columns headers.
        writer = csv.writer(csv_file)
        writer.writerow(['Property_ID', 'Price', 'Beds', 'Baths', 'Sqft', 'Address', 'City', 'Zip_Code'])

        extracted_houses = 0
        actual_offset = 0       # how many houses to skip on each request
        limit_per_page = 20     # how many houses we ask for at a time
        more_houses = True

        while more_houses:
            print(f"Downloading block (Offset: {actual_offset})...")

            # This is a GraphQL payload, it is different from an API REST because it only sends the data that we are asking for
            json_data = {
                'query': 'query HomeSearch($query: HomeSearchCriteria!, $limit: Int, $offset: Int, $bucket: SearchAPIBucket) {\n  home_search(\n    query: $query\n    limit: $limit\n    offset: $offset\n    bucket: $bucket\n  ) {\n    total\n    results {\n      property_id\n      list_price\n      list_price_min\n      description {\n        beds\n        beds_min\n        baths_consolidated\n        baths_min\n        sqft\n        sqft_min\n      }\n      location {\n        address {\n          line\n          city\n          postal_code\n        }\n      }\n    }\n  }\n}',
                'operationName': 'HomeSearch',
                'variables': {
                    'query': {
                        'primary': True,
                        'status': ['for_sale'],
                        'search_location': {'location': '78640'},
                    },
                    'limit': limit_per_page,
                    'offset': actual_offset,
                    'bucket': {'sort': 'fractal_v1.4.5_fr'},
                },
            }

            # This is the trigger. It sends a POST request to Realtor's database URL, wrapping it in our headers disguie and
            # attaching the json_data package
            response = requests.post('https://www.realtor.com/frontdoor/graphql', headers=headers, json=json_data)

            if response.status_code == 200:
                datos = response.json()
                results = datos.get('data', {}).get('home_search', {}).get('results', [])

                if not results:
                    print("No more properties, extraction finished")
                    more_houses = False
                    break

                for casa in results:
                    prop_id = casa.get('property_id') or 'N/A'
                    
                    #sometimes there is only a price_min
                    price = casa.get('list_price')
                    if price is None:
                        price = casa.get('list_price_min', 'N/A')
                        
                    desc = casa.get('description') or {}
                    
                    beds = desc.get('beds')
                    if beds is None:
                        beds = desc.get('beds_min', 'N/A')
                        
                    baths = desc.get('baths_consolidated')
                    if baths is None:
                        baths = desc.get('baths_min', 'N/A')
                        
                    sqft = desc.get('sqft')
                    if sqft is None:
                        sqft = desc.get('sqft_min', 'N/A')
                        
                    loc = casa.get('location') or {}
                    addr = loc.get('address') or {}
                    line = addr.get('line', 'N/A')
                    ciudad = addr.get('city', 'N/A')
                    postal = addr.get('postal_code', 'N/A')

                    writer.writerow([prop_id, price, beds, baths, sqft, line, ciudad, postal])
                    extracted_houses += 1

                actual_offset += limit_per_page
                time.sleep(1)
                
            else:
                print(f"Error. Code: {response.status_code}")
                more_houses = False

    print(f"\n It is done. {extracted_houses} properties stores in 'real_estate_dataset.csv'")

if __name__ == "__main__":
    extract_all_houses()