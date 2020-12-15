import pytest
import requests
import json

def test_valid_login():
    url = 'http://localhost:5000/login_data'
    data = {
        'correo': 'orlando.avilag@hotmail.com',
        'pass': 'LandoWolf10*'
    }

    response = requests.post(url, data = data)

    assert response.status_code == 200