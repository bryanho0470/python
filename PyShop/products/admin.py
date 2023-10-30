from django.contrib import admin
from .models import Product, Offer


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')


class ProductOffer(admin.ModelAdmin):
    list_display = ('coupon', 'discount')


admin.site.register(Product, ProductAdmin)

admin.site.register(Offer, ProductOffer)