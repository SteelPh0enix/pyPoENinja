import pytest
import requests
import requests_cache

import pypoeninja.urls as urls
from tests.poeninja_constants import DEFAULT_CATEGORY_NAME, DEFAULT_LEAGUE_NAME

STATUS_CODE_OK = 200
INVALID_CATEGORY_NAME = "invalid category"
INVALID_LANGUAGE = "invalid language"


requests_cache.install_cache()  # type: ignore


def check_url_request_status_code(url: str) -> int:
    request = requests.get(url)
    return request.status_code


def test_base_url_is_responding():
    assert check_url_request_status_code(urls.BASE_URL) == STATUS_CODE_OK


def test_api_index_url_is_responding():
    assert check_url_request_status_code(urls.api_index_url()) == STATUS_CODE_OK


def test_category_urls_are_responding():
    for category in urls.CATEGORIES:
        category_url = urls.api_category_url(DEFAULT_LEAGUE_NAME, category)
        assert check_url_request_status_code(category_url) == STATUS_CODE_OK


def test_category_url_fails_on_invalid_category():
    with pytest.raises(urls.UrlException):
        urls.api_category_url(DEFAULT_LEAGUE_NAME, INVALID_CATEGORY_NAME)


def test_category_url_fails_on_invalid_language():
    with pytest.raises(urls.UrlException):
        urls.api_category_url(
            DEFAULT_LEAGUE_NAME, DEFAULT_CATEGORY_NAME, INVALID_LANGUAGE
        )
