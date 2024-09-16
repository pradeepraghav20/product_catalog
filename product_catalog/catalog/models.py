
from django.db import models
class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory_count = models.IntegerField()
    category = models.CharField(max_length=255)
    sales = models.IntegerField(default=0)  # To track sales for popularity

    def __str__(self):
        return self.name
