import pytest
from fastapi.testclient import TestClient
from main import app


@pytest.fixture()
def client():
    return TestClient(app)


headers = {"Content-Type": "application/json"}


def test_person_query(client: TestClient):
    queries = [
        {
            "query": """
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
      """,
            "expected_status_code": 200,
            "expected_response": {
                "data": {
                    "person": {
                        "email": "test@example.com",
                        "name": "John Doe",
                        "address": {
                            "number": 123,
                            "street": "Main St",
                            "city": "New York",
                            "state": "ARIZONA",
                        },
                    }
                }
            },
        },
    ]

    for query in queries:
        response = client.post(
            "/graphql", headers=headers, json={"query": query["query"]}
        )

        assert response.status_code == 200
        assert "data" in response.json()
        assert "person" in response.json()["data"]
        assert "email" in response.json()["data"]["person"]
        assert "name" in response.json()["data"]["person"]
        assert "address" in response.json()["data"]["person"]
        assert "number" in response.json()["data"]["person"]["address"]
        assert "street" in response.json()["data"]["person"]["address"]
        assert "city" in response.json()["data"]["person"]["address"]
        assert "state" in response.json()["data"]["person"]["address"]
        assert response.status_code == query["expected_status_code"]
        assert response.json() == query["expected_response"]
