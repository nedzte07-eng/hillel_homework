import requests

class TestApp:

    def test_upload_image(self, base_url, file_image):

        files, _ = file_image

        response = requests.post(f'{base_url}/upload', files=files)
        data = response.json()["image_url"]

        assert response.status_code == 201
        assert data == "http://127.0.0.1:8080/uploads/screenshot_for_19.jpg"

    def test_get(self, base_url, file_image):
        _,filename = file_image
        headers = {"Content-Type": "text"}
        response = requests.get(f'{base_url}/image/{filename}', headers=headers)
        data = response.json()["image_url"]

        assert response.status_code == 200
        assert data == "http://127.0.0.1:8080/uploads/screenshot_for_19.jpg"

    def test_delete(self, base_url, file_image):
        _,filename = file_image
        headers = {"Content-Type": "text"}
        response = requests.delete(f'{base_url}/delete/{filename}', headers=headers)
        data = response.json()["message"]

        assert response.status_code == 200
        assert data == "Image screenshot_for_19.jpg deleted"

