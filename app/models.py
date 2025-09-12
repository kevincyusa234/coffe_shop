from django.db import models

# Create your models here.
class Booking(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    date = models.DateField()
    time = models.TimeField()
    people = models.IntegerField()
    comments = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} - {self.date} at {self.time}"

# product models
class Product(models.Model):
    name = models.CharField(max_length=100)
    ingredients = models.TextField(blank=True, null=True)
    status = models.BooleanField(default=True)  # Available or not

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="menu_items")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="menu_items")
    price = models.DecimalField(max_digits=6, decimal_places=2)
    status = models.BooleanField(default=True)  

    def __str__(self):
        return f"({self.category.name})"


