import pypoeninja.leagues as leagues
from pypoeninja.leagues_constants import (
    HARDCORE_LEAGUE_DISPLAY_NAME,
    HARDCORE_LEAGUE_NAME,
    HARDCORE_LEAGUE_URL,
    STANDARD_LEAGUE_DISPLAY_NAME,
    STANDARD_LEAGUE_NAME,
    STANDARD_LEAGUE_URL,
    TEMPORARY_LEAGUE_DISPLAY_NAME,
    TEMPORARY_LEAGUE_HC_DISPLAY_NAME,
    TEMPORARY_LEAGUE_HC_NAME,
    TEMPORARY_LEAGUE_HC_SSF_DISPLAY_NAME,
    TEMPORARY_LEAGUE_HC_SSF_NAME,
    TEMPORARY_LEAGUE_HC_SSF_URL,
    TEMPORARY_LEAGUE_HC_URL,
    TEMPORARY_LEAGUE_NAME,
    TEMPORARY_LEAGUE_SSF_DISPLAY_NAME,
    TEMPORARY_LEAGUE_SSF_NAME,
    TEMPORARY_LEAGUE_SSF_URL,
    TEMPORARY_LEAGUE_URL,
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


def test_fetch_general_metadata_economy_leagues_have_expected_field_values():
    meta = leagues.fetch_general_metadata()
    for league in meta.economyLeagues:
        if league.name == TEMPORARY_LEAGUE_NAME:
            assert league.url == TEMPORARY_LEAGUE_URL
            assert league.displayName == TEMPORARY_LEAGUE_DISPLAY_NAME
            assert league.hardcore is False
            assert league.indexed is True
        if league.name == TEMPORARY_LEAGUE_HC_NAME:
            assert league.url == TEMPORARY_LEAGUE_HC_URL
            assert league.displayName == TEMPORARY_LEAGUE_HC_DISPLAY_NAME
            assert league.hardcore is True
            assert league.indexed is False
        elif league.name == STANDARD_LEAGUE_NAME:
            assert league.url == STANDARD_LEAGUE_URL
            assert league.displayName == STANDARD_LEAGUE_DISPLAY_NAME
            assert league.hardcore is False
            assert league.indexed is False
        elif league.name == HARDCORE_LEAGUE_NAME:
            assert league.url == HARDCORE_LEAGUE_URL
            assert league.displayName == HARDCORE_LEAGUE_DISPLAY_NAME
            assert league.hardcore is True
            assert league.indexed is False


def test_fetch_general_metadata_returns_expected_build_leagues():
    meta = leagues.fetch_general_metadata()
    found_leagues = 0
    for league in meta.buildLeagues:
        if league.name in EXPECTED_BUILD_LEAGUES:
            found_leagues += 1

    assert found_leagues == len(EXPECTED_BUILD_LEAGUES)


def test_fetch_general_metadata_build_leagues_have_expected_field_values():
    meta = leagues.fetch_general_metadata()
    for league in meta.economyLeagues:
        if league.name == TEMPORARY_LEAGUE_NAME:
            assert league.url == TEMPORARY_LEAGUE_URL
            assert league.displayName == TEMPORARY_LEAGUE_DISPLAY_NAME
            assert league.hardcore is False
            assert league.indexed is True
        if league.name == TEMPORARY_LEAGUE_HC_NAME:
            assert league.url == TEMPORARY_LEAGUE_HC_URL
            assert league.displayName == TEMPORARY_LEAGUE_HC_DISPLAY_NAME
            assert league.hardcore is True
            assert league.indexed is False
        if league.name == TEMPORARY_LEAGUE_SSF_NAME:
            assert league.url == TEMPORARY_LEAGUE_SSF_URL
            assert league.displayName == TEMPORARY_LEAGUE_SSF_DISPLAY_NAME
            assert league.hardcore is False
            assert league.indexed is False
        if league.name == TEMPORARY_LEAGUE_HC_SSF_NAME:
            assert league.url == TEMPORARY_LEAGUE_HC_SSF_URL
            assert league.displayName == TEMPORARY_LEAGUE_HC_SSF_DISPLAY_NAME
            assert league.hardcore is True
            assert league.indexed is False


def test_fetch_league_metadata_returns_none_on_invalid_league():
    assert leagues.fetch_league_metadata(INVALID_LEAGUE_NAME) is None


def test_fetch_league_metadata_returns_expected_leagues():
    for league_name in EXPECTED_LEAGUES:
        league = leagues.fetch_league_metadata(league_name)
        assert league is not None
