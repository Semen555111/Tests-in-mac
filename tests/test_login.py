import re
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from pages.home_page import HomePage

def test_login(page: Page) -> None:
    page.goto("https://www.saucedemo.com/")
    login_page = LoginPage(page)
    login_page.login("standard_user", "secret_sauce")
    home_page = HomePage(page)
    high = home_page.sort_products("hilo")
    prices1 = home_page.get_prices()
    prices_float = [float(price.replace("$", "")) for price in prices1]
    if len(prices_float) > 0:
        assert prices_float == sorted(prices_float, reverse=True)
    else:
        raise AssertionError("No prices found on the page.")
    low = home_page.sort_products("lohi")
    prices2 = home_page.get_prices()
    prices_float2 = [float(price.replace("$", "")) for price in prices2]
    if len(prices_float2) > 0:
        assert prices_float2 == sorted(prices_float2)
    else:
        raise AssertionError("No prices found on the page.")

