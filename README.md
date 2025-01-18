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

## Docker
To build Dockerfile locally use following commands:
```shell
docker build . -t [image-name]:[tag] -f /path/to/Dockerfile
```
```shell
docker run -d tag
```
then open a browser and navigate to http://localhost:8000. If it opens "Hello world", then it works.

## Workflows
There are two workflows in the project. One should trigger on pull request and another one on merge. There is no option 
for triggering on push, cause it may cost a lot of resources.

To run ***fastapi_merge.yml*** workflow, a pull request should be made to the main branch and merged to GitHub. 
It will trigger the pipeline and can be seen in GitHub -> Actions tab. The workflow includes the following checks:
SonarCloud, Snyk, Trivy. It also builds the Docker image and push it to DockerHub.

To run ***fastapi_pr.yml*** pipeline, a pull request should be made to the main branch to GitHub. 
It will trigger the pipeline and can be seen in GitHub -> Actions tab. The workflow includes the following checks:
GitLeaks, EditConfig, Python PyLint, Python Black, MarkdownLint CLI, Unit tests.
