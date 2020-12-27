import config
from pymongo.mongo_client import MongoClient


class MongoConnection:
    def __init__(self):
        self.connection_string = config.MONGODB_URI
        connect_timeout = config.MONGO_TIMEOUT * 1000
        self.client = MongoClient(
            self.connection_string,
            serverSelectionTimeoutMS=connect_timeout,
            authSource="admin"
        )
        self._db = config.MONGODB_NAME

    @property
    def db(self):
        return self.client[self._db]

    def set_db_name(self, db_name):
        self._db = db_name
