import config
from pymongo.mongo_client import MongoClient


class Mongo:

    @staticmethod
    def connect():  # returns a mongo connection
        return MongoClient(host=[config.MONGO_HOST],
                           document_class=dict,
                           tz_aware=False,
                           connect=True)

    @staticmethod
    def get_users_valid_prefixes(user):
        # query users saved prefixes
        pass
