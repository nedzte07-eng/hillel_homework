import os
import pytest
import requests
from dotenv import load_dotenv

load_dotenv(dotenv_path="utils/.env")

@pytest.fixture
def base_url():
    BASE_URL = os.getenv("API_URL")
    return BASE_URL

@pytest.fixture
def auth():
    AUTH = ("guest", "welcome2qauto")
    return AUTH

@pytest.fixture
def user_credential():
    USER_CREDENTIALS = {
        "email": os.getenv("EMAIL"),
        "password": os.getenv("PASSWORD"),
        "remember": 'false'
    }
    return USER_CREDENTIALS

@pytest.fixture
def car_credential():
    CAR_CREDENTIALS = {
        "carBrandId": 2,
        "carModelId": 8,
        "mileage": 555
    }
    return CAR_CREDENTIALS

@pytest.fixture
def sign_up(base_url, auth, user_credential):
    response = requests.post(
        f"{base_url}api/auth/signin",
        auth=auth,
        json=user_credential
    )
    # return response.cookies.get("sid")
    return response

@pytest.fixture
def car_data(sign_up, base_url):
    token_session = sign_up.cookies.get("sid")
    response_car = requests.get(
        f"{base_url}api/cars", headers={"Cookie": f"sid={token_session}"})
    return response_car