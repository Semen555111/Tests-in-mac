import re
from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("https://www.saucedemo.com/")
    page.locator("[data-test=\"username\"]").fill("standard_user")
    page.locator("[data-test=\"password\"]").fill("secre_sauce")
    page.locator("[data-test=\"login-button\"]").click()
    page.get_by_role("button", name="Open Menu").click()
    page.locator("[data-test=\"dynamic-catalog-sidebar-link\"]").click()
    page.locator("[data-test=\"dynamic-catalog-slider-link\"]").click()
    expect(page.locator("[data-test=\"primary-header\"]")).to_contain_text("Swag Labs")