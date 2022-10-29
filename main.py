import importlib
import requests
import pytest


response_first_pet = requests.post('https://petstore.swagger.io/v2/pet', json={
  "id": 102838,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "Asya",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
})

response_second_pet = requests.post('https://petstore.swagger.io/v2/pet', json={
  "id": 1028438,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "Kit",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
})

response_third_pet = requests.post('https://petstore.swagger.io/v2/pet', json={
  "id": 102223838,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "Pyos",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
})


print("Создаем трех питомцев:\nПервый питомец: ", response_first_pet.text, "\n", "Второй питомец: ", response_second_pet.text, "\n", "Третий питомец: ", response_third_pet.text, sep='')


response_first_pet = requests.put('https://petstore.swagger.io/v2/pet', json={
  "id": 102838,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "Masha",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
})

print("Сменили имя Асе на Машу:\n", response_first_pet.text)

petId = 102838

response_first_pet = requests.get(f'https://petstore.swagger.io/v2/pet/{petId}')

print("Ищем Машу:\n", response_first_pet.text)