import requests


def test_hello_world():
    r = requests.get('http://localhost:5002')
    assert r.text == 'hello world!'
