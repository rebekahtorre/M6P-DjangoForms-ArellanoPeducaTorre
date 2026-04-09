from django.db import models
from django.utils import timezone

# Create your models here. testing

class Supplier(models.Model):
    name = models.CharField(max_length=300)
    city = models.CharField(max_length=300)
    country = models.CharField(max_length=300)
    created_at = models.DateTimeField(blank=True, null=True)
    objects = models.Manager()

    def getName(self) -> str:
        return self.name
    
    def __str__(self) -> str:
        return f"{self.name} - {self.city}, {self.country} created at: {self.created_at}"

class WaterBottle(models.Model):
    sku = models.CharField(max_length=300, unique=True, db_index=True)
    brand = models.CharField(max_length=300)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    size = models.CharField(max_length=300)
    mouth_size = models.CharField(max_length=300)
    color = models.CharField(max_length=300)
    supplied_by = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    current_quantity = models.PositiveIntegerField()
    objects = models.Manager()

    def __str__(self) -> str:
        return f"{self.sku}: {self.brand}, {self.mouth_size}, {self.size}, {self.color}, supplied by {self.supplied_by}, {self.cost}: {self.current_quantity}"
    
    
