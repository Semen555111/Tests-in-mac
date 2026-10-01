from playwright.sync_api import Page, expect
class HomePage:
    def __init__(self, page: Page):
        self.page = page
        self.performance_link = page.get_by_role("link", name="Performance")
        self.upgrade_button = page.get_by_role("button", name="Upgrade")


    def navigate_to_performance(self):
        self.performance_link.click()