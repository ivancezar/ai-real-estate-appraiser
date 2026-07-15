import requests
from bs4 import BeautifulSoup

def scrape_test_site():

    url = "https://toscrape.com"

    print(f"Starting connection with {url}")

    answer = requests.get(url)

    if answer.status_code == 200:
        print("Succesfull Connection")
    
        soup = BeautifulSoup(answer.text, "html.parser")

        title = soup.select_one("h1")

        if title:
            print(f"Data extracted by the bot: {title.text.strip()}")
    
    else:
        print(f"Connection error. Code: {answer.status_code}")

if __name__ == "__main__":
    scrape_test_site()
