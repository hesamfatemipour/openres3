from flask import Flask, request, jsonify
from http import HTTPStatus

import config
from db.mongo import MongoConnection
import re

app = Flask(__name__)

bucket_name_regex = re.compile(r'^[A-Za-z]{1,1}[A-Za-z0-9_]{3,12}$')


# the assumption based on the document is that prefixes are unique per user
# CRUD for prefixes is a prerequisites to this endpoint

def query_mongo(user_id):
    """ returns the prefixes for a provided user"""
    client = MongoConnection()
    prefixes = client.db.prefixes.find_one({"user_id": user_id})
    return prefixes


# validate users requested based on a regex
def validate_bucket_name_regex(bucket_name):
    return True if bucket_name_regex.fullmatch(bucket_name) else False


def validate(bucket_name: str, user_id: int):
    # query mongo to get users registered prefixes
    user_prefix = query_mongo(user_id=user_id)
    if not user_prefix:
        return False, 'user prefix not found'

    # step 1 validation of the provided bucket name
    bucket_name_regex.fullmatch(bucket_name)

    # main validation logic
    if bucket_name.startswith(user_prefix['prefixes']) and validate_bucket_name_regex(bucket_name):
        return True, 'user is allowed to create bucket'
    else:
        return False, 'user can not create the bucket with the requested name'


@app.route('/users/<user_id>', methods=['POST'])
def validate_bucket_name(user_id):
    """
    :param user_id:
    :return: checks the availability of a bucket name.
    """
    bucket_name = request.args.get("bucket_name")
    if not bucket_name:
        return jsonify({"cause": 'No bucket name provided', "status_code": HTTPStatus.BAD_REQUEST})

    can_create, cause = validate(bucket_name=bucket_name, user_id=user_id)  # returns True or False and cause

    if can_create:
        return jsonify({"cause": cause, "status_code": HTTPStatus.OK})
    else:
        return jsonify({"cause": cause, "status_code": HTTPStatus.BAD_REQUEST})


if __name__ == '__main__':
    app.run(threaded=True, host='0.0.0.0', debug=config.DEBUG)
    print(app.url_map)
