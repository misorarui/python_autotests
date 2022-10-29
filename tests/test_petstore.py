import importlib
import requests
import pytest

petId = 102838
URL = 'https://petstore.swagger.io/v2'
response_first_pet = requests.get(f'{URL}/pet/{petId}')


def test_statuscode():
    assert response_first_pet.status_code == 200

def test_response_name():
    assert response_first_pet.json()['name'] == 'Masha'