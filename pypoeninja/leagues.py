"""Functions for fetching general information about current/past leagues metadata."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, cast

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
    """League name"""
    url: str
    """Base URL of league's data"""
    display_name: str
    """Display name of the league"""
    hardcore: bool
    """Is league hardcore?"""
    indexed: bool
    """Is league indexed?"""


@dataclass
class SnapshotInfo:
    """Dataclass representing PoE.Ninja snapshot information"""

    url: str
    """Snapshot URL"""
    snapshot_type: str
    """Snapshot type"""
    name: str
    """Snapshot name"""
    time_machine_labels: list[str]
    """Time machine labels"""
    version: str
    """Snapshot version"""
    snapshot_name: str
    """Snapshot name"""
    overview_type: int
    """Overview type"""
    search_mode: int
    """Search mode"""
    has_server: bool
    """Has server?"""


@dataclass
class LeaguesMetadata:
    """Dataclass representing leagues and snapshots metadata"""

    economy_leagues: list[LeagueInfo]
    """List of current economy leagues' metadata"""
    old_economy_leagues: list[LeagueInfo]
    """List of old economy leagues' metadata"""
    snapshot_versions: list[SnapshotInfo]
    """Snapshots"""
    build_leagues: list[LeagueInfo]
    """List of leagues with available build statistics"""
    old_build_leagues: list[LeagueInfo]
    """List of old leagues with available build statistics"""


def extract_league_info(json_obj: dict[str, Any]) -> LeagueInfo:
    return LeagueInfo(
        name=json_obj["name"],
        url=json_obj["url"],
        display_name=json_obj["displayName"],
        hardcore=json_obj["hardcore"],
        indexed=json_obj["indexed"],
    )


def extract_snapshot_version(json_obj: dict[str, Any]) -> SnapshotInfo:
    return SnapshotInfo(
        url=json_obj["url"],
        snapshot_type=json_obj["type"],
        name=json_obj["name"],
        time_machine_labels=json_obj["timeMachineLabels"],
        version=json_obj["version"],
        snapshot_name=json_obj["snapshotName"],
        overview_type=json_obj["overviewType"],
        search_mode=json_obj["searchMode"],
        has_server=json_obj["hasServer"],
    )


def fetch_general_metadata() -> LeaguesMetadata:
    """Fetches the information about available leagues and snapshots.

    Returns:
        LeaguesMetadata: Dataclass instance with leagues and snapshots info.
    """
    request_data = get_json(api_index_url())
    economy_leagues = [extract_league_info(json_obj) for json_obj in request_data["economyLeagues"]]
    old_economy_leagues = [
        extract_league_info(json_obj) for json_obj in request_data["oldEconomyLeagues"]
    ]
    snapshot_versions = [
        extract_snapshot_version(json_obj) for json_obj in request_data["snapshotVersions"]
    ]
    build_leagues = [extract_league_info(json_obj) for json_obj in request_data["buildLeagues"]]
    old_build_leagues = [
        extract_league_info(json_obj) for json_obj in request_data["oldBuildLeagues"]
    ]
    return LeaguesMetadata(
        economy_leagues,
        old_economy_leagues,
        snapshot_versions,
        build_leagues,
        old_build_leagues,
    )


def fetch_league_info(league_name: str) -> LeagueInfo | None:
    """Fetches the metadata of specific league. Names can be found in :mod:`leagues_constants
    <pypoeninja.leagues_constants>` module.

    Args:
        league_name (str): Name of the league

    Returns:
        LeagueInfo | None: League metadata, or None if league is not found
    """
    leagues = fetch_general_metadata().economy_leagues + fetch_general_metadata().build_leagues
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
