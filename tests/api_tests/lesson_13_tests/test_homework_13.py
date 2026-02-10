import logging
import pytest
import requests

_log = logging.getLogger('Main')
log_format = logging.Formatter('%(asctime)s [%(levelname)s]  %(message)s')
console_handler = logging.StreamHandler()
console_handler.setFormatter(log_format)
_log.addHandler(console_handler)
_log.setLevel(logging.DEBUG)

class TestContent:

    @pytest.mark.external_api
    def test_signin_with_existence_user_200(self, sign_up):
        user_id = sign_up.json()["data"]["userId"]
        assert sign_up.status_code == 200, "Sign up failed"
        assert user_id == 328924, "User was not signed in"

    @pytest.mark.external_api
    def test_adding_a_car_201(self, sign_up, base_url, auth, car_credential):
        token_session = sign_up.cookies.get("sid")
        response_car = requests.post(
            f"{base_url}api/cars",
            auth=auth,
            json=car_credential,
            headers={"Cookie": f"sid={token_session}"}
        )
        assert response_car.status_code == 201, "Car was not created"
        assert response_car.json()["status"] == "ok", "Car was not created"

    @pytest.mark.external_api
    def test_if_car_is_present_200(self, sign_up, car_data):

        assert car_data.status_code == 200, "Car was not found"
        assert car_data != [], "Cars were not found"

    @pytest.mark.external_api
    def test_deleting_a_car_200(self, sign_up, car_data, base_url):
        car_id = car_data.json()["data"][0]["id"]
        print(car_id)
        token_session = sign_up.cookies.get("sid")
        response_car = requests.delete(f"{base_url}api/cars/{car_id}", headers={"Cookie": f"sid={token_session}"})
        assert response_car.json()["status"] == "ok", "Car was not deleted"

    @pytest.mark.external_api
    def test_if_car_is_absent_200(self, sign_up, base_url):
        sid = sign_up.cookies.get("sid")
        response_car = requests.get(
            f"{base_url}api/cars", headers={"Cookie": f"sid={sid}"})
        data = response_car.json()["data"]
        assert data == [], "Cars were found"

    @pytest.mark.external_api
    def test_user_logout_200(self, sign_up, base_url):
        sid = sign_up.cookies.get("sid")
        response = requests.get(f"{base_url}api/auth/logout", headers={"Cookie": f"sid={sid}"})
        assert response.json()["status"] == "ok", "Logout failed"



