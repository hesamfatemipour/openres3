import unittest
from unittest import TestCase

from middleware import validate_bucket_name_regex


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
