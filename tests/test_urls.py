"""Unit tests for URL-related code"""
from datetime import timedelta

import pytest
import requests
import requests_cache

from pypoeninja import urls
from pypoeninja.leagues_constants import CHALLENGE_LEAGUE_NAME

STATUS_CODE_OK = 200
DEFAULT_TIMEOUT_SECONDS = 5.0
INVALID_CATEGORY_NAME = "invalid category"
INVALID_LANGUAGE = "invalid language"
DEFAULT_LEAGUE_NAME = CHALLENGE_LEAGUE_NAME
DEFAULT_CATEGORY_NAME = next(iter(urls.CATEGORIES.keys()))

requests_cache.install_cache(
    "tests_cache",
    backend="sqlite",
    use_temp=True,
    expire_after=timedelta(hours=1),
)


def check_url_request_status_code(url: str) -> int:
    request = requests.get(url, timeout=DEFAULT_TIMEOUT_SECONDS)
    return request.status_code


def test_base_url_is_responding() -> None:
    assert check_url_request_status_code(urls.BASE_URL) == STATUS_CODE_OK


def test_api_index_url_is_responding() -> None:
    assert check_url_request_status_code(urls.api_index_url()) == STATUS_CODE_OK


def test_category_urls_are_responding() -> None:
    for category in urls.CATEGORIES:
        category_url = urls.api_category_url(DEFAULT_LEAGUE_NAME, category)
        assert check_url_request_status_code(category_url) == STATUS_CODE_OK


def test_category_url_fails_on_invalid_category() -> None:
    with pytest.raises(urls.UrlError):
        urls.api_category_url(DEFAULT_LEAGUE_NAME, INVALID_CATEGORY_NAME)


def test_category_url_fails_on_invalid_language() -> None:
    with pytest.raises(urls.UrlError):
        urls.api_category_url(
            DEFAULT_LEAGUE_NAME,
            DEFAULT_CATEGORY_NAME,
            INVALID_LANGUAGE,
        )
