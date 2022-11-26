"""This module contains functions for fetching general information about current/past leagues metadata."""

from dataclasses import dataclass

from dacite.core import from_dict

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


def fetch_current_temporary_league() -> LeagueInfo:
    """Fetches the metadata of current temporary league.

    Returns:
        LeagueInfo: Current temporary league metadata.
    """
    return fetch_general_metadata().economyLeagues[0]
