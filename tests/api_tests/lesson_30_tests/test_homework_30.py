import logging
import pytest
import requests
import allure

_log = logging.getLogger('Main')
log_format = logging.Formatter('%(asctime)s [%(levelname)s]  %(message)s')
console_handler = logging.StreamHandler()
console_handler.setFormatter(log_format)
_log.addHandler(console_handler)
_log.setLevel(logging.DEBUG)


@allure.feature("Testing of API add check and delete")
class TestContent:


    @pytest.mark.external_api
    @allure.story("Sign in with existing user")
    @allure.title("Checking of signing an existing user")
    @allure.description("Ensure that a user signing via API")
    def test_signin_with_existence_user_200(self, sign_up):
        user_id = sign_up.json()["data"]["userId"]
        with allure.step(f"Log in with user_id {user_id}"):
            with allure.step("Assert the status code"):
                assert sign_up.status_code == 200, "Response status code is incorrect"
            with allure.step("Assert the status user id"):
                assert user_id == 329784, "User was not signed in"


    @pytest.mark.external_api
    @allure.story("Adding a car to garage")
    @allure.title("Adding a car to the garage list")
    @allure.description("Ensure that a car is adding via API")
    def test_adding_a_car_201(self, sign_up, base_url, auth, car_credential):
        token_session = sign_up.cookies.get("sid")
        response_car = requests.post(
            f"{base_url}api/cars",
            auth=auth,
            json=car_credential,
            headers={"Cookie": f"sid={token_session}"}
        )
        data_car = response_car.json()["data"]
        with allure.step("Validation of adding car to garage"):
            with allure.step("Assert the status code"):
                assert response_car.status_code == 201, "Response status code is incorrect"
            with allure.step("Assert that id in response is not empty"):
                assert data_car["id"] is not None, "Id was not created"
            with allure.step("Assert that carBrandId in response is correct"):
                assert data_car["carBrandId"] == 2
            with allure.step("Assert that carModelId in response is correct"):
                assert data_car["carModelId"] == 8
            with allure.step("Assert that initialMileage in response is correct"):
                assert data_car["initialMileage"] == 555
            with allure.step("Assert that brand in response is correct"):
                assert data_car["brand"] == "BMW"
            with allure.step("Assert that model in response is correct"):
                assert data_car["model"] == "X5"
            with allure.step("Assert that logo in response is correct"):
                assert data_car["logo"] == "bmw.png"


    @pytest.mark.external_api
    @allure.story("Check if the car is added to garage")
    @allure.title("Checking presence of a car in the garage list")
    @allure.description("Ensure that a car is present via API")
    def test_if_car_is_present_200(self, car_data):
        data_car = car_data.json()["data"][0]
        with allure.step("Validation of that car is present in garage"):
            with allure.step("Assert the status code"):
                assert car_data.status_code == 200, "Response status code is incorrect"
            with allure.step("Assert that id in response is not empty"):
                assert data_car["id"] is not None, "Id was not created"
            with allure.step("Assert that carBrandId in response is correct"):
                assert data_car["carBrandId"] == 2
            with allure.step("Assert that carModelId in response is correct"):
                assert data_car["carModelId"] == 8
            with allure.step("Assert that initialMileage in response is correct"):
                assert data_car["initialMileage"] == 555
            with allure.step("Assert that brand in response is correct"):
                assert data_car["brand"] == "BMW"
            with allure.step("Assert that model in response is correct"):
                assert data_car["model"] == "X5"
            with allure.step("Assert that logo in response is correct"):
                assert data_car["logo"] == "bmw.png"


    # @pytest.mark.external_api
    # @allure.story("Check negative if the car is added to garage")
    # @allure.title("Checking presence of a car in the garage list - NEGATIVE test")
    # @allure.description("Ensure that a car is present via API - NEGATIVE test")
    # def test_if_car_is_present_200_failed_intentionally(self, car_data):
    #     data_car = car_data.json()["data"][0]
    #     with allure.step("Validation of that car is present in garage intentionally failed"):
    #         with allure.step("Assert the status code"):
    #             assert car_data.status_code == 200, "Response status code is incorrect"
    #         with allure.step("Assert that id in response is not empty"):
    #             assert data_car["id"] is not None, "Id was not created"
    #         with allure.step("Assert that carBrandId in response is correct - should fail here"):
    #             assert data_car["carBrandId"] == 4
    #         with allure.step("Assert that carModelId in response is correct"):
    #             assert data_car["carModelId"] == 8
    #         with allure.step("Assert that initialMileage in response is correct"):
    #             assert data_car["initialMileage"] == 555
    #         with allure.step("Assert that brand in response is correct"):
    #             assert data_car["brand"] == "BMW"
    #         with allure.step("Assert that model in response is correct"):
    #             assert data_car["model"] == "X5"
    #         with allure.step("Assert that logo in response is correct"):
    #             assert data_car["logo"] == "bmw.png"


    @pytest.mark.external_api
    @allure.story("Check deleting car from garage")
    @allure.title("Deleting a car from the garage list")
    @allure.description("Ensure that once a car is deleted via API")
    def test_deleting_a_car_200(self, sign_up, car_data, base_url):
        car_id = car_data.json()["data"][0]["id"]
        # print(car_id)
        token_session = sign_up.cookies.get("sid")
        response_car = requests.delete(f"{base_url}api/cars/{car_id}", headers={"Cookie": f"sid={token_session}"})
        deleted_car_id = response_car.json()["data"]["carId"]
        with allure.step("Validation of deleting car by id"):
            with allure.step("Assert the status code"):
                assert response_car.status_code == 200, "Response status code is incorrect"
            with allure.step("Assert the status in response JSON"):
                assert response_car.json()["status"] == "ok", "Car was not deleted"
            with allure.step(f"Assert the id car for deleting is {car_id} "):
                assert deleted_car_id == car_id, "Seems was deleted wrong car"


    @pytest.mark.external_api
    @allure.story("Check the absence of the car in garage")
    @allure.title("Checking that a car is absent in the garage list")
    @allure.description("Ensure that a car is absent via API")
    def test_if_car_is_absent_200(self, sign_up, base_url):
        token_session = sign_up.cookies.get("sid")
        response_car = requests.get(
            f"{base_url}api/cars", headers={"Cookie": f"sid={token_session}"})
        data = response_car.json()["data"]
        with allure.step("Validation by it that car is absent in garage:"):
            with allure.step("Assert the status code"):
                assert response_car.status_code == 200, "Response status code is incorrect"
            with allure.step("Assert that the data in response is empty"):
                assert data == [], "Cars were found"


    @pytest.mark.external_api
    @allure.story("Log out of the user")
    @allure.title("Checking of logging out of the user")
    @allure.description("Ensure that a user is logged out via API")
    def test_user_logout_200(self, sign_up, base_url):
        sid = sign_up.cookies.get("sid")
        response = requests.get(f"{base_url}api/auth/logout", headers={"Cookie": f"sid={sid}"})
        with allure.step("Validation of the user logging out"):
            with allure.step("Assert the status code"):
                assert response.status_code == 200, "Response status code is incorrect"
            with allure.step("Assert the status in response JSON"):
                assert response.json()["status"] == "ok", "Logout failed"



