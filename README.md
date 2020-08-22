[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

# [OpeningHours](https://woltchallenge.app) API

This is...

## See it in action

1) Use cURL to send a POST request to the API
    ```
    curl -X POST http://woltchallenge.app/api/v1/get_hours_for_humans -H "Content-Type: application/json" -d '{"monday": [], "tuesday": [ { "type": "open", "value": 36000 }, { "type": "close", "value": 64800 } ], "wednesday": [], "thursday": [ { "type": "open", "value": 36000 }, { "type": "close", "value": 64800 } ], "friday": [ { "type": "open", "value": 36000 } ], "saturday": [ { "type": "close", "value": 3600 }, { "type": "open", "value": 36000 } ], "sunday": [ { "type": "close", "value": 3600 }, { "type": "open", "value": 43200 }, { "type": "close", "value": 75600 } ] }'
    ```
2) Or if running locally using `flask run` you can use file as the data
    ```
    (venv) user@machine OpeningHours % flask run
    (venv) user@machine OpeningHours % curl -i -X POST http://127.0.0.1:5000/api/v1/get_hours_for_humans -H "Content-Type: application/json" --data-binary "@tests/resources/input.json"
    ```

## What would I change about the data model

asdf

## Prerequisites

1) Install necessary software tools. For OS X, this is:
    ```
    brew install kubernetes-cli
    brew install kustomize
    brew install skaffold
    brew install terraform
    
    # Docker Desktop
    https://docs.docker.com/docker-for-mac/install/
   
    # Git
    https://git-scm.com/book/en/v2/Getting-Started-Installing-Git
    ```

## Setup

1) Clone this repo
    ```
    git clone https://github.com/m-tanner/OpeningHours.git
    ```
   
2) Create a virtual environment for the project
    ```
    user@machine OpeningHours % virtualenv venv
    
    # and activate it
    source venv/bin/activate
    ```

3) Install the project's requirements
    ```
    (venv) user@machine OpeningHours % pip install -r requirements.txt
    ```

4) Setup your `bash_profile`, `bashrc`, or `zshrc`
    ```
    export GOOGLE_APPLICATION_CREDENTIALS="$HOME/.gcloud/<CREDS>.json"
    export TF_VAR_GOOGLE_APPLICATION_CREDENTIALS="$HOME/.gcloud/<CREDS>.json"
    export CLOUD_PROVIDER="gcloud"
    export GCLOUD_PROJECT=<PROJECT NAME>
    
    # This is for flask and would need to change if the project structure changes
    export FLASK_CONFIG=dev
    export FLASK_ENV=developement
    export FLASK_DEBUG=1
    export FLASK_APP="src/app/app.py"
    export FLASK_SECRET_KEY=<A SECRET KEY>
    ```
   
5) Ensure that you can get the tests to pass
    ```
    (venv) user@machine OpeningHours % flask test
    ```

8) Setup kube config file
    ```
    apiVersion: v1
    clusters:
    - cluster:
        certificate-authority-data: <REDACTED>
        server: https://kubernetes.docker.internal:6443
      name: docker-desktop
    - cluster:
        certificate-authority-data: <REDACTED>
        server: https://XX.XXX.XXX.XX
      name: <NAME OF REMOTE CLUSTER>
    contexts:
    - context:
        cluster: docker-desktop
        namespace: development
        user: docker-desktop
      name: docker-desktop
    - context:
        cluster: <NAME OF REMOTE CLUSTER>
        namespace: production
        user: <NAME OF REMOTE CLUSTER>
      name: production
    - context:
        cluster: <NAME OF REMOTE CLUSTER>
        namespace: staging
        user: <NAME OF REMOTE CLUSTER>
      name: staging
    current-context: <set this>
    kind: Config
    preferences: {}
    users:
    - name: docker-desktop
      user:
        client-certificate-data: <REDACTED>
        client-key-data: <REDACTED>
    - name: gke_four-track-friday-2_us-west1-a_cluster-2
      user:
        auth-provider:
          config:
            access-token: <REDACTED>
            cmd-args: config config-helper --format=json
            cmd-path: /path/to/google-cloud-sdk/bin/gcloud
            expiry: <REDACTED>
            expiry-key: '{.credential.token_expiry}'
            token-key: '{.credential.access_token}'
          name: gcp
    ```

6) Start Kubernetes locally
    ```
    # this example uses docker-desktop instead of minikube
    # follow instructions here
    # ensure that, under Resources > File Sharing, you've mounted $HOME
    https://docs.docker.com/docker-for-mac/kubernetes/
    
    # should you prefer minikube, use 
    minikube start --driver hyperkit --kubernetes-version v1.16.12 --addons ingress --mount-string "$HOME:$HOME" --mount
    ```

7) Setup Kubernetes locally
    ```
    # make the namespace you'll use for the particular environment
    user@machine OpeningHours % kubectl apply -f src/k8s/dev/namespace.yml
   
    # set kubectl to use that namespace
    user@machine OpeningHours % kubectl config set-context --current --namespace=development
    
    # https://kubernetes.io/docs/tasks/access-application-cluster/web-ui-dashboard/
    user@machine OpeningHours % kubectl apply -f https://raw.githubusercontent.com/kubernetes/dashboard/v2.0.0/aio/deploy/recommended.yaml
    
    # in a free terminal tab
    kubectl proxy
    # would have to do this to actually connect since minikube isn't handling auth
    https://github.com/kubernetes/dashboard/blob/master/docs/user/access-control/creating-sample-user.md
    
    # https://kubernetes.github.io/ingress-nginx/deploy/#docker-for-mac
    user@machine OpeningHours % kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/controller-v0.34.1/deploy/static/provider/cloud/deploy.yaml
    ```
   
8) Manually setup some things that Skaffold can't do
    ```
    # create that the appropriate secret
    # after manually filling in secrets
    # never commit secrets!
    user@machine OpeningHours % kubectl apply -f src/k8s/<dev, stg, prod>/secret.yml
   
    # to generate secret values, which must be encoded in base64
    user@machine OpeningHours % echo -n "value to convert" | base64
   
    # fill in a path to credentials in src/k8s/dev/patch.yml
   
    # for cloud deployments that will receive real traffic
    # create a certificate for https connections
    user@machine OpeningHours % kubectl apply -f src/k8s/<dev, stg, prod>/certificate.yml
    ```
    
9) You're ready to deploy the app! Jump straight to the Skaffold section for maximum velocity!

## Testing and Linting
1) Simply run the following commands in your favorite terminal:
    ```
    # pylint
    (venv) user@machine OpeningHours % pylint -j 0 src/ --errors-only
    (venv) user@machine OpeningHours % pylint -j 0 tests/ --errors-only
   
    # flake8
    (venv) user@machine OpeningHours % flake8 src/
    (venv) user@machine OpeningHours % flake8 tests/
   
    # black
    (venv) user@machine OpeningHours % black --check src/
    (venv) user@machine OpeningHours % black --check tests/
    
    # pytype
    (venv) user@machine OpeningHours % pytype
   
    # pytest with coverage
    (venv) user@machine OpeningHours % coverage run --source=src/ -m pytest tests/ -s -v --disable-pytest-warnings
   
    # generate coverage report
    (venv) user@machine OpeningHours % coverage report --omit='src/app/*' -m --fail-under=100
    ```
   
## Building
1) To build locally, tag, and push to a remote container registry
    ```
    # from the project root directory
    (venv) user@machine OpeningHours % docker build -t oh_web_app -f src/docker/Dockerfile .
   
    (venv) user@machine OpeningHours % docker run --name oh -p 8080:8080 -e <all the env vars described in the bash profile section> -v $GOOGLE_APPLICATION_CREDENTIALS:/path/to/application/credentials -d oh_web_app:latest
   
    (venv) user@machine OpeningHours % docker tag oh_web_app:latest gcr.io/<CLOUD_PROJECT_NAME>/oh_web_app
   
    (venv) user@machine OpeningHours % docker push gcr.io/<CLOUD_PROJECT_NAME>/oh_web_app
    ``` 

## Deployment

1) Simply run the following command in your favorite terminal
    ```
    (venv) user@machine OpeningHours % run_svc
    # This entry point is provided by the setup.py
    ```

2) Deploy to Kubernetes locally
    ```
    1) kubectl config use-context docker-desktop
    2) kubectl config set-context --current --namespace=development
    3) kubectl apply -f src/k8s/dev/secret.yml (or ensure it's already created)
    4) skaffold run
        # trailing the logs can be helpful when troubleshooting
        # skaffold run --trail
    ```

3) Deploy to Kubernetes in the cloud
    ```
    1) kubectl config use-context gke...
    2) kubectl config set-context --current --namespace=<staging or production>
    3) kubectl apply -f src/k8s/<stg or prod>/secret.yml (or ensure it's already created)
    4) kubectl apply -f src/k8s/<stg or prod>/certificate.yml (or ensure it's already created)
    3) skaffold run
        # trailing the logs can be helpful when troubleshooting
        # skaffold run --trail
    ```

## Use Skaffold to Build, Test, and Deploy
1) Use the docker-desktop context from .kube/config
    ```
    # with docker-desktop as the example
    kubectl config use-context docker-desktop
    ```
2) Set the proper namespace
    ```
    # with development as the example
    kubectl config set-context --current --namespace=development
    ```
3) `skaffold run` or `skaffold run --trail`, which can be more helpful when troubleshooting

## Related Infrastructure
1) Separately create and manage a Google Cloud Platform Kubernetes Cluster
2) Separately create and manage a Google Cloud Bucket to store Terraform state
3) Separately create and manage a Google Cloud Service Account to use for resource creation
4) Separately acquire a domain through Google Domains and verify ownership
4) Add your Google Cloud Platform service account of choice as a verified owner
3) Run Terraform
    ```
    # initialize terraform if you haven't
    (venv) user@machine terraform % terraform init
    
    # always plan first!
    (venv) user@machine terraform % terraform plan
   
    # then apply, check again before typing "yes"
    (venv) user@machine terraform % terraform apply
   
    # don't forget to format Terraform properly after making changes
    (venv) user@machine terraform % terraform fmt
    ```
4) Once the network infrastructure is up, point your domain registrar to the DNS NS data
5) To get Google Analytics, create a property and get the gtag.js