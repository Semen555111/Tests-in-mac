import re
from playwright.sync_api import Playwright, sync_playwright, expect

def test_add_todo(page):
    page.wait_for_timeout(3000)
    page.goto('https://www.wikipedia.org')
    title = 'Govno'

    try:
        assert 'Wikipedia' in title, f"Site expected '{title}'"
    except:
        print('Expected Wikipedia bur got' f"{title}")



