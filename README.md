# Template básico de código para início de um projeto de GEN AI


## Informações básicas sobre o template

O template consiste em uma arquitetura básica onde dentro do main.py, há 1 api's que pode ser usada passando alguma informação via request. Vale ressaltar que esse payload via api é opcional, podendo ter outra solução dependendo da solução proposta.

Dentro do use-case, é onde o prompt precisará ser montado, e após essa montagem, se comunicar via sdk com o gemini que irá gerar a resposta ou retornar algum erro.

![exercicio drawio (1)](https://github.com/citggp-gp-labs/python-genai-project-template/assets/126102622/e6909ddf-445e-4987-8c8c-e656c5c2f06f)

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
