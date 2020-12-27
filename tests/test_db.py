from unittest import TestCase
from unittest import mock
from db.mongo import MongoConnection
from middleware import query_mongo


class TestValidateBucketName(TestCase):
    def __init__(self, method_name) -> None:
        super().__init__(method_name)
        self.mongo = MongoConnection()
        self.test_db_name = 'test_db'

    def seed_data(self):
        self.mongo.set_db_name(self.test_db_name)
        data = [{
            "user_id": 1,
            "prefixes": ['test', 'arvan']
        }]
        self.mongo.db.prefixes.insert_many(data)

    def tear_down(self) -> None:
        self.mongo.client.drop_database(self.test_db_name)

    @mock.patch('middleware.MongoConnection')
    def test_mongo_client_should_return_users_prefixes(self, mocked_connection):
        mocked_connection.return_value = self.mongo

        # insert data in sql
        self.seed_data()
        document = query_mongo(user_id=1)

        # check data validity in mongo
        self.assertEqual(document['user_id'], 1)
        self.assertEqual(document['prefixes'], ['test', 'arvan'])

        # delete test data
        self.tear_down()
