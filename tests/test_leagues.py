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


def test_expected_economy_leagues_appearance():
    """Check if economy leagues metadata contains expected leagues"""
    meta = leagues.fetch_general_metadata()
    found_leagues = 0
    for league in meta.economyLeagues:
        if league.name in EXPECTED_ECONOMY_LEAGUES:
            found_leagues += 1

    assert found_leagues == len(EXPECTED_ECONOMY_LEAGUES)


def test_expected_economy_leagues_state():
    """Check if economy leagues expected in metadata have expected field values"""
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


def test_expected_build_leagues_appearance():
    """Check if build leagues metadata contains expected leagues"""
    meta = leagues.fetch_general_metadata()
    found_leagues = 0
    for league in meta.buildLeagues:
        if league.name in EXPECTED_BUILD_LEAGUES:
            found_leagues += 1

    assert found_leagues == len(EXPECTED_BUILD_LEAGUES)


def test_expected_build_leagues_state():
    """Check if build leagues expected in metadata have expected field values"""
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
