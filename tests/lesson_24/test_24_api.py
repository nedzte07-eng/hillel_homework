import logging
import pytest
import json

from tests.lesson_24.conftest import payload

base_url = 'http://127.0.0.1:8080'


class TestCarsApi:

    @pytest.mark.parametrize(
        "get_car_list_with_parameters",
        [
            {"sort_by": "brand", "limit": 5},
            {"sort_by": "year", "limit": 8},
            {"sort_by": "engine_volume", "limit": 10},
            {"sort_by": "price", "limit": 19}
        ],
        indirect=True
    )

    def test_get_sort_Limit_car(self, get_car_list_with_parameters):

            response, length, sort_by = get_car_list_with_parameters
            data = response.json()
            values = [car[sort_by] for car in data]

            assert response.status_code == 200
            assert len(data) == length
            assert values == sorted(values)
            logging.info(f"Test get_sort_Limit_car with sort_by '{sort_by}' and limit '{length}' passed")

    def test_get_car_list(self, get_car_list):
        with open("cars_db.txt", "r", encoding="utf-8") as f:
            content = f.read()
            logging.info(f"Some log for test_get_car_list")

        assert True




