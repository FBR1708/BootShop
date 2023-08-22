from django.contrib import admin
from .models import Product, Color, Category, ProductImage

@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ["name", "price", "created_at"]

@admin.register(Color)
class ColorModelAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoryModelAdmin(admin.ModelAdmin):
    pass

@admin.register(ProductImage)
class ProductImageModelAdmin(admin.ModelAdmin):
    pass
