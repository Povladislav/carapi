import json

from django.test import Client, TestCase

from car.models import AvailableCar, Car, Color, ModelName

c = Client()


class TestCaseClass(TestCase):
    def setUp(self):
        color = Color.objects.create(title="yellow")
        modelname = ModelName.objects.create(title="AUDIA6")
        car = Car.objects.create(model=modelname, color=color, power=Car.POWER.choices[0][0])
        AvailableCar.objects.create(available_car=car, count=5, price=50000)

    def test_create_car(self):
        car = Car.objects.get(id=1)
        av_car = AvailableCar.objects.get(id=1)
        self.assertEqual(car.model.title, "AUDIA6")
        self.assertEqual(av_car.price, 50000)

    def test_crud_car_get_all(self):
        response = c.get('http://127.0.0.1:8000/api/v1/cars/')
        self.assertEqual(200, response.status_code)
        self.assertEqual("50000", response.data[0]["price"])

    def test_crud_car_create(self):
        car = Car.objects.first()
        response = c.post('http://127.0.0.1:8000/api/v1/cars/',
                          {"count": 5, "price": 50000, "available_car": car.id})
        self.assertEqual(201, response.status_code)
        self.assertEqual("50000", response.data["price"])

    def test_crud_car_update(self):
        av_car = AvailableCar.objects.first()
        data = json.dumps({"count": 6})
        response = c.patch(f'http://127.0.0.1:8000/api/v1/cars/{av_car.id}/', data=data,
                           content_type='application/json')
        self.assertEqual(200, response.status_code)

    def test_crud_car_delete(self):
        av_car = AvailableCar.objects.first()
        response = c.delete(f'http://127.0.0.1:8000/api/v1/cars/{av_car.id}/')
        self.assertEqual(204, response.status_code)
