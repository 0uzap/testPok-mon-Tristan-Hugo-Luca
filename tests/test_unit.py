from http import client
from urllib import response
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
from fastapi import APIRouter,  Depends
from app.utils.utils import get_db
import pytest
from main import app
from app import actions
client = TestClient(app)

# Test 1 
# Check the get trainers by name endpoint
def test_get_trainer_by_name():
    trainer_name = 'Alexis'
    response = client.get(f"/trainers/by_name/{trainer_name}")
    assert response.status_code == 200 
    assert response.json()['id'] == 1