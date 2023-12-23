"""Misc request utilities"""
from __future__ import annotations

from typing import Any

import requests
import requests_cache

DEFAULT_CACHE_EXPIRATION_TIME = 600
"""Default cache expiration time"""
APP_USER_AGENT = "pyPoENinja Client"
"""Application user agent"""
HTTP_OK_CODE = 200
"""HTTP OK code"""


class RequestError(Exception):
    """Stub class for request error"""


def enable_cache(expiration_time: int = DEFAULT_CACHE_EXPIRATION_TIME) -> None:
    """Enables request caching to reduce the amount of requests to PoE.Ninja API

    Args:
        expiration_time (int, optional): Amount of time until the cache is invalidated, in seconds.
                                         Defaults to :const:`DEFAULT_CACHE_EXPIRATION_TIME`
    """
    requests_cache.install_cache(  # type: ignore
        expire_after=expiration_time,
        allowable_methods=["GET"],
    )


def disable_cache() -> None:
    """Disables request caching"""
    requests_cache.uninstall_cache()


def is_cache_enabled() -> bool:
    """Checks if request caching is enabled

    Returns:
        bool: is caching enabled?
    """
    return requests_cache.is_installed()


def get_json(url: str, timeout: float = 5.0) -> dict[str, Any]:
    """Performs HTTP GET for a JSON at specified URL. Throws RequestError with HTTP status code if
    it's not successful.

    Args:
        url (str): URL from which the JSON will be fetched
        timeout (float): Timeout in seconds. 5 by default.

    Returns:
        dict[str, Any]: JSON response
    """
    headers = {"User-Agent": APP_USER_AGENT}
    request = requests.get(url, headers=headers, timeout=timeout)
    if request.status_code != HTTP_OK_CODE:
        raise RequestError(request.status_code)
    return request.json()


# Cache is enabled by default, to reduce the amount of requests - especially in tests.
# You may disable it manually, if needed.
enable_cache()
