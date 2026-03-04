import urllib.parse


import requests

# url = 'http://127.0.0.1:8080'
# response = requests.get(url)
#
# # Перевірка статус-коду
# if response.status_code == 200:
#     data = response.json()  # отримання даних у форматі JSON
#     print('Отримано дані:', data)
# else:
#     print('Помилка. Статус-код:', response.status_code)

class TestApp:

    def test_upload_image(self, base_url, file_image):

        files, _ = file_image

        response = requests.post(f'{base_url}/upload', files=files)
        data = response.json()["image_url"]

        assert response.status_code == 201
        assert data == "http://127.0.0.1:8080/uploads/screenshot_for_19.jpg"

    def test_get(self, base_url, file_image):
        _,filename = file_image
        encoded_filename = urllib.parse.quote(filename)
        headers = {"Content-Type": "text"}
        response = requests.get(f'{base_url}/image/{encoded_filename}', headers=headers)
        data = response.json()["image_url"]

        assert response.status_code == 200
        assert data == "http://127.0.0.1:8080/uploads/screenshot_for_19.jpg"
