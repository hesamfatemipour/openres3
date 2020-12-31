import os

DEBUG = False

# mongo
MONGODB_URI = os.environ.get(
    'MONGODB_URI',
    'mongodb://openresty:test123@10.0.1.8:27017'
)
MONGODB_NAME = 'openres3'
MONGODB_TESTDB_NAME = 'openres3'
MONGO_TIMEOUT = 60
