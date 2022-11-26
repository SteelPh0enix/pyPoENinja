import pypoeninja.leagues as leagues
from pypoeninja.leagues_constants import (
    HARDCORE_LEAGUE_NAME,
    STANDARD_LEAGUE_NAME,
    TEMPORARY_LEAGUE_HC_NAME,
    TEMPORARY_LEAGUE_HC_SSF_NAME,
    TEMPORARY_LEAGUE_NAME,
    TEMPORARY_LEAGUE_SSF_NAME,
)

EXPECTED_ECONOMY_LEAGUES = [
    STANDARD_LEAGUE_NAME,
    HARDCORE_LEAGUE_NAME,
    TEMPORARY_LEAGUE_NAME,
    TEMPORARY_LEAGUE_HC_NAME,
]

EXPECTED_BUILD_LEAGUES = [
    TEMPORARY_LEAGUE_NAME,
    TEMPORARY_LEAGUE_HC_NAME,
    TEMPORARY_LEAGUE_SSF_NAME,
    TEMPORARY_LEAGUE_HC_SSF_NAME,
]

EXPECTED_LEAGUES = [
    STANDARD_LEAGUE_NAME,
    HARDCORE_LEAGUE_NAME,
    TEMPORARY_LEAGUE_NAME,
    TEMPORARY_LEAGUE_HC_NAME,
    TEMPORARY_LEAGUE_SSF_NAME,
    TEMPORARY_LEAGUE_HC_SSF_NAME,
]

INVALID_LEAGUE_NAME = "invalid league"


def test_fetch_general_metadata_returns_expected_economy_leagues():
    meta = leagues.fetch_general_metadata()
    found_leagues = 0
    for league in meta.economyLeagues:
        if league.name in EXPECTED_ECONOMY_LEAGUES:
            found_leagues += 1

    assert found_leagues == len(EXPECTED_ECONOMY_LEAGUES)


def test_fetch_general_metadata_returns_expected_build_leagues():
    meta = leagues.fetch_general_metadata()
    found_leagues = 0
    for league in meta.buildLeagues:
        if league.name in EXPECTED_BUILD_LEAGUES:
            found_leagues += 1

    assert found_leagues == len(EXPECTED_BUILD_LEAGUES)


def test_fetch_league_metadata_returns_none_on_invalid_league():
    assert leagues.fetch_league_info(INVALID_LEAGUE_NAME) is None


def test_fetch_league_metadata_returns_expected_leagues():
    for league_name in EXPECTED_LEAGUES:
        league = leagues.fetch_league_info(league_name)
        assert league is not None


def test_fetch_challenge_league_info_does_not_return_none():
    """this verifies that cast() is not silencing potential error, although other tests should also catch it"""
    assert leagues.fetch_challenge_league_info() is not None
