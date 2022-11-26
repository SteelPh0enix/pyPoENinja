"""This module contains functions for fetching general information about current/past leagues metadata."""

from pypoeninja.request_utils import get_json
from pypoeninja.urls import api_index_url
from typing import cast

LEAGUES_FIELD = "economyLeagues"
"""Field for economy leagues metadata"""

LeagueInfo = dict[str, str | bool]
"""Type representing league metadata"""
SnapshotInfo = dict[str, str | list[str]]
"""Type representing snapshot metadata"""
LeaguesMetadata = dict[str, list[LeagueInfo | SnapshotInfo]]
"""Type representing leagues metadata"""


def fetch_general_metadata() -> LeaguesMetadata:
    """Fetches the information about available leagues and snapshots.

    Returns:
        LeaguesMetadata: JSON with leagues and snapshots info.
    """
    return cast(LeaguesMetadata, get_json(api_index_url()))


def fetch_current_leagues() -> list[LeagueInfo]:
    """Fetches the list of current leagues metadata.

    Returns:
        List[LeagueInfo]: List of current leagues metadata.
    """
    return cast(list[LeagueInfo], fetch_general_metadata()[LEAGUES_FIELD])


def fetch_current_temporary_league() -> LeagueInfo:
    """Fetches the metadata of current temporary league.

    Returns:
        LeagueInfo: Current temporary league metadata.
    """
    return fetch_current_leagues()[0]
