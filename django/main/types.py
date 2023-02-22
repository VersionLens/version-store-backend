import strawberry
from strawberry import auto
from typing import List
from . import models


@strawberry.django.type(models.Category)
class Category:
    id: auto
    name: auto
    products: List["Product"]


@strawberry.django.type(models.Product)
class Product:
    id: auto
    name: auto
    price: auto
    image: auto
    category: Category


@strawberry.django.type(models.BasketItem)
class BasketItem:
    id: auto
    product: Product


@strawberry.django.type(models.Basket)
class Basket:
    id: auto
    items: List[BasketItem]

    @strawberry.django.field
    def items(self, info) -> List[BasketItem]:
        return models.BasketItem.objects.filter(basket=self)
