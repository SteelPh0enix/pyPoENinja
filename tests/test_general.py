import pypoeninja.general as general

CURRENT_LEAGUE = "Kalandra"


def test_general_metadata_has_expected_fields():
    metadata = general.fetch_general_metadata()
    assert "economyLeagues" in metadata
    assert "oldEconomyLeagues" in metadata
    assert "snapshotVersions" in metadata
    assert "buildLeagues" in metadata
    assert "oldBuildLeagues" in metadata


def test_current_leagues_has_expected_leagues():
    leagues = general.fetch_current_leagues()
    expected_leagues = ["Standard", "Hardcore"]
    expected_leagues_found = 0
    for league in leagues:
        if league["name"] in expected_leagues:
            expected_leagues_found += 1

    assert expected_leagues_found == len(expected_leagues)


def test_league_structure_has_expected_fields():
    league = general.fetch_current_leagues()[0]
    assert "name" in league
    assert "url" in league
    assert "displayName" in league
    assert "hardcore" in league
    assert "indexed" in league


def test_current_temporary_league_is_correct():
    assert general.fetch_current_temporary_league()["name"] == CURRENT_LEAGUE
