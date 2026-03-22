import logging
import pytest
import json

from lessons.lesson_19.homework_19_01 import response
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
    def test_get_sort_limit_car(self, get_car_list_with_parameters):
        response, length, sort_by = get_car_list_with_parameters
        data = response.json()
        values = [car[sort_by] for car in data]

        assert response.status_code == 200
        assert len(data) == length
        assert values == sorted(values)
        logging.info(f"Test get_sort_Limit_car with sort_by '{sort_by}' and limit '{length}' passed")

    def test_get_full_car_list(self, get_full_car_list):
        with open("cars_db.txt", "r", encoding="utf-8") as f:
            content = f.read()

        namespace = {}
        exec(content, namespace)  # виконує текст як Python‑код
        cars_db = namespace["cars_db"]  # тепер це dict

        # отримати список словників без id
        cars_list = list(cars_db.values())

        # відсортувати по brand
        cars_sorted = sorted(cars_list, key=lambda x: x["brand"])
        logging.info(f"Sorted list from db file: {cars_sorted}")

        assert response.status_code == 200
        assert len(get_full_car_list) == len(cars_sorted)
        assert get_full_car_list == cars_sorted
        logging.info(f"Test get_full_car_list with {len(cars_list)} cars passed")
