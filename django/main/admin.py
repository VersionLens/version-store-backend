from django.contrib import admin
from .models import Product, Basket, Category


class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "price", "category", "image")


admin.site.register(Product, ProductAdmin)


class BasketItemInline(admin.TabularInline):
    model = Basket.products.through
    extra = 0


class BasketAdmin(admin.ModelAdmin):
    inlines = (BasketItemInline,)


admin.site.register(Basket, BasketAdmin)


admin.site.register(Category)
