import pypoeninja.request_utils as request

TEST_API_URL = "https://jsonplaceholder.typicode.com/todos/1"
EXPECTED_RESPONSE = {
    "userId": 1,
    "id": 1,
    "title": "delectus aut autem",
    "completed": False,
}


def test_cache_enabling():
    # Cache should be enabled by default
    assert request.is_cache_enabled()
    request.disable_cache()
    assert not request.is_cache_enabled()
    request.enable_cache()
    assert request.is_cache_enabled()


def test_getting_json():
    json = request.get_json(TEST_API_URL)
    assert json == EXPECTED_RESPONSE
