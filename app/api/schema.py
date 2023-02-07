import strawberry
from enum import Enum


@strawberry.enum
class State(Enum):
    ALABAMA = "AL"
    ALASKA = "AK"
    ARIZONA = "AZ"
    # Add more states


@strawberry.type
class Address:
    number: int
    street: str
    city: str
    state: State

    class Meta:
        name = "Address"


@strawberry.type
class Person:
    email: str
    name: str
    address: Address
