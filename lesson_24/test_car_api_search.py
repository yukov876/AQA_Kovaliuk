import logging
import pytest
import requests
from assertpy import assert_that

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(message)s",
    handlers=[
        logging.FileHandler("test_search.log"),
        logging.StreamHandler()
    ]
)

@pytest.mark.parametrize("sort_by, limit", [
    ("brand", 3),
    ("year", 2),
    ("engine_volume", 5),
    ("price", 300),
    (None, None)
])
def test_search_cars(authorization, sort_by, limit):
    params = {}

    if sort_by:
        params['sort_by'] = sort_by
    if limit:
        params['limit'] = limit

    response = authorization.get("http://127.0.0.1:8080/cars", params=params)

    logging.info(f"Запит: /cars?sort_by={sort_by}&limit={limit}")
    logging.info(f"Відповідь статус: {response.status_code}")
    logging.info(f"Відповідь JSON: {response.json()}")

    assert_that(response.status_code).is_equal_to(200)

    assert_that(response.json()).is_instance_of(list)

    for car in response.json():
        assert_that(car).contains_key("brand", "year", "engine_volume", "price")

    logging.info(f"Тест успішний для параметрів: sort_by={sort_by}, limit={limit}\n")

