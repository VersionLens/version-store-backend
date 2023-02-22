from django.contrib import admin
from .models import Product, Basket, Review


# Product
class ReviewInline(admin.TabularInline):
    model = Review
    extra = 0


class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "price", "image")
    inlines = (ReviewInline,)


admin.site.register(Product, ProductAdmin)


# Basket
class BasketItemInline(admin.TabularInline):
    model = Basket.products.through
    extra = 0


class BasketAdmin(admin.ModelAdmin):
    inlines = (BasketItemInline,)


admin.site.register(Basket, BasketAdmin)
