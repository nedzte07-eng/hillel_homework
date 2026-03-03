import os

import pytest
from dotenv import load_dotenv
load_dotenv(dotenv_path="utils/.env")

@pytest.fixture
def base_url():
    BASE_URL = os.getenv("RC1_ORION")
    return BASE_URL

@pytest.fixture
def user_credential():
    USER_CREDENTIALS = {
        "email": os.getenv("RC1_ORION_EMAIL"),
        "password": os.getenv("RC1_ORION_PASSWORD"),
        "remember": 'false'
    }
    return USER_CREDENTIALS

