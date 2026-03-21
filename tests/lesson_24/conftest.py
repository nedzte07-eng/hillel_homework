import logging
import pytest
import requests
from requests.auth import HTTPBasicAuth

base_url = 'http://127.0.0.1:8080'

payload = {
    "username": "sasha",
    "password": "sasha_test"
}

@pytest.fixture(scope="class")
def session_sasha():
    logging.info("Start of the fixture")
    session = requests.Session()
    response = session.post(base_url + '/auth', auth=HTTPBasicAuth(payload["username"], payload["password"]))

    if response.status_code == 200:
        logging.info("Logged in as sasha user")
        token = response.json()["access_token"]
        logging.info(f"Token for this session: {token}")

        # додаємо токен у заголовки для всієї сесії
        session.headers.update({"Authorization": f"Bearer {token}"})

        yield session
    else:
        logging.error("End of the fixture with failure")
        pytest.fail(f"Login failed with status {response.status_code}")


    logging.info("End of the fixture")
