from http import client
from urllib import response
from fastapi.testclient import TestClient
import pytest
from main import app
client = TestClient(app)


# Test 1
def test_pokemon_battle_win(mocker):
    mocker.patch(
        "app.utils.pokeapi.battle_compare_stats",
        return_value = 1
    )
    
    first_api_id=1
    second_api_id=4

    response = client.get(f"/pokemons/battle?first_api_id={first_api_id}&second_api_id={second_api_id}")
    assert response.status_code == 200
    assert response.json() == {"winner": "bulbasaur"}