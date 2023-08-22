from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self) -> str:
        return self.title


class Color(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.title


class Product(models.Model):
    name = models.CharField(max_length=128)
    brand = models.CharField(max_length=50, blank=True)
    price = models.PositiveIntegerField()
    count = models.PositiveIntegerField()
    description = models.TextField()
    dimension = models.CharField(max_length=200)
    displaysize = models.PositiveIntegerField()
    colors = models.ManyToManyField(Color, related_name="products")
    categories = models.ManyToManyField(Category, related_name="category")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self) -> str:
        return self.name


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=f"images/{product}/", blank=True)

    def __str__(self) -> str:
        return self.product.name
