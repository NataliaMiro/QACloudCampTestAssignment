import requests
import json

# Проверка с заполненными параметрами
def test_create_post():
    url = 'https://jsonplaceholder.typicode.com/posts'

    body_content={
        'title': 'foo',
        'body': 'bar',
        'userId': 1
    }

    body_strcontent = json.dumps(body_content)
    body = body_strcontent
    headers = {
        'Content-type': 'application/json; charset=UTF-8',
    }

    response = requests.post(url, body, headers=headers)

    assert response.status_code == 201
    assert response.json()['title'] == 'foo'
    assert response.json()['body'] == 'bar'
    assert response.json()['userId'] == 1


# В запросе отсутствует тело
def test_create_post():
    url = 'https://jsonplaceholder.typicode.com/posts'
    headers = {
        'Content-type': 'application/json; charset=UTF-8',
    }

    response = requests.post(url, headers=headers)

    assert response.status_code != 201

# Получение ресурса с существующим id
def test_get_resourse():
    url = 'https://jsonplaceholder.typicode.com/posts/1'
    response = requests.get(url)
    assert response.status_code == 200


# Получение ресурса с несуществующим id
def test_get_resourse():
    url = 'https://jsonplaceholder.typicode.com/posts/10000'
    response = requests.get(url)
    assert response.status_code == 404

# Удаление ресурса с существующим id
def test_delete_resourse():
    url = 'https://jsonplaceholder.typicode.com/posts/1'
    response = requests.delete(url)
    assert response.status_code == 200

# Удаление ресурса с несуществующим id
def test_delete_resourse():
    url = 'https://jsonplaceholder.typicode.com/posts/a'
    response = requests.delete(url)
    assert response.status_code != 200