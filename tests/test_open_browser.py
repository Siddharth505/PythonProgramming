
from playwright.sync_api import Page, expect


def test_open_browser(page: Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    url = page.url
    print("URL is:", url)
    expect(page).to_have_url("https://rahulshettyacademy.com/AutomationPractice/")