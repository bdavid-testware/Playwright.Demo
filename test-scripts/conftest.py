import pytest
from playwright.sync_api import sync_playwright

# Fixture to launch a browser instance for testing

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()

# Fixture to create a new page for each test

@pytest.fixture
def page(browser):
    page = browser.new_page()
    yield page
    page.close()