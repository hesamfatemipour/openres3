from flask import Flask, request
from http import HTTPStatus
from db.mongo import MongoConnection
import re

bucket_name_regex = re.compile(r'^[A-Za-z]{1,1}[A-Za-z0-9]{3,7}$')
app = Flask(__name__)


def query_mongo(user_id):
    client = MongoConnection()
    prefixes = client.db.prefixes.find_one({"user_id": user_id})
    return prefixes


def validate_bucket_name_regex(bucket_name):
    return True if bucket_name_regex.fullmatch(bucket_name) else False


def validate(bucket_name: str, user_id: int) -> bool:
    user_prefix = query_mongo(user_id=user_id)
    bucket_name_regex.fullmatch(bucket_name)
    if bucket_name.startswith(user_prefix['prefix']) and validate_bucket_name_regex(bucket_name):
        return True
    else:
        return False


@app.route('/user/<username>/')
def validate_bucket_name(user_id):
    bucket_name = request.args.get("bucket_name")
    if not bucket_name:
        return 'No bucket name provided', HTTPStatus.BAD_REQUEST
    can_create = validate(bucket_name=bucket_name, user_id=user_id)
    if can_create:
        return 'valid bucket name', HTTPStatus.OK
    else:
        return 'invalid bucket name'


if __name__ == '__main__':
    app.run(threaded=True, host='0.0.0.0')
