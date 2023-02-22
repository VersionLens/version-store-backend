import strawberry
from strawberry import auto
from django.contrib.auth import get_user_model
from typing import List
from . import models

UserModel = get_user_model()


@strawberry.django.type(UserModel)
class User:
    id: auto
    username: auto


@strawberry.django.type(models.Review)
class Review:
    id: auto
    user: User
    product: auto
    comment: auto


@strawberry.django.type(models.Product)
class Product:
    id: auto
    name: auto
    price: auto
    image: auto
    reviews: List[Review]


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
