# FastAPI starter
A boilerplate to start developing microservices in Python.

## Tests
To run the tests use following command:
```shell
pytest
```

To run the tests with coverage use following command:
```shell
pytest --cov=app --cov-report=term-missing
```

To build Dockerfile locally use following commands:
```shell
docker build . -t [tag] -f /path/to/Dockerfile/image-name
```
```shell
docker run -d tag
```
then open a browser and navigate to http://localhost:8000. If it opens "Hello world", then it works.
