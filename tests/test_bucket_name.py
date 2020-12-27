from unittest import TestCase, mock

from db.mongo import MongoConnection
from middleware import validate_bucket_name_regex, validate


class TestValidateBucketName(TestCase):
    def __init__(self, method_name) -> None:
        super().__init__(method_name)

    def test_func_bucket_name_should_validate_bucket_names_with_given_regex(self):
        should_fail = ['آِروان', '44arvan', 'gitlabgitlabgitlab', 'باکت']
        for case in should_fail:
            self.assertEqual(validate_bucket_name_regex(case), False)

        should_pass = ['arvan', 'arvans3']
        for case in should_pass:
            self.assertEqual(validate_bucket_name_regex(case), True)


class TestBucketNameCreation(TestCase):
    def __init__(self, method_name) -> None:
        super().__init__(method_name)

        self.mongo = MongoConnection()
        self.test_db_name = 'test_db'

    def seed_data(self):
        self.mongo.set_db_name(self.test_db_name)
        data = [{
            "user_id": 1,
            "prefixes": 'test'
        }]
        self.mongo.db.prefixes.insert_many(data)

    def tear_down(self) -> None:
        self.mongo.client.drop_database(self.test_db_name)

    @mock.patch('middleware.MongoConnection')
    def test_bucket_name_creation_should_allow_users_to_create_buckets_with_valid_prefixes(self, mocked_connection):
        mocked_connection.return_value = self.mongo

        self.seed_data()

        bucket_name = 'test_gitlab'
        can_create, cause = validate(bucket_name=bucket_name, user_id=1)

        self.assertEqual(can_create, True)
        self.tear_down()
