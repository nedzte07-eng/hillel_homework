import logging
import requests

_log = logging.getLogger('Main')
log_format = logging.Formatter('%(asctime)s [%(levelname)s]  %(message)s')
console_handler = logging.StreamHandler()
console_handler.setFormatter(log_format)
_log.addHandler(console_handler)
_log.setLevel(logging.DEBUG)

base_url = 'http://127.0.0.1:7070'
content = {'cars': ['Audi, VW', 'Toyota']}
updated_content = {'bikes': ['Honda', 'Suzuki']}


@allure.feature("Testing of API add check and delete")
class TestContent:


    @pytest.mark.external_api
    @allure.story("Sign in with existing user")
    def test_signin_with_existence_user_200(self, sign_up):
        user_id = sign_up.json()["data"]["userId"]
        with allure.step(f"Log in with user_id {user_id}"):
            with allure.step("Assert the status code"):
                assert sign_up.status_code == 200, "Response status code is incorrect"
            with allure.step("Assert the status user id"):
                assert user_id == 329784, "User was not signed in"

    def test_get_content(self):
        _log.info('Getting content...')
        response_get = requests.get(f'{base_url}/content')
        assert response_get.status_code == 200, "Unable to get content"
        server_content = response_get.json().get('content')
        assert content in server_content

    def test_modify_content(self):
        _log.info('Modifying content...')
        response = requests.put(f'{base_url}/content/0', json=updated_content)
        assert response.status_code == 200, "Unable modify content"
        assert response.json().get('message') == 'Content updated successfully!'

    def test_deleting_content(self):
        _log.info('Deleting content...')
        response = requests.delete(f'{base_url}/content/0')
        assert response.status_code == 200, "Unable delete content"
        assert response.json().get('message') == 'Content deleted successfully!'