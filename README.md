# Template básico de código para início de um projeto de GEN AI

## Iniciar ambiente local

Dentro de uma virtual env em python, rodar os seguintes comandos

Criando uma virtual env
```sh
python -m venv venv
source venv/bin/activate
```

Instalando as dependências básicas do projeto

```sh
pip install google-cloud-logging
pip install python-dotenv
pip install google-cloud-aiplatform
pip install flask
pip install gunicorn
```

Gere um arquivo de requirements com os comandos

```sh
pip freeze > requirements.txt
```

Rodar a aplicação em um servidor local.

```sh
flask --app main run
```
ou

```sh
gunicorn --bind 127.0.0.1:8080 main:app
```

## Deploy do projeto

Deploy do projeto via comando gcloud.

```sh
gcloud run {deploy cloud-run-name} \
    --project={project_id} \
    --source=. \
    --port=80 \
    --region={location} \
    --no-allow-unauthenticated \
    --service-account={service_account} \
    --concurrency=80 \
    --cpu=1 \
    --memory=512Mi \
    --no-cpu-throttling \
    --max-instances=5 \
    --min-instances=1 \
    --update-env-vars=PROJECT_ID="{project_id}",PROJECT_LOCATION="{location}",DEFAULT_MODEL_VERSION="{gemini_model}",BUCKET_NAME="{bucket_name}",BUCKET_FILE="{csv_file}",LOG_LEVEL="DEBUG" \
    --ingress=internal-and-cloud-load-balancing
```

## Teste de chamada via curl

```sh
curl -H "Content-Type: application/json" -H "Authorization: Bearer $(gcloud auth print-identity-token)" "http://34.128.131.116"
```

## Informações extra

Não é possível acessar diretamente o endpoint do cloud run, pois não há ingress público. Para acessar o serviço foi criado [Load Balance](https://console.cloud.google.com/net-services/loadbalancing/details/httpAdvanced/app-vertex-ai?project=poc-vibrancy-vertexai) disponível no host [http://34.128.131.116](http://34.128.131.116).
