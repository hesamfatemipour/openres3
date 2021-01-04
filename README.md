### OpenreS3

#### will validate your bucket names
it's an attempt to validate users requested bucket name a step before sending the request to
the S3 service, uses openresty and lua to redirect requests to middleware and python and
mongo_db to validate the name.


- how to run:

```
python dependencies: pip3 install -r requirements.pip
lua dependencies: sudo luarocks install luasocket lua-cjson
```

```
step one: you need a virtualenv to install dependencies
step two: python3 middleware.py 
```

- to run test:
```
python3 -m unittest discover -vs tests
```

- run with docker:
```
docker-compose -f docker-compose.yml build
docker-compose -f docker-compose.yml up -d
```

TODO:
- unittest for lua module with : http://olivinelabs.com/busted
- after reviewing some libraries it's not recommended to use lua socket, it is more safe to use:
https://github.com/openresty/lua-nginx-module/blob/master/README.markdown#ngxsockettcp
  
- define a prefix for lua module in openresty
- log aggregation in nginx: https://github.com/mtourne/nginx_log_by_lua