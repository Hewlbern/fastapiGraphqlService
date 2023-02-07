# Example FastAPI and Graphql
This is an example project that showcases a microservice built with FastAPI and Strawberry-GraphQL.

## Running

### In Docker

```sh
docker-compose up web
```

or to run cleanly (it takes longer):

```sh
docker-compose down
docker-compose rm -f
docker-compose up --force-recreate --build  --abort-on-container-exit web
```

## Testing

### In Docker

```sh
docker-compose up tests
```

or to run cleanly (it takes longer):

```sh
docker-compose down
docker-compose rm -f
docker-compose up --force-recreate --build  --abort-on-container-exit tests
```


### Client

You can use a GraphQL client like Insomnia or GraphQL Playground to test the API; alternatively head towards http://0.0.0.0:8008/graphql .

### Built With

- FastAPI - A modern, fast (high-performance) web framework for building APIs with Python 3.7+ based on standard Python type hints.
- Strawberry-GraphQL - A graphql library for Python, using the strawberry type system.
