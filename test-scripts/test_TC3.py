# TC3 : Valet parking – 5 hours or less – lower boundary less 1 minute

import re
from playwright.sync_api import Page, expect

def test_example(page: Page) -> None:
    page.goto("https://www.shino.de/parkcalc/")
    with page.expect_popup() as page7_info:
        page.get_by_role("row", name="Please input entry date and").get_by_role("link").click()
    page7 = page7_info.value
    page7.get_by_role("link", name="14").click()
    page.locator("#StartingTime").click()
    page.locator("#StartingTime").fill("08:00")
    with page.expect_popup() as page8_info:
        page.get_by_role("cell", name="MM/DD/YYYY Pick a date 12:00").get_by_role("link").click()
    page8 = page8_info.value
    page8.get_by_role("link", name="14").click()
    page.locator("#LeavingTime").click()
    page.locator("#LeavingTime").fill("08:00")
    page.get_by_role("button", name="Calculate").click()
    expect(page.get_by_role("rowgroup")).to_contain_text("$ 0.00")
    expect(page.get_by_role("rowgroup")).to_contain_text("(0 Days, 0 Hours, 0 Minutes)")