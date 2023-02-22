from django.db import models as m
from django.utils.translation import gettext_lazy as _


class Category(m.Model):
    name = m.CharField(max_length=30)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name


class Product(m.Model):
    name = m.CharField(max_length=50, unique=True)
    price = m.PositiveSmallIntegerField()
    image = m.ImageField(upload_to="products")
    category = m.ForeignKey(
        Category, on_delete=m.CASCADE, related_name="products", null=True, blank=True
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
