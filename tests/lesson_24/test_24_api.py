import logging
import pytest

base_url = 'http://127.0.0.1:8080'


class TestCarsApi:

    @pytest.mark.parametrize(
        "get_car_list",
        [
            {"sort_by": "brand", "limit": 5},
            {"sort_by": "year", "limit": 5},
            {"sort_by": "engine_volume", "limit": 5},
            {"sort_by": "price", "limit": 5},
        ],
        indirect=True
    )

    def test_get_car(self, get_car_list):
            data = get_car_list.json()
            assert get_car_list.status_code == 200
            assert len(data) == 5