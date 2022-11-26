import pypoeninja.leagues as leagues

CURRENT_TEMPORARY_LEAGUE = "Kalandra"


def test_fetching_economy_leagues():
    meta = leagues.fetch_general_metadata()
    expected_economy_leagues = ["Standard", "Hardcore", CURRENT_TEMPORARY_LEAGUE]
    found_leagues = 0

    for league in meta.economyLeagues:
        if league.name in expected_economy_leagues:
            found_leagues += 1

    assert found_leagues == len(expected_economy_leagues)
