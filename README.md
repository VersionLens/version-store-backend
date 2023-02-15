# Django backend for Version Store (a demo project)

This backend is a Django server with GraphQL.

## Where's the frontend?

Check out [version-store-frontend](https://github.com/VersionLens/version-store-frontend) to get the frontend for this project.

## Prerequisites

-   Python 3.10
-   Poetry [installation guide](https://python-poetry.org/docs/#installation)

## Installation

Install dependences:

```
poetry install
```

Activate virtualenv

```
poetry shell
```

Migrate data

```
python django/manage.py migrate
```

## Run

Activate virtualenv

```
poetry shell
```

Run server

```
python django/manage.py runserver
```
