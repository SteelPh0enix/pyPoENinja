"""This module contains functions for fetching general information about current/past leagues metadata."""

from dataclasses import dataclass
from typing import cast

from dacite.core import from_dict

from pypoeninja.leagues_constants import (
    CHALLENGE_LEAGUE_HC_NAME,
    CHALLENGE_LEAGUE_HC_SSF_NAME,
    CHALLENGE_LEAGUE_NAME,
    CHALLENGE_LEAGUE_SSF_NAME,
    HARDCORE_LEAGUE_NAME,
    STANDARD_LEAGUE_NAME,
)
from pypoeninja.request_utils import get_json
from pypoeninja.urls import api_index_url


@dataclass
class LeagueInfo:
    """Dataclass representing PoE.Ninja metadata of a single league"""

    name: str
    url: str
    displayName: str
    hardcore: bool
    indexed: bool


@dataclass
class SnapshotInfo:
    """Dataclass representing PoE.Ninja snapshot information"""

    url: str
    type: str
    name: str
    timeMachineLabels: list[str]
    version: str
    snapshotName: str


@dataclass
class LeaguesMetadata:
    """Dataclass representing leagues and snapshots metadata"""

    economyLeagues: list[LeagueInfo]
    oldEconomyLeagues: list[LeagueInfo]
    snapshotVersions: list[SnapshotInfo]
    buildLeagues: list[LeagueInfo]
    oldBuildLeagues: list[LeagueInfo]


def fetch_general_metadata() -> LeaguesMetadata:
    """Fetches the information about available leagues and snapshots.

    Returns:
        LeaguesMetadata: Dataclass instance with leagues and snapshots info.
    """
    return from_dict(data_class=LeaguesMetadata, data=get_json(api_index_url()))


def fetch_league_info(league_name: str) -> LeagueInfo | None:
    """Fetches the metadata of specific league. Names can be found in :ref:leagues_constants

    Args:
        league_name (str): Name of the league

    Returns:
        LeagueInfo | None: League metadata, or None if league is not found
    """
    leagues = (
        fetch_general_metadata().economyLeagues + fetch_general_metadata().buildLeagues
    )
    for league in leagues:
        if league.name == league_name:
            return league

    return None


def fetch_challenge_league_info() -> LeagueInfo:
    """Fetches the metadata of current challenge league.

    Returns:
        LeagueInfo: Current challenge league metadata.
    """
    return cast(LeagueInfo, fetch_league_info(CHALLENGE_LEAGUE_NAME))


def fetch_challenge_hc_league_info() -> LeagueInfo:
    """Fetches the metadata of current challenge hardcore league.

    Returns:
        LeagueInfo: Current challenge hardcore league metadata.
    """
    return cast(LeagueInfo, fetch_league_info(CHALLENGE_LEAGUE_HC_NAME))


def fetch_challenge_ssf_league_info() -> LeagueInfo:
    """Fetches the metadata of current challenge solo self-found league.

    Returns:
        LeagueInfo: Current challenge solo self-found league metadata.
    """
    return cast(LeagueInfo, fetch_league_info(CHALLENGE_LEAGUE_SSF_NAME))


def fetch_challenge_hc_ssf_league_info() -> LeagueInfo:
    """Fetches the metadata of current challenge hardcore solo self-found league.

    Returns:
        LeagueInfo: Current challenge hardcore solo self-found league metadata.
    """
    return cast(LeagueInfo, fetch_league_info(CHALLENGE_LEAGUE_HC_SSF_NAME))


def fetch_standard_league_info() -> LeagueInfo:
    """Fetches the metadata of standard league.

    Returns:
        LeagueInfo: Standard league metadata
    """
    return cast(LeagueInfo, fetch_league_info(STANDARD_LEAGUE_NAME))


def fetch_hardcore_league_info() -> LeagueInfo:
    """Fetches the metadata of standard league.

    Returns:
        LeagueInfo: Standard league metadata
    """
    return cast(LeagueInfo, fetch_league_info(HARDCORE_LEAGUE_NAME))
