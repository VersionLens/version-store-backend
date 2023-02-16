import strawberry
from strawberry import auto
from typing import List
from . import models


@strawberry.django.type(models.Product)
class Product:
    id: auto
    name: auto
    price: auto
    image: auto


@strawberry.django.type(models.BasketItem)
class BasketItem:
    id: auto
    product: Product
    quantity: auto


@strawberry.django.type(models.Basket)
class Basket:
    id: auto
    items: List[BasketItem]

    @strawberry.django.field
    def items(self, info) -> List[BasketItem]:
        return models.BasketItem.objects.filter(basket=self)
