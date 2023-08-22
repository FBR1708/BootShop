# from rest_framework.serializers import ModelSerializer, ReadOnlyField
# from .models import Category, Color, Product, ProductImage
#
#
# class CategoryModelSerializer(ModelSerializer):
#     class Meta:
#         model = Category
#         fields = "title",
#
#
# class ColorModelSerializer(ModelSerializer):
#     class Meta:
#         model = Color
#         fields = "title",
#
#
# class ProductModelSerializer(ModelSerializer):
#     categories = CategoryModelSerializer(many=True)
#     colors = ColorModelSerializer(many=True)
#
#     class Meta:
#         model = Product
#         fields = "__all__"
#
#
# class ProductImageModelSerializer(ModelSerializer):
#     class Meta:
#         model = ProductImage
#         fields = "__all__"
#
from rest_framework.serializers import ModelSerializer
from main.models import Category, Product, ProductColor, ProductImage


class CategoryModelSerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ('title',)


class ProductColorModelSerializer(ModelSerializer):
    class Meta:
        model = ProductColor
        fields = ('color',)


class ProductModelSerializer(ModelSerializer):
    category = CategoryModelSerializer(many=True)
    color = ProductColorModelSerializer(many=True)

    class Meta:
        model = Product
        fields = '__all__'


class ProductImageModelSerializer(ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ("to_product", 'image',)


class PostActiveSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ("is_active",)
