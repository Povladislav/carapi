import decimal

from celery import shared_task
from django.db import transaction
from django.db.models import F, Q
from django.utils import timezone

from car.models import AvailableCar, PreferableCar
from customer.models import User
from producer.models import Producer
from showroom.models import Discount, History, ShowRoom

users_with_offers = User.objects.filter(
    offer__count__isnull=False, is_verified=True, balance__gte=F("offer__price")
)
cars_for_customer = AvailableCar.objects.filter(showroom__isnull=False)
cars_for_showroom = AvailableCar.objects.filter(producer__isnull=False)
showrooms = ShowRoom.objects.exclude(preferable_cars__count__isnull=True)

producers = Producer.objects.all()


def iterator(showroom, p_car):
    most_benefit_car = None
    final_price = None
    for a_car in cars_for_showroom.filter(available_car=p_car.preferable_car):
        if a_car.producer.discount.exists():
            discount = Discount.objects.filter(
                Q(car=a_car.available_car)
                & Q(date_of_start__lt=timezone.now())
                & Q(date_of_end__gt=timezone.now())
            ).first()
            if (
                discount is not None
                and final_price <= p_car.price
                and showroom.balance >= p_car.price * p_car.count
            ):
                final_price = a_car.price * discount.size
                if most_benefit_car is None:
                    most_benefit_car = a_car
                    most_benefit_car.price = final_price
                elif (
                    most_benefit_car is not None
                    and a_car.price <= most_benefit_car.price
                ):
                    most_benefit_car = a_car
                    most_benefit_car.price = final_price
        else:
            final_price = a_car.price
            if (
                final_price <= p_car.price
                and showroom.balance >= p_car.price * p_car.count
            ):
                if most_benefit_car is None:
                    most_benefit_car = a_car
                    most_benefit_car.price = final_price
                elif (
                    most_benefit_car is not None
                    and a_car.price <= most_benefit_car.price
                ):
                    most_benefit_car = a_car
                    most_benefit_car.price = final_price
    return most_benefit_car


@shared_task
@transaction.atomic
def customer_buy_car():
    for user in users_with_offers:
        cars = AvailableCar.objects.filter(
            Q(available_car=user.offer.preferable_car) & Q(showroom__isnull=False)
        )
        for car in cars:
            if user.offer.price >= car.price and car.count > 0 and car.discount is None:
                user.purchased_cars.add(car.available_car)
                car.count -= 1
                user.balance -= car.price
                history = History.objects.create(
                    buyer_customer=user, count=1, whole_price=car.price
                )
                history.sold_car.add(car.available_car)
                car.showroom.history.add(history)
                car.showroom.balance += car.price
                car.showroom.save()
                car.save()
                user.save()
                break

            elif (
                car.discount is not None
                and timezone.now().date() > car.discount.date_of_start
                and car.discount.date_of_end > timezone.now().date()
            ):
                total_price = car.price * car.discount.size
                user.purchased_cars.add(car.available_car)
                car.count -= 1
                user.balance -= total_price
                history = History.objects.create(
                    buyer_customer=user, count=1, whole_price=car.price
                )
                history.sold_car.add(car.available_car)
                car.showroom.balance += total_price
                car.showroom.save()
                car.showroom.history.add(history)
                car.save()
                user.save()
                break


# @shared_task
# @transaction.atomic
# def showroom_buy_car():
#     for showroom in showrooms:
#         preferable_cars = showroom.preferable_cars.all()
#         for p_car in preferable_cars:
#             most_benefit_car = iterator(showroom, p_car)
#             if most_benefit_car is not None and int(p_car.count) == int(
#                     most_benefit_car.count
#             ):
#                 most_benefit_car.producer = None
#                 most_benefit_car.showroom = showroom
#                 most_benefit_car.price = round(float(most_benefit_car.price) / 0.7)
#                 showroom.balance -= most_benefit_car.price * most_benefit_car.count
#                 history = History.objects.create(
#                     buyer_showroom=showroom,
#                     count=p_car.count,
#                     whole_price=most_benefit_car.price * most_benefit_car.count,
#                 )
#                 history.sold_car.add(p_car.preferable_car)
#                 history.save()
#                 showroom.history.add(history)
#                 showroom.save()
#                 most_benefit_car.save()
#                 break
#
#             elif int(p_car.count) < int(most_benefit_car.count):
#                 most_benefit_car.count -= p_car.count
#                 showroom.balance -= p_car.count * most_benefit_car.price
#                 showroom.save()
#                 most_benefit_car.save()
#                 AvailableCar.objects.create(
#                     available_car=most_benefit_car.available_car,
#                     count=p_car.count,
#                     showroom=showroom,
#                     price=round(float(most_benefit_car.price) / 0.7),
#                 )
#                 history = History.objects.create(
#                     buyer_showroom=showroom,
#                     count=p_car.count,
#                     whole_price=p_car.price * p_car.count,
#                 )
#                 history.sold_car.add(p_car.preferable_car)
#                 history.save()
#                 showroom.history.add(history)
#                 break
#             elif int(p_car.count) > int(most_benefit_car.count):
#                 AvailableCar.objects.create(
#                     available_car=most_benefit_car.available_car,
#                     count=most_benefit_car.count,
#                     showroom=showroom,
#                     price=round(float(most_benefit_car.price) / 0.7),
#                 )
#                 p_car.count -= most_benefit_car.count
#                 showroom.balance -= most_benefit_car.count * most_benefit_car.price
#                 history = History.objects.create(
#                     buyer_showroom=showroom,
#                     count=p_car.count,
#                     whole_price=most_benefit_car.price * most_benefit_car.count,
#                 )
#                 history.sold_car.add(p_car.preferable_car)
#                 history.save()
#                 showroom.history.add(history)
#                 showroom.save()
#                 p_car.save()
#                 AvailableCar.objects.get(
#                     available_car=most_benefit_car.available_car
#                 ).delete()
#                 break


@shared_task
@transaction.atomic
def showroom_buy_car():
    final_price = 0
    for showroom in showrooms:
        for preferable_car in showroom.preferable_cars.all():
            most_benefit_car = (
                cars_for_showroom.filter(
                    Q(available_car=preferable_car) & Q(price__lte=preferable_car.price)
                )
                .order_by("price")
                .first()
            )
            if (
                most_benefit_car.discount is not None
                and most_benefit_car.discount.date_of_start
                <= timezone.now()
                <= most_benefit_car.discount.date_of_end
            ):
                if preferable_car.count == most_benefit_car.count:
                    final_price = (
                        most_benefit_car.price
                        * most_benefit_car.count
                        * most_benefit_car.discount
                    )
                    showroom.balance -= final_price
                    most_benefit_car.producer = None
                    most_benefit_car.showroom = showroom
                    most_benefit_car.price = float(most_benefit_car.price) / 0.7
                    history = History.objects.create(
                        buyer_showroom=showroom,
                        count=preferable_car.count,
                        whole_price=most_benefit_car.price * most_benefit_car.count,
                    )
                    history.sold_car.add(preferable_car.preferable_car)
                    history.save()
                    preferable_car.delete()
                    preferable_car.save()
                    most_benefit_car.save()
                    showroom.save()
                elif preferable_car.count >= most_benefit_car.count:
                    final_price = (
                        most_benefit_car.price
                        * most_benefit_car.count
                        * most_benefit_car.discount
                    )
                    showroom.balance -= final_price
                    most_benefit_car.producer = None
                    most_benefit_car.showroom = showroom
                    preferable_car.count -= most_benefit_car.count
                    most_benefit_car.price = float(most_benefit_car.price) / 0.7
                    history = History.objects.create(
                        buyer_showroom=showroom,
                        count=preferable_car.count,
                        whole_price=most_benefit_car.price * most_benefit_car.count,
                    )
                    history.sold_car.add(preferable_car.preferable_car)
                    history.save()
                    preferable_car.save()
                    most_benefit_car.save()
                    showroom.save()
                elif preferable_car.count <= most_benefit_car.count:
                    final_price = (
                        most_benefit_car.price
                        * preferable_car.count
                        * most_benefit_car.discount
                    )
                    showroom.balance -= final_price
                    most_benefit_car.count -= preferable_car.count
                    AvailableCar.objects.create(
                        available_car=most_benefit_car.available_car,
                        count=preferable_car.count,
                        showroom=showroom,
                        price=round(float(most_benefit_car.price) / 0.7),
                    )
                    history = History.objects.create(
                        buyer_showroom=showroom,
                        count=preferable_car.count,
                        whole_price=most_benefit_car.price * most_benefit_car.count,
                    )
                    history.sold_car.add(preferable_car.preferable_car)
                    history.save()
                    preferable_car.save()
                    most_benefit_car.save()
                    showroom.save()
            else:
                if preferable_car.count == most_benefit_car.count:
                    final_price = most_benefit_car.price * most_benefit_car.count
                    showroom.balance -= final_price
                    most_benefit_car.producer = None
                    most_benefit_car.showroom = showroom
                    most_benefit_car.price = float(most_benefit_car.price) / 0.7
                    history = History.objects.create(
                        buyer_showroom=showroom,
                        count=preferable_car.count,
                        whole_price=most_benefit_car.price * most_benefit_car.count,
                    )
                    history.sold_car.add(preferable_car.preferable_car)
                    history.save()
                    preferable_car.delete()
                    preferable_car.save()
                    most_benefit_car.save()
                    showroom.save()
                elif preferable_car.count >= most_benefit_car.count:
                    final_price = most_benefit_car.price * most_benefit_car.count
                    showroom.balance -= final_price
                    most_benefit_car.producer = None
                    most_benefit_car.showroom = showroom
                    preferable_car.count -= most_benefit_car.count
                    most_benefit_car.price = float(most_benefit_car.price) / 0.7
                    history = History.objects.create(
                        buyer_showroom=showroom,
                        count=preferable_car.count,
                        whole_price=most_benefit_car.price * most_benefit_car.count,
                    )
                    history.sold_car.add(preferable_car.preferable_car)
                    history.save()
                    preferable_car.save()
                    most_benefit_car.save()
                    showroom.save()
                elif preferable_car.count <= most_benefit_car.count:
                    final_price = most_benefit_car.price * preferable_car.count
                    showroom.balance -= final_price
                    most_benefit_car.count -= preferable_car.count
                    AvailableCar.objects.create(
                        available_car=most_benefit_car.available_car,
                        count=preferable_car.count,
                        showroom=showroom,
                        price=round(float(most_benefit_car.price) / 0.7),
                    )
                    history = History.objects.create(
                        buyer_showroom=showroom,
                        count=preferable_car.count,
                        whole_price=most_benefit_car.price * most_benefit_car.count,
                    )
                    history.sold_car.add(preferable_car.preferable_car)
                    history.save()
                    preferable_car.save()
                    most_benefit_car.save()
                    showroom.save()
