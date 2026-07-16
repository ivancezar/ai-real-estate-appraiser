from playwright.sync_api import sync_playwright
from playwright_stealth import Stealth
import time

def scrape_with_playwright():

    # we initialize Playwright's sesion
    with Stealth().use_sync(sync_playwright()) as p:
        # We launch Chromium. headless=False let's us see the bot's screen
        browser = p.chromium.launch(headless=False)

        context = browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        )
        # We open a window
        page = context.new_page()

        url = "https://www.realtor.com/realestateandhomes-search/Austin_TX"
        print(f"Navigating to {url}")

        # We go to the web
        page.goto(url)

        # We wait around 5 seconds to let the web's JavaScript fully load
        page.wait_for_timeout(5215)

        print("\nSucces. Browser loaded")
        print(f"\nPage title: {page.title()}")

        # An extra of 4 seconds to see the screen
        time.sleep(4)

        browser.close()

if __name__ == "__main__":
    scrape_with_playwright()
