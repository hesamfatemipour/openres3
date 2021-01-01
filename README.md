### OpenreS3

#### will validate your bucket names

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
docker-compose -f docker-compose.yml up -d
```