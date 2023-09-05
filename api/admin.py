from django.contrib import admin
from .models import PizzaOrder, Topping
# Register your models here.

admin.site.register(PizzaOrder)
admin.site.register(Topping)

