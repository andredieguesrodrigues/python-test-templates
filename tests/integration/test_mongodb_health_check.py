
import pymongo

from pymongo.errors import ServerSelectionTimeoutError
""

def test_mongodb_availability_status_code_equals_200():

    connected = True

    client = pymongo.MongoClient() # Add MONGO URL here

    try:
        client.server_info()
    except ServerSelectionTimeoutError:
        connected = False

    assert connected is True
