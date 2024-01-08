import requests
import pytest

URL = 'https://jsonplaceholder.typicode.com/posts/'


def test_get_request():
    response = requests.get(f'{URL}1')
    print('LOL')
    assert response.status_code == 200
    assert response.json()['userId'] == 1


def test_post_request():
    payload = {
        'title': 'foo',
        'body': 'bar',
        'userId': 1
    }
    response = requests.post(URL, json=payload)
    assert response.status_code == 201
    assert response.json()['userId'] == 1
    assert response.json()['title'] == 'foo'


def test_put_request():
    payload = {
        'id': 1,
        'title': 'foo',
        'body': 'bar',
        'userId': 1
    }
    response = requests.put(f'{URL}1', json=payload)
    assert response.status_code == 200
    assert response.json()['title'] == 'foo'
    assert response.json()['body'] == 'bar'


def test_delete_request():
    response = requests.delete(f'{URL}1')
    assert response.status_code == 200
