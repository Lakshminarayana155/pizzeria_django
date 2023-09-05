from celery import shared_task
from datetime import timedelta
from django.utils import timezone
from .models import PizzaOrder

@shared_task
def update_order_status_periodic():
    # Calculate the timestamps for status changes
    print("Updating order status periodically...")
    now = timezone.now()
    one_minute_later = now - timedelta(minutes=1)
    three_minutes_later = now - timedelta(minutes=3)
    five_minutes_later = now - timedelta(minutes=5)

    # Update orders based on their created_at timestamp
    PizzaOrder.objects.filter(
        order_status='Accepted',
        orderd_at__lte=one_minute_later
    ).update(order_status='Preparing')

    PizzaOrder.objects.filter(
        order_status='Preparing',
        orderd_at__lte=three_minutes_later
    ).update(order_status='Dispatched')

    PizzaOrder.objects.filter(
        order_status='Dispatched',
        orderd_at__lte=five_minutes_later
    ).update(order_status='Delivered')
