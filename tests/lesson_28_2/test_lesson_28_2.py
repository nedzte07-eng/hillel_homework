import os

from playwright.sync_api import expect
from pages.login_page import LoginPage

UI_URL = os.getenv("API_URL")
EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")



def test_login_to_garage(page):
    login = LoginPage(page)

    garage = login.navigate().submit(EMAIL, PASSWORD)

    expect(garage.get_alert_success()).to_have_text("You have been successfully logged in")
    garage.click_button_add_car()
