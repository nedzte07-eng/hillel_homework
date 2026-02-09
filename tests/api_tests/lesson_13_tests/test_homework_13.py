# 1)
import logging
import pytest
import requests

_log = logging.getLogger('Main')
log_format = logging.Formatter('%(asctime)s [%(levelname)s]  %(message)s')
console_handler = logging.StreamHandler()
console_handler.setFormatter(log_format)
_log.addHandler(console_handler)
_log.setLevel(logging.DEBUG)

# headers = {'Authorization': "Bearer token_256"}
# return response, headers
BASE_URL = "https://qauto.forstudy.space/"
AUTH = ("guest", "welcome2qauto")
USER_CREDENTIALS = {
"email": "nedzelnytskyidev+hillel02026@gmail.com",
"password": "AYf3JtDQnAcMbnc",
"remember": 'false'
}
CAR_CREDENTIALS = {
  "carBrandId": 2,
  "carModelId": 8,
  "mileage": 555
}

@pytest.fixture
def session_cookie():
    response = requests.post(
        f"{BASE_URL}api/auth/signin",
        auth=AUTH,
        json=USER_CREDENTIALS
    )
    assert response.status_code == 200, "Login failed"
    return response.cookies.get("sid")

@pytest.fixture
def car_id(session_cookie):
    response_car = requests.get(
        f"{BASE_URL}api/cars", headers={"Cookie": f"sid={session_cookie}"})
    data = response_car.json()["data"]
    assert data, "Cars were not found"
    return data[0]["id"]


class TestContent:

    def test_signin_with_existence_user(self, session_cookie):
        assert session_cookie is not None

    def test_adding_a_car(self, session_cookie):
        response_car = requests.post(
            f"{BASE_URL}api/cars",
            auth=AUTH,
            json=CAR_CREDENTIALS,
            headers={"Cookie": f"sid={session_cookie}"}
        )
        assert response_car.json()["status"] == "ok", "Car was not created"

    def test_if_car_is_present(self, session_cookie, car_id):
        print(car_id)
        assert car_id != [], "Cars were not found"

    def test_deleting_a_car(self, session_cookie, car_id):
        response_car = requests.delete(f"{BASE_URL}api/cars/{car_id}", headers={"Cookie": f"sid={session_cookie}"})
        assert response_car.json()["status"] == "ok", "Car was not deleted"

    def test_if_car_is_absent(self, session_cookie):
        response_car = requests.get(
            f"{BASE_URL}api/cars", headers={"Cookie": f"sid={session_cookie}"})
        data = response_car.json()["data"]
        assert data == [], "Cars were found"

    def test_user_logout(self, session_cookie):
        response = requests.get(f"{BASE_URL}api/auth/logout", headers={"Cookie": f"sid={session_cookie}"})
        assert response.json()["status"] == "ok", "Logout failed"



