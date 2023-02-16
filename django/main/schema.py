import strawberry
from typing import List
from .types import Product
from main.models import Product as ProductModel

@strawberry.type
class Query:
    Products: List[Product] = strawberry.django.field()

schema = strawberry.Schema(query=Query)