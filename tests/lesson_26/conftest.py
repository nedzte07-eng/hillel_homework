import os
import pytest
from dotenv import load_dotenv

load_dotenv(dotenv_path=r"C:\Users\nedzt\Documents\Study\QA Automation Python\hillel_homework\.env")

BASE_URL = os.getenv("RC1_ORION")
USER_EMAIL = os.getenv("RC1_ORION_EMAIL")
USER_PASSWORD = os.getenv("RC1_ORION_PASSWORD")
BASIC_AUTH_USER = os.getenv("RC1_ORION_BASIC_USER")
BASIC_AUTH_PASS = os.getenv("RC1_ORION_BASIC_PASS")


@pytest.fixture(scope="session")
def logged_in_context(browser):
    context = browser.new_context(
        http_credentials={"username": BASIC_AUTH_USER, "password": BASIC_AUTH_PASS}
    )
    page = context.new_page()
    page.goto(f"{BASE_URL}/login")
    page.fill('input[name="email"]', USER_EMAIL)
    page.fill('input[name="password"]', USER_PASSWORD)
    page.click('button[type="submit"]')
    # після логіну cookies вже збережені в context
    page.close()
    yield context

@pytest.fixture(scope="function")
def ui_login(logged_in_context):
    page = logged_in_context.new_page()
    page.goto(f"{BASE_URL}")
    yield page
