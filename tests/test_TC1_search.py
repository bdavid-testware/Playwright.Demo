# Import necessary libraries, Playwright functions
import re
from socket import timeout
from playwright.sync_api import expect

# Define a pytest function (def test_...)
def test_nso(page):

    # Navigate to the website
    page.goto("https://www.nemzetisport.hu")
    
    # Accept cookies if the button is present, catch any exceptions and print an error message
    try:
        page.get_by_role("button", name="Elfogadom").click()

    except Exception as e:
        print(f"Hiba történt a cookie elfogadása során: {e}")
    
    # Interact with the search icon, fill in the search field and press Enter
    page.locator("//kesma-icon[@name='nso-search']//*[name()='svg']").click()
    page.get_by_placeholder("Keresés sportágra, csapatra, ligára vagy játékosra...").fill("Premier League")
    page.get_by_placeholder("Keresés sportágra, csapatra, ligára vagy játékosra...").press("Enter")

    # Verify outcome with an assertion, checking if the URL contains "Premier League"
    expect(page).to_have_url(re.compile(".Premier%20League"))
