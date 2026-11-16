from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    price = models.DecimalField(max_digits=10, decimal_places=2) #12345678.90
    description = models.TextField()
    stock = models.PositiveSmallIntegerField()
    
    def __str__(self) -> str:
        return self.name

class OrderStatus(models.TextChoices):
    PENDING = 'Pending'
    PROCESSING = 'Processing'
    PAID = 'Paid'
    CANCELLED = 'Cancelled'

class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=11, choices=OrderStatus, default=OrderStatus.PENDING)
    created_at = models.DateTimeField(auto_now_add=True)

