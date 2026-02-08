# 1)
import logging

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
  "mileage": 444
}

class TestContent:

    def test_signin_with_existence_user(self):
        print('Sign in with existence user')
        response = requests.post(f'{BASE_URL}api/auth/signin', auth=AUTH, json=USER_CREDENTIALS)
        assert response.status_code == 200, "Content was not created"

    def test_adding_a_car(self):
        print('Adding a car')
        response = requests.post(f'{BASE_URL}api/auth/signin', auth=AUTH, json=USER_CREDENTIALS)
        assert response.status_code == 200, "Content was not created"
        token_session = response.cookies.get("sid")
        response_car = requests.post(f'{BASE_URL}api/cars', auth=AUTH, json=CAR_CREDENTIALS, headers={"Cookie": f"sid={token_session}"})
        assert response_car.status_code == 201, "Content was not created"


        # yield response , 123, [1, 34]
        # #POST_TEST
        # print('Deleting content...')
        # response = requests.delete(f'{base_url}/content/{response.json().get('id')}')
        # assert response.status_code == 200, "Unable delete content"


    # def add_car(self, signin_with_existence_user):
    #     _log.info('Adding a car')
    #




    """
    # 2)
    @pytest.mark.positive
    def auth_login_negative_401():
        content = {'username': '12312312', 'password': '123123123'}
        response = requests.post(f'{BASE_URL}', json=content)
        assert response.status_code == 401, "Content was not created"
    
    # 3) створіть conftest file  і зробіть в ньому фікстуру -> Створіть окремий файл /users
    
    
    def test_get_content(auth_login):
        # assert False
        response, headers = auth_login
        print('Getting content...')
        # headers = headers -> очікуєтся, що фікстура зробить логін зі статусром 200 і в ньому буде лежати ТОКЕН
        response_get = requests.get(f'{base_url}/users', headers=headers) #url 'http://127.0.0.1:7070/api/v1/users'
        assert response_get.status_code == 200, "Unable to get content"
        server_content = response_get.json().get('content')
    
    """