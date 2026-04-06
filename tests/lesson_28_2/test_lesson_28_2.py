import os

from playwright.sync_api import expect
from tests.lesson_28_2.login_page import LoginPage

UI_URL = os.getenv("API_URL")
EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")



def test_add_car_add_expenses_delete_car(page):
    login = LoginPage(page)

    garage = login.navigate().submit(EMAIL, PASSWORD)

    expect(garage.get_alert_success()).to_have_text("You have been successfully logged in")
    garage.add_car()
    expenses = garage.expenses_click()
    expect(expenses.get_header_name()).to_have_text("Fuel expenses")
    expenses.add_expenses()
    garage = (expenses.garage_click())
    expect(garage.get_header_name()).to_have_text("Garage")
    garage.delete_car()