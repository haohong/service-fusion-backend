from django.db import models
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField


class User(models.Model):
    """
    This class represents the user model.
    """
    firstname = models.CharField(max_length=30, blank=False)
    lastname = models.CharField(max_length=30, blank=False)
    birthday = models.DateField(blank=False)

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)


class Address(models.Model):
    """
    This class represents address model.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address1 = models.CharField(max_length=128, blank=False)
    address2 = models.CharField(max_length=128, blank=True)

    city = models.CharField(max_length=64, blank=False)
    state = models.CharField(max_length=64, blank=False)
    country = CountryField(blank=False)
    zipcode = models.CharField(max_length=16, blank=False)

    def __str__(self):
        return "{} {} {} {} {} {}".format(
            self.address1, self.address2, self.city, self.state, self.country, self.zipcode)


class Email(models.Model):
    """
    This class represents email model.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=50, blank=False)

    def __str__(self):
        return self.email


class PhoneNumber(models.Model):
    """
    This class represents phone number model
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone_number = PhoneNumberField(blank=False)
