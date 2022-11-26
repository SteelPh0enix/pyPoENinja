import pypoeninja.leagues as leagues
from tests.poeninja_constants import (
    CURRENT_TEMPORARY_LEAGUE_NAME,
    HARDCORE_LEAGUE_NAME,
    STANDARD_LEAGUE_NAME,
)


def test_fetching_economy_leagues():
    meta = leagues.fetch_general_metadata()
    expected_economy_leagues = [
        STANDARD_LEAGUE_NAME,
        HARDCORE_LEAGUE_NAME,
        CURRENT_TEMPORARY_LEAGUE_NAME,
    ]
    found_leagues = 0

    for league in meta.economyLeagues:
        if league.name in expected_economy_leagues:
            found_leagues += 1

    assert found_leagues == len(expected_economy_leagues)
