# FastAPI starter

A boilerplate application to start developing microservices in Python.

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

Two workflows are available in the project. One should trigger on pull request and another one on merge. A workflow, 
which triggers on push is not created, as it may cost a lot of resources and go over the budget.

To run ***fastapi_merge.yml*** workflow, a pull request should be made to the main branch and merged to GitHub. 
It will trigger the pipeline and can be seen in GitHub -> Actions tab. The workflow includes the following checks:
SonarCloud, Snyk, Trivy. It also builds the Docker image and push it to DockerHub.

To run ***fastapi_pr.yml*** pipeline, a pull request should be made to the main branch to GitHub. 
It will trigger the pipeline and can be seen in GitHub -> Actions tab. The workflow includes the following checks:
GitLeaks, EditConfig, Python PyLint, Python Black, MarkdownLint CLI, Unit tests.

## ArgoCD

Prerequisites: 
- installed ***kubectl*** command-line tool
- installed ***Docker Desktop*** or other external cluster 

### Install ArgoCD

```shell
kubectl create namespace argocd
```

This will create a new namespace server, where Argo CD services and application resources will live.
```shell
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
```

### Download ArgoCD on Macbook

```shell
brew install argocd
```
Port Forwarding
```shell
kubectl port-forward svc/argocd-server -n argocd 8080:443
```

### Login via UI

Navigate to a browser and open *https://localhost:8080* - the certificate will be invalid, though open it. 
The username is *admin* and the temp password can be extracted with the command bellow, excluding the % symbol at the end.
```shell
kubectl -n argocd get secret argocd-initial-admin-secret -o jsonpath="{.data.password}" | base64 -d
```
Update the password:
```shell
argocd account update-password
```

### Create apps via UI

After logging in, click the '+ New App' button, give the app a name (at this example set 'app'), use the project 'default', 
and leave the sync policy as 'Manual'.
Connect the deployment repo to Argo CD by setting repository URL to the GitHub repo URL: 
https://github.com/boyanaboneva/devops-gitops, 
leave revision as 'HEAD', and set the path to the deployment folder name - in this case 'devops-service-deployment'.
For 'Destination' set cluster to:
https://kubernetes.default.svc 
and namespace to 'application'. Finally, click on the 'Create' button.

### Sync (Deploy) The Application

If it's Health status is 'Out of sync', then click on the 'Sync apps' button in the application page UI. A panel will be
opened and then, click on 'Synchronize' button.
You can see more details by clicking at the 'app' application.

## Kubernetes deployment

Deployments files are in another repo: https://github.com/boyanaboneva/devops-gitops

Create another namespace, e.g. 'application':
```shell
kubectl create namespace application
```

To create a config map with environment variables navigate to the file in the gitops repo via terminal:
```shell
kubectl apply -f env_fastapi_configmap.yml
```

Using terminal navigate to the kubernetes deployment folder in the gitops repo. Apply the 'deployment.yml' file in the
newly created namespace, e.g. 'application':
```shell
kubectl apply -f deployment.yml -n application
```
The response should look like this:
```shell
deployment.apps/fast-api-deployment created
```

To check everything is applied, get the pods of this namespace:
```shell
kubectl get pods -n application
```
The response should look like this:
```shell
NAME                                   READY   STATUS    RESTARTS   AGE
fast-api-deployment-66ff55bb64-cmkbl   1/1     Running   0          22s
```

Using terminal navigate to the kubernetes deployment folder in the gitops repo. Apply the 'service.yml' file in the
newly created namespace, e.g. 'application':
```shell
kubectl apply -f service.yml -n application
```
The response should look like this:
```shell
service/fastapi-service configured
```

## Software architecture diagram
![alt text](resources/software-architecture.png "architecture")