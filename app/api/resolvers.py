import strawberry
from api.schema import Address, Person, State


@strawberry.type
class Query:
    @strawberry.field
    def person() -> Person:
        return Person(
            email="test@example.com",
            name="John Doe",
            address=Address(
                number=123, street="Main St", city="New York", state=State.ARIZONA
            ),
        )
