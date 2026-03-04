import pytest
import os


@pytest.fixture
def base_url():
    URL = "http://127.0.0.1:8080"
    return URL

@pytest.fixture
def file_image():
    filename = "screenshot_for_19.jpg"
    image_file = os.path.join(os.path.dirname(__file__), filename)
    return {"image": open(image_file, "rb")}, filename