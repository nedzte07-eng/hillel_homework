# 1)
import pytest
import requests

from tests.api_tests.lesson_13_tests.test_api_from_hillel_article_13 import base_url

# headers = {'Authorization': "Bearer token_256"}
# return response, headers
BASE_URL = 'https://qauto.forstudy.space/'


@pytest.mark.positive
def auth_login_positive_200():
    content = {'username': 'admin', 'password': 'admin'}
    response = requests.post(f'{BASE_URL}', json=content)
    assert response.status_code == 200, "Content was not created"


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