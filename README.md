# flask_template

[![Build Status](https://travis-ci.org/ricardochaves/flask_template.svg?branch=master)](https://travis-ci.org/ricardochaves/flask_template) [![Coverage Status](https://coveralls.io/repos/github/ricardochaves/flask_template/badge.svg?branch=master)](https://coveralls.io/github/ricardochaves/flask_template?branch=master) [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black) [![Maintainability](https://api.codeclimate.com/v1/badges/cf419e1537019ed23b51/maintainability)](https://codeclimate.com/github/ricardochaves/flask_template/maintainability) [![Updates](https://pyup.io/repos/github/ricardochaves/flask_template/shield.svg)](https://pyup.io/repos/github/ricardochaves/flask_template/) [![Python 3](https://pyup.io/repos/github/ricardochaves/flask_template/python-3-shield.svg)](https://pyup.io/repos/github/ricardochaves/flask_template/) [![Codacy Badge](https://api.codacy.com/project/badge/Grade/3affcb2f1dff44288c894d79fa3f0ac7)](https://www.codacy.com/app/ricardochaves/flask_template?utm_source=github.com&utm_medium=referral&utm_content=ricardochaves/flask_template&utm_campaign=Badge_Grade)
[![GitHub](https://img.shields.io/github/license/mashape/apistatus.svg)](https://github.com/ricardochaves/flask_template/blob/master/LICENSE)

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
