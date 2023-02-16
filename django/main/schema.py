import strawberry
from typing import List
from .types import Product, Basket
from main.models import Product as ProductModel
from main.models import Basket as BasketModel


@strawberry.type
class Query:
    products: List[Product] = strawberry.django.field()

    @strawberry.django.field
    def basket(self, info) -> Basket:
        return BasketModel.get()


schema = strawberry.Schema(query=Query)
