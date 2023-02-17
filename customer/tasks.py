from celery import shared_task
from customer.models import User


@shared_task
def customer_buy_car():
    pass