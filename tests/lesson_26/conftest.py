import os
import pytest
from dotenv import load_dotenv
from playwright.sync_api import Page, expect

load_dotenv(dotenv_path=r"C:\Users\nedzt\Documents\Study\QA Automation Python\hillel_homework\.env")

BASE_URL = os.getenv("RC1_ORION")
USER_EMAIL = os.getenv("RC1_ORION_EMAIL")
USER_PASSWORD = os.getenv("RC1_ORION_PASSWORD")
BASIC_AUTH_USER = os.getenv("RC1_ORION_BASIC_USER")
BASIC_AUTH_PASS = os.getenv("RC1_ORION_BASIC_PASS")


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "http_credentials": {
            "username": BASIC_AUTH_USER,
            "password": BASIC_AUTH_PASS
        },
        'base_url' : BASE_URL,
    }



@pytest.fixture(scope="function")
def ui_login(page:Page):
    # logged_in_context.tracing.start(screenshots=True, snapshots=True, sources=True))
    page.goto("/admin/login")
    page.fill('input[name="email"]', USER_EMAIL)
    page.fill('input[name="password"]', USER_PASSWORD)
    page.click('button[type="submit"]')

    # після логіну cookies вже збережені в context
    expect(page.locator("span.account-user-name")).to_have_text("Sasha Nedzelnytsky")
    page.reload()
    yield page
    # yield page
    # logged_in_context.tracing.stop(path="trace.zip")
