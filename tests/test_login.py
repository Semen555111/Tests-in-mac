import re
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from pages.home_page import HomePage

def test_login(page: Page) -> None:
    page.goto("https://opensource-demo.orangehrmlive.com/")
    login_page = LoginPage(page)
    login_page.username_input.fill("Admin")
    login_page.password_input.fill("admin123")
    login_page.login_button.click()
    home_page = HomePage(page)
    home_page.navigate_to_performance()
    expect(home_page.upgrade_button).to_be_visible()