from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.core.validators import MinValueValidator
from django.db import models
from django_countries.fields import CountryField


class DateMixin(models.Model):
    created_at = models.DateField(auto_now=True)
    updated_at = models.DateField(auto_now_add=True)

    class Meta:
        abstract = True


class IsActiveMixin(models.Model):
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        if username is None:
            raise TypeError("User should have a username!")
        if email is None:
            raise TypeError("User should have an email!")
        user = self.model(username=username, email=self.normalize_email(email))
        user.set_password(password)
        user.save()
        return user


class User(AbstractUser, DateMixin, IsActiveMixin):
    email = models.EmailField(max_length=44, unique=True, db_index=True)
    balance = models.DecimalField(validators=[MinValueValidator(0)], decimal_places=0, max_digits=6, null=True)
    is_verified = models.BooleanField(default=False)
    info = models.CharField(max_length=200)
    purchased_cars = models.ManyToManyField('car.Car', blank=True)
    objects = UserManager()

    def __str__(self):
        return self.username


class Location(models.Model):
    country = CountryField()
