"""This module contains functions for fetching general information about current/past leagues metadata."""

import requests
from pypoeninja.urls import api_index_url

LEAGUES_FIELD = "economyLeagues"


def fetch_general_metadata():
    request = requests.get(api_index_url())
    return request.json()


def fetch_current_leagues():
    return fetch_general_metadata()[LEAGUES_FIELD]


def fetch_current_temporary_league():
    return fetch_current_leagues()[0]
