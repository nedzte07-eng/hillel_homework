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
    def test_signin_with_existence_user_200(self, session_cookie):
        assert session_cookie is not None

    @pytest.mark.external_api
    def test_adding_a_car_201(self, session_cookie, base_url, auth, car_credential):
        response_car = requests.post(
            f"{base_url}api/cars",
            auth=auth,
            json=car_credential,
            headers={"Cookie": f"sid={session_cookie}"}
        )
        assert response_car.json()["status"] == "ok", "Car was not created"

    @pytest.mark.external_api
    def test_if_car_is_present_200(self, session_cookie, car_id):
        print(car_id)
        assert car_id != [], "Cars were not found"

    @pytest.mark.external_api
    def test_deleting_a_car_200(self, session_cookie, car_id, base_url):
        response_car = requests.delete(f"{base_url}api/cars/{car_id}", headers={"Cookie": f"sid={session_cookie}"})
        assert response_car.json()["status"] == "ok", "Car was not deleted"

    @pytest.mark.external_api
    def test_if_car_is_absent_200(self, session_cookie, base_url):
        response_car = requests.get(
            f"{base_url}api/cars", headers={"Cookie": f"sid={session_cookie}"})
        data = response_car.json()["data"]
        assert data == [], "Cars were found"

    @pytest.mark.external_api
    def test_user_logout_200(self, session_cookie, base_url):
        response = requests.get(f"{base_url}api/auth/logout", headers={"Cookie": f"sid={session_cookie}"})
        assert response.json()["status"] == "ok", "Logout failed"



