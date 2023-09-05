from django.urls import path
from .views import PizzaOrderAPIView

urlpatterns = [
    path('orderpizza/',PizzaOrderAPIView.as_view(), name="orderpizza"),
    path('pizzaorders/<int:id>/', PizzaOrderAPIView.as_view(), name="pizzaorder-detail"),
]