"""Unit tests of code fetching league informations"""
from __future__ import annotations

from pypoeninja import leagues
from pypoeninja.leagues_constants import (
    CHALLENGE_LEAGUE_HC_NAME,
    CHALLENGE_LEAGUE_HC_SSF_NAME,
    CHALLENGE_LEAGUE_NAME,
    CHALLENGE_LEAGUE_SSF_NAME,
    HARDCORE_LEAGUE_NAME,
    STANDARD_LEAGUE_NAME,
)

EXPECTED_ECONOMY_LEAGUES = [
    STANDARD_LEAGUE_NAME,
    HARDCORE_LEAGUE_NAME,
    CHALLENGE_LEAGUE_NAME,
    CHALLENGE_LEAGUE_HC_NAME,
]

EXPECTED_BUILD_LEAGUES = [
    CHALLENGE_LEAGUE_NAME,
    CHALLENGE_LEAGUE_HC_NAME,
    CHALLENGE_LEAGUE_SSF_NAME,
    CHALLENGE_LEAGUE_HC_SSF_NAME,
]

EXPECTED_LEAGUES = [
    STANDARD_LEAGUE_NAME,
    HARDCORE_LEAGUE_NAME,
    CHALLENGE_LEAGUE_NAME,
    CHALLENGE_LEAGUE_HC_NAME,
    CHALLENGE_LEAGUE_SSF_NAME,
    CHALLENGE_LEAGUE_HC_SSF_NAME,
]

INVALID_LEAGUE_NAME = "invalid league"


def test_fetch_general_metadata_returns_expected_economy_leagues() -> None:
    meta = leagues.fetch_general_metadata()
    found_leagues = 0
    for league in meta.economy_leagues:
        if league.name in EXPECTED_ECONOMY_LEAGUES:
            found_leagues += 1

    assert found_leagues == len(EXPECTED_ECONOMY_LEAGUES)


def test_fetch_general_metadata_returns_expected_build_leagues() -> None:
    meta = leagues.fetch_general_metadata()
    found_leagues = 0
    for league in meta.build_leagues:
        if league.name in EXPECTED_BUILD_LEAGUES:
            found_leagues += 1

    assert found_leagues == len(EXPECTED_BUILD_LEAGUES)


def test_fetch_league_metadata_returns_none_on_invalid_league() -> None:
    assert leagues.fetch_league_info(INVALID_LEAGUE_NAME) is None


def test_fetch_league_metadata_returns_expected_leagues() -> None:
    for league_name in EXPECTED_LEAGUES:
        league = leagues.fetch_league_info(league_name)
        assert league is not None


def test_fetch_challenge_league_info_returns_correct_metadata() -> None:
    """this verifies that cast() is not silencing potential error, although other tests should also
    catch it"""
    meta = leagues.fetch_challenge_league_info()
    assert meta is not None
    assert meta.name == CHALLENGE_LEAGUE_NAME


def test_fetch_challenge_hc_league_info_returns_correct_metadata() -> None:
    """this verifies that cast() is not silencing potential error, although other tests should also
    catch it"""
    meta = leagues.fetch_challenge_hc_league_info()
    assert meta is not None
    assert meta.name == CHALLENGE_LEAGUE_HC_NAME


def test_fetch_challenge_ssf_league_info_returns_correct_metadata() -> None:
    """this verifies that cast() is not silencing potential error, although other tests should also
    catch it"""
    meta = leagues.fetch_challenge_ssf_league_info()
    assert meta is not None
    assert meta.name == CHALLENGE_LEAGUE_SSF_NAME


def test_fetch_challenge_hc_ssf_league_info_returns_correct_metadata() -> None:
    """this verifies that cast() is not silencing potential error, although other tests should also
    catch it"""
    meta = leagues.fetch_challenge_hc_ssf_league_info()
    assert meta is not None
    assert meta.name == CHALLENGE_LEAGUE_HC_SSF_NAME


def test_fetch_standard_league_info_returns_correct_metadata() -> None:
    """this verifies that cast() is not silencing potential error, although other tests should also
    catch it"""
    meta = leagues.fetch_standard_league_info()
    assert meta is not None
    assert meta.name == STANDARD_LEAGUE_NAME


def test_fetch_hardcore_league_info_returns_correct_metadata() -> None:
    """this verifies that cast() is not silencing potential error, although other tests should also
    catch it"""
    meta = leagues.fetch_hardcore_league_info()
    assert meta is not None
    assert meta.name == HARDCORE_LEAGUE_NAME
