import requests
from playwright.sync_api import expect
import os

UI_URL = os.getenv("API_URL")

# to run in bash
# python -m pytest --headed --browser=chromium --tracing=on
#trace view
# python -m playwright show-trace trace.zip


def test_check_create_car(create_car):
    expect(create_car).to_have_url(f"https://qauto.forstudy.space/panel/garage")


