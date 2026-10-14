import pytest
import requests
from main import get_poke
from unittest.mock import patch

@patch("main.requests.get")
def test_get_poke_success(mock_get):
    mock_response = mock_get.return_value
    mock_response.json.return_value = {
        "name" : "pikachu",
        "id" : 25
    }
    mock_response.raise_for_status.return_value = None

    result = get_poke("pikachu")

    assert result["name"] == "pikachu"
    assert result["id"] == 25
    mock_get.assert_called_once_with("https://pokeapi.co/api/v2/pokemon/pikachu")



@patch("main.requests.get")
def test_get_poke_failure(mock_get):

    mock_get.side_effect = requests.RequestException("API is down")
    failureResult = get_poke("not-a-real-pokemon")

    assert failureResult is None

