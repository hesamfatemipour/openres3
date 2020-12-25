from flask import Flask, request
from http import HTTPStatus

app = Flask(__name__)


def mongo_query(**kwargs):
    pass


def validate(bucket_name: str, username: str) -> bool:
    pass


@app.route('/user/<username>/')
def validate_bucket_name(username):
    bucket_name = request.args.get("bucket_name")
    if not bucket_name:
        return 'No bucket name provided', HTTPStatus.BAD_REQUEST
    can_create = validate(bucket_name=bucket_name, username=username)
    if can_create:
        return 'valid bucket name', HTTPStatus.OK
    else:
        return 'invalid bucket name'


if __name__ == '__main__':
    app.run(threaded=True, host='0.0.0.0')
