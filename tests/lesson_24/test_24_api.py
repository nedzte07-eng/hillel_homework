import logging
import pytest

base_url = 'http://127.0.0.1:8080'

class TestCarsApi:
    def test_get_cars(self, session_sasha):
        response = session_sasha.get(base_url + "/cars?sort_by=price&limit=3")
        assert response.status_code == 200
        data = response.json()
        logging.info(f"Cars response: {data}")
        assert len(data) == 3

    def test_get_car(self, session_sasha):
        response = session_sasha.get(base_url + "/cars?sort_by=price&limit=8")
        assert response.status_code == 200
        data = response.json()
        logging.info(f"Cars response: {data}")
        assert len(data) == 8
