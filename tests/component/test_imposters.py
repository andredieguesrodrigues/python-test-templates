import requests
import json

def test_simple_get_component_test_equals_200():
    # Arrange
    # As example, add some body and headers for the request
    body = {
        "id": "001",
        "name": "test"
    }

    headers = {
        'Accept': '*/*',
        'User-Agent': 'request'
    }

    # Act
    # Make a request passing the correct url, endpoint, body and headers
    response = requests.get(URL + "/endpoint", json=body, headers=headers)
    json_object = json.loads(response)

    # Assert
    # Check the status code and message not empty
    assert response.status_code == 200
    assert json_object["message"] == ""
    assert json_object["code"] == ""

