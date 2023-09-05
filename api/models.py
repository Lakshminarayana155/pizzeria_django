import json
from django.db import models

# Create your models here.
# class PizzaBase(models.Model):
#     class Meta:
#         db_table = "pizza_base"
#     name = models.CharField(max_length=100, unique=True)
    
#     def __str__(self):
#         return self.name

# class Cheese(models.Model):
#     class Meta:
#         db_table = "cheese"
#     name = models.CharField(max_length=100, unique=True)
    
#     def __str__(self):
#         return self.name
    
class Topping(models.Model):
    class Meta:
        db_table = "topping"
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
    
class PizzaOrder(models.Model):
    class Meta:
        db_table = "pizza_order"

    STATUS_CHOICES = [
        ('Accepted', 'Accepted'),
        ('Preparing', 'Preparing'),
        ('Dispatched', 'Dispatched'),
        ('Delivered', 'Delivered'),
    ]
    
    BASE_CHOICES = [
        (1, 'Thin-Crust'),
        (2, 'Normal'),
        (3, 'Cheese-Burst'),
    ]

    CHEESE_CHOICES = [
        (1, 'Cream Cheese'),
        (2, 'Mozzarella'),
        (3, 'Cheddar'),
        (4, 'Cottage cheese'),
    ]

    base = models.CharField(max_length=20, choices=BASE_CHOICES)
    cheese = models.CharField(max_length=20, choices=CHEESE_CHOICES)
    toppings = models.ManyToManyField(Topping, related_name='pizza_orders')
    order_status =models.CharField(max_length=20,choices=STATUS_CHOICES,default='Accepted')
    orderd_at = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=100.00)

    def __str__(self):
        return f"Pizza Order #{self.pk}"
