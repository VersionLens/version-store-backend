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
