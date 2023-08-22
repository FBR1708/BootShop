from django.db import models
from django.contrib.auth.models import User
from main.models import Product, ProductColor


class ProductShop(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    count = models.PositiveIntegerField()
    color = models.ForeignKey(ProductColor, on_delete=models.SET_NULL, null=True)
    price = models.PositiveIntegerField()
    sum_price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.sum_price = self.count * self.product.price
        return super().save(*args, **kwargs)


class Contact(models.Model):
    name = models.CharField(max_length=80)
    email = models.EmailField(max_length=128)
    submit = models.CharField(max_length=200)
    body = models.TextField()

    def __str__(self):
        return self.name
