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
        'base_url': ui_url,  # ->     page.goto('https://qauto.forstudy.space/')
    }
