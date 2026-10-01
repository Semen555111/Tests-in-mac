import re
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from pages.home_page import HomePage


def test_login(page: Page) -> None:
    login_page = LoginPage(page)
    home_page = HomePage(page)

    page.goto("https://www.saucedemo.com/")
    login_page.username_input('standard_user')
    login_page.password_input('secret_sauce')
    login_page.login_button.click()
    expect(home_page.is_primary_header_visible()).to_be_true()
    home_page.click_open_menu_button()
    home_page.is_primary_header_visible()