import strawberry
from strawberry.types import Info
from typing import List, Optional
from .types import Product, Basket, Category
from main.models import Product as ProductModel
from main.models import Basket as BasketModel
from main.models import BasketItem as BasketItemModel


@strawberry.type
class Query:
    products: List[Product] = strawberry.django.field()
    product: Product = strawberry.django.field()
    category: Category = strawberry.django.field()
    categories: List[Category] = strawberry.django.field()

    @strawberry.django.field
    def basket(self, info) -> Basket:
        return BasketModel.get()


@strawberry.type
class Mutation:
    @strawberry.mutation
    def add_to_basket(self, info, product_id: int) -> Basket:
        product = ProductModel.objects.get(pk=product_id)
        basket = BasketModel.get()
        BasketItemModel.objects.create(product=product, basket=basket)
        return basket

    @strawberry.mutation
    def remove_from_basket(self, info, item_id: int) -> Basket:
        item = BasketItemModel.objects.get(pk=item_id)
        item.delete()
        return BasketModel.get()


schema = strawberry.Schema(query=Query, mutation=Mutation)
