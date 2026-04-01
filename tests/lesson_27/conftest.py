import os

import pytest
from dotenv import load_dotenv
from playwright.sync_api import expect, Page

load_dotenv(dotenv_path=r"C:\Users\nedzt\Documents\Study\QA Automation Python\hillel_homework\.env")

ui_url = os.getenv('API_URL')
auth_user = os.getenv('AUTH_BASIC_USER')
auth_password = os.getenv('AUTH_BASIC_PASSWORD')
login = os.getenv('EMAIL')
password = os.getenv('PASSWORD')


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "http_credentials": {
            "username": auth_user,
            "password": auth_password
        },
        'base_url' :ui_url, #->     page.goto('https://qauto.forstudy.space/')
    }



@pytest.fixture(scope="function")
def ui_login(page: Page):
    page.goto('')
    page.locator('//button[@class="btn btn-outline-white header_signin"]').click()
    page.get_by_role("textbox", name="Email").fill(str(login))
    assert page.get_by_role("textbox", name="Email").input_value() == str(login)  # check if input field is fill 'STR'
    page.get_by_role("textbox", name="Password").fill(password)
    assert page.get_by_role("textbox", name="Password").input_value() == password
    page.get_by_role("button", name="Login").click()
    element_notify = page.locator('//div[@class="alert alert-success"]/p')
    expect(element_notify).to_have_text("You have been successfully logged in")
    assert element_notify.inner_text() == "You have been successfully logged in"
    page.reload()
    return page

