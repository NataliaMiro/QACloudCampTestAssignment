import unittest
import requests
import json

class TestStringMethods(unittest.TestCase):
    # Проверка с заполненными параметрами
    def test_create_post(self):
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

        self.assertTrue(response.status_code == 201)
        self.assertTrue(response.json()['title'] == 'foo')
        self.assertTrue(response.json()['body'] == 'bar')
        self.assertTrue(response.json()['userId'] == 1)


    # В запросе отсутствует тело
    def test_create_post_when_empty_body(self):
        url = 'https://jsonplaceholder.typicode.com/posts'
        headers = {
            'Content-type': 'application/json; charset=UTF-8',
        }

        response = requests.post(url, headers=headers)

        self.assertTrue(response.status_code != 201)

    # Получение ресурса с существующим id
    def test_get_resourse(self):
        url = 'https://jsonplaceholder.typicode.com/posts/1'
        response = requests.get(url)
        self.assertTrue(response.status_code == 200)


    # Получение ресурса с несуществующим id
    def test_get_resourse(self):
        url = 'https://jsonplaceholder.typicode.com/posts/10000'
        response = requests.get(url)
        self.assertTrue(response.status_code == 404)

    # Удаление ресурса с существующим id
    def test_delete_resourse(self):
        url = 'https://jsonplaceholder.typicode.com/posts/1'
        response = requests.delete(url)
        self.assertTrue(response.status_code == 200)

    # Удаление ресурса с несуществующим id
    def test_delete_resourse_when_id_is_not_correct(self):
        url = 'https://jsonplaceholder.typicode.com/posts/a'
        response = requests.delete(url)
        self.assertTrue(response.status_code != 200)

if __name__ == '__main__':
    unittest.main()