import json

from start_app import app


def test_index_returns_200():
    request, response = app.test_client.get('/')
    assert response.status == 200

def test_index_put_not_allowed():
    request, response = app.test_client.put('/')
    assert response.status == 405

def test_get_request_includes_data():
    params = {'key1': 'value1', 'key2': 'value2'}
    request, response = app.test_client.get('/', params=params)
    assert request.args.get('key1') == 'value1'

def test_post_json_request_includes_data():
    data = {'key1': 'value1', 'key2': 'value2'}
    request, response = app.test_client.post('/', data=json.dumps(data))
    assert request.json.get('key1') == 'value1'
