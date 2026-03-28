from playwright.sync_api import expect
import os

BASE_URL = os.getenv("RC1_ORION")

# to run in bash
# python -m pytest --headed --browser=chromium


def test_check_login(ui_login):
    expect(ui_login).to_have_url(f"{BASE_URL}")

    expect(ui_login.locator("span.account-user-name")).to_have_text("Sasha Nedzelnytsky")

