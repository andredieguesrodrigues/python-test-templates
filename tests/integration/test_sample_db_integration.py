
import pymongo
from pymongo.errors import ServerSelectionTimeoutError
import pytest

def test_mongodb_integration_status_code_equals_200():

    connected = True

    client = pymongo.MongoClient() # Add MONGO URL here

    try:
       client.server_info()
    except ServerSelectionTimeoutError:
       connected = False

    assert connected is True
