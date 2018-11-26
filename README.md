# flask_template

[![Build Status](https://travis-ci.org/ricardochaves/flask_template.svg?branch=master)](https://travis-ci.org/ricardochaves/flask_template) [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black) [![Maintainability](https://api.codeclimate.com/v1/badges/cf419e1537019ed23b51/maintainability)](https://codeclimate.com/github/ricardochaves/flask_template/maintainability)

---

A Flask API base template

## Env file

Create a `.env` fila on project root:

```
# FLASK
FLASK_APP=app.py
PORT=5005
DEBUG=True
LOGGIN_LEVEL=DEBUG

# Docker
PYTHONUNBUFFERED=1
```

## Lint

O projeto já tem alguns lints configurados

### Black

O rojeto usa [black](https://github.com/ambv/black/) e tem um pre commit para garantir a aplicação sempre que um commit acontecer. A configuração fica no arquivo `.pre-commit-config.yaml`. Mais informações [aqui](https://github.com/ambv/black/#version-control-integration).

## Test

Para rodar os testes basta executar `tox`.
