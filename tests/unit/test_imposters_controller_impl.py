import json

def test_simple_unit_test_equals_201():

    # Arrange
    # As example, add some file as start point (setup) for the tests

    with open('') as file:
        file_data = json.load(file)

    # Act
    # Call your method to be tested passing the initial file (or variables, etc)
    msg, error = call_method_to_be_tested(file_data)

    # Assert
    # Check the status code and message not empty
    assert error == 201
    assert msg != ""

