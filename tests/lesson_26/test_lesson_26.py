from playwright.sync_api import expect
import os

BASE_URL = os.getenv("RC1_ORION")

# to run in bash
# python -m pytest --headed --browser=chromium --tracing on
#trace view
# python -m playwright show-trace test-results/tests-lesson-26-test-lesson-26-py-test-check-login-chromium/trace.zip


def test_check_login(ui_login):
    expect(ui_login).to_have_url(f"{BASE_URL}")

    expect(ui_login.locator("span.account-user-name")).to_have_text("Sasha Nedzelnytsky")

def test_order_page(ui_login):
    expect(ui_login).to_have_url(f"{BASE_URL}")
    expect(ui_login.locator("//span[text()='Orders']")).to_be_visible()
    ui_login.click("//span[text()='Orders']")
    expect(ui_login).to_have_url(f"{BASE_URL}/order")
    expect(ui_login.locator("a[href*='/admin/order/create']")).to_be_visible()
    ui_login.click("a[href*='/admin/order/create']")
    expect(ui_login).to_have_url(f"{BASE_URL}/order/create")



