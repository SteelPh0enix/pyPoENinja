import pypoeninja.urls as urls
import requests
import pytest


def check_url_request_status_code(url: str) -> int:
    request = requests.get(url)
    return request.status_code


STATUS_CODE_OK = 200
DEFAULT_LEAGUE = "Standard"
DEFAULT_CATEGORY = "Currency"
INVALID_CATEGORY = "abcdef"
INVALID_LANGUAGE = "qwerty"


def test_base_url_is_responding():
    assert check_url_request_status_code(urls.BASE_URL) == STATUS_CODE_OK


def test_api_index_url_is_responding():
    assert check_url_request_status_code(urls.api_index_url()) == STATUS_CODE_OK


def test_category_urls_are_responding():
    for category in urls.CATEGORIES:
        category_url = urls.api_category_url(DEFAULT_LEAGUE, category)
        assert check_url_request_status_code(category_url) == STATUS_CODE_OK


def test_category_url_fails_on_invalid_category():
    with pytest.raises(urls.UrlException):
        urls.api_category_url(DEFAULT_LEAGUE, INVALID_CATEGORY)


def test_category_url_fails_on_invalid_language():
    with pytest.raises(urls.UrlException):
        urls.api_category_url(DEFAULT_LEAGUE, DEFAULT_CATEGORY, INVALID_LANGUAGE)
