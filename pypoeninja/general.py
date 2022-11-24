"""This module contains functions for fetching general information about current/past leagues metadata."""

from pypoeninja.request_utils import get_json
from pypoeninja.urls import api_index_url
from typing import Dict, List

LEAGUES_FIELD = "economyLeagues"
"""Field for economy leagues metadata"""

LeagueInfo = Dict[str, str | bool]
"""Type representing league metadata"""
SnapshotInfo = Dict[str, str | List[str]]
"""Type representing snapshot metadata"""


def fetch_general_metadata() -> Dict[str, List[LeagueInfo | SnapshotInfo]]:
    """Fetches the information about available leagues and snapshots.

    Returns:
        Dict[str, List[LeagueInfo | SnapshotInfo]]: JSON with leagues and snapshots info.
    """
    return get_json(api_index_url())  # type: ignore


def fetch_current_leagues() -> List[LeagueInfo]:
    """Fetches the list of current leagues metadata.

    Returns:
        List[LeagueInfo]: List of current leagues metadata.
    """
    return fetch_general_metadata()[LEAGUES_FIELD]  # type: ignore


def fetch_current_temporary_league() -> LeagueInfo:
    """Fetches the metadata of current temporary league.

    Returns:
        LeagueInfo: Current temporary league metadata.
    """
    return fetch_current_leagues()[0]
