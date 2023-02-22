from django.db import models as m
from django.utils.translation import gettext_lazy as _


class Product(m.Model):
    name = m.CharField(max_length=50, unique=True)
    price = m.PositiveSmallIntegerField()
    image = m.ImageField(upload_to="products")

    class Category(m.TextChoices):
        CLOTHING = "Clothing"
        ACCESSORIES = "Accessories"
        BATHROOM_AND_KITCHEN = "Bathroom & Kitchen"
        ELECTRONICS = "Electronics"

    category = m.CharField(
        max_length=30,
        choices=Category.choices,
        default=Category.ACCESSORIES,
    )

    def __str__(self):
        return self.name


class BasketItem(m.Model):
    product = m.ForeignKey(Product, on_delete=m.CASCADE)
    basket = m.ForeignKey("Basket", on_delete=m.CASCADE)


class Basket(m.Model):
    products = m.ManyToManyField(Product, through="BasketItem")

    @staticmethod
    def get():
        if Basket.objects.first():
            return Basket.objects.first()
        else:
            return Basket.objects.create()
