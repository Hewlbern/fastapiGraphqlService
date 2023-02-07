# Example FastAPI and GraphQL

This project showcases a microservice built with FastAPI and Strawberry-GraphQL.

To run the service in a Docker container, use the following command:


## Running the Service


### With Docker

To run the service in a Docker container, use the following command:

```sh
docker-compose up web
```

If you'd like to run the service with a clean slate, use the following commands:

```sh
docker-compose down
docker-compose rm -f
docker-compose up --force-recreate --build  --abort-on-container-exit web
```

## Testing the Service

### With Docker
To test the service in a Docker container, use the following command:

```sh
docker-compose up tests
```

If you'd like to test the service with a clean slate, use the following commands:

```sh
docker-compose down
docker-compose rm -f
docker-compose up --force-recreate --build  --abort-on-container-exit tests
```


### Using a GraphQL Client

You can use a GraphQL client like Insomnia or GraphQL Playground to test the API; alternatively head towards http://0.0.0.0:8008/graphql .

Here's an example GraphQL query you can run:

```
query {
  person {
    email
    name
    address {
      number
      street
      city
      state
    }
  }
}
```

### Tools and Technologies

- FastAPI - A modern, fast (high-performance) web framework for building APIs with Python 3.7+ based on standard Python type hints.

- Strawberry-GraphQL - A graphql library for Python, using the strawberry type system.
