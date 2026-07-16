from camoufox.sync_api import Camoufox
import time

def scrape_with_camoufox():
    with Camoufox(headless=False) as browser:

        page = browser.new_page()
        url = "https://www.realtor.com/realestateandhomes-search/Austin_TX"

        page.goto(url)

        page.wait_for_timeout(5215)

        print(f"Page title: {page.title()}")

        time.sleep(5)

if __name__ == "__main__":

    scrape_with_camoufox()