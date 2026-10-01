from playwright.sync_api import Page, expect
class HomePage:
    def __init__(self, page: Page):
        self.page = page
        self.open_menu_button = page.get_by_role("button", name="Open Menu")
        self.slidebar_link = page.locator("[data-test=\"dynamic-catalog-slidebar-link\"]")
        self.slider_link = page.locator("[data-test=\"dynamic-catalog-slider-link\"]")
    def click_open_menu_button(self):
        self.open_menu_button.click()
        self.slidebar_link.click()
        self.slider_link.click()
    def is_primary_header_visible(self):
         expect(self.page.locator("[data-test=\"primary-header\"]")).to_contain_text("Swag Labs")