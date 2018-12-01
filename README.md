# flask_template

[![Build Status](https://travis-ci.org/ricardochaves/flask_template.svg?branch=master)](https://travis-ci.org/ricardochaves/flask_template) [![Coverage Status](https://coveralls.io/repos/github/ricardochaves/flask_template/badge.svg?branch=master)](https://coveralls.io/github/ricardochaves/flask_template?branch=master) [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black) [![Maintainability](https://api.codeclimate.com/v1/badges/cf419e1537019ed23b51/maintainability)](https://codeclimate.com/github/ricardochaves/flask_template/maintainability) [![Updates](https://pyup.io/repos/github/ricardochaves/flask_template/shield.svg)](https://pyup.io/repos/github/ricardochaves/flask_template/) [![Python 3](https://pyup.io/repos/github/ricardochaves/flask_template/python-3-shield.svg)](https://pyup.io/repos/github/ricardochaves/flask_template/) [![Codacy Badge](https://api.codacy.com/project/badge/Grade/3affcb2f1dff44288c894d79fa3f0ac7)](https://www.codacy.com/app/ricardochaves/flask_template?utm_source=github.com&utm_medium=referral&utm_content=ricardochaves/flask_template&utm_campaign=Badge_Grade)
[![GitHub](https://img.shields.io/github/license/mashape/apistatus.svg)](https://github.com/ricardochaves/flask_template/blob/master/LICENSE)

---

A Flask API base template

## Env file

Create a `.env` fila on project root, see [`.exemple.env`](https://github.com/ricardochaves/flask_template/blob/master/.exemple.env):

```INI
# FLASK
FLASK_APP=app.py
PORT=5005
DEBUG=True
LOGGIN_LEVEL=DEBUG

# Docker
PYTHONUNBUFFERED=1
```

## Lint

The project already has some lints set up

### Black

The project use [black](https://github.com/ambv/black/) and has a pre commit to ensure the application whenever a commit happens. The configuration can be find in [`.pre-commit-config.yaml`](https://github.com/ricardochaves/flask_template/blob/master/.pre-commit-config.yaml). More information [here](https://github.com/ambv/black/#version-control-integration).

The black configuration can be find in [`pyproject.toml`](https://github.com/ricardochaves/flask_template/blob/master/pyproject.toml)

### Pylint

The configuration for Pylint can be found in [`pylintrc`](https://github.com/ricardochaves/flask_template/blob/master/.pylintrc).

### Pep8 and Flake8

The configuration can be found in [`setup.cfg`](https://github.com/ricardochaves/flask_template/blob/master/setup.cfg)

## Test

To run the tests just run `tox`.

Or run with docker `docker-compose run --rm web_test`

The tox configuration can be found in [`tox.ini`](https://github.com/ricardochaves/flask_template/blob/master/tox.ini)

## VsCode

If you use [VSCode](https://code.visualstudio.com/), this is a sugestion to `settings.json`

```json
{
  "python.pythonPath": ".venv/bin/python",
  "files.exclude": {
    "**/.git": true,
    "**/__pycache__": true,
    "**/*.pyc": true
  },
  "editor.formatOnSave": true,
  "python.formatting.provider": "black",
  "python.formatting.autopep8Args": ["--max-line-length=120"],
  "python.formatting.blackArgs": ["--line-length=120"],
  "python.linting.flake8Enabled": true,
  "python.linting.pylintArgs": ["--load-plugins pylint_flask"],
  "python.sortImports.args": ["-sl", "-l 120"],
  "editor.codeActionsOnSave": {
    "source.organizeImports": true
  }
}
```

## Routes

[Variable Rules](http://flask.pocoo.org/docs/1.0/quickstart/#variable-rules)
