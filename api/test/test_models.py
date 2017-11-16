from datetime import date
from django.test import TestCase
from django.db import IntegrityError

from ..models import Person, Address, Email, PhoneNumber


class PersonModelTestCase(TestCase):
    """
    This class defines the test suite for the user model.
    """

    def setUp(self):
        """Define the test client and other test variables."""
        self.person_first_name = "John"
        self.person_last_name = "Doe"
        self.person_date_of_birth = date(1990, 4, 15)
        self.person = Person(
            first_name=self.person_first_name,
            last_name=self.person_last_name,
            date_of_birth=self.person_date_of_birth
        )

    def test_model_can_create_a_person(self):
        """Test the person model can be created."""
        old_count = Person.objects.count()
        self.person.save()
        new_count = Person.objects.count()
        self.assertNotEqual(old_count, new_count)

    def test_model_person_str_representation(self):
        """Test the string representation."""
        self.assertEqual(self.person.__str__(), "{} {}".format(
            self.person.first_name, self.person.last_name))


class AddressModelTestCase(TestCase):
    """
    This class defines the test suite for the address model.
    """

    def setUp(self):
        """Define the test client and other test variables."""
        self.address_owner = Person.objects.create(
            first_name="John",
            last_name="Doe",
            date_of_birth=date(1990, 4, 15)
        )
        self.address_address1 = "123 ABC street"
        self.address_address2 = ""
        self.address_city = "Seattle"
        self.address_state = "Washington"
        self.address_country = "US"
        self.address_zip_code = "23842"
        self.address = Address(
            owner=self.address_owner,
            address1=self.address_address1,
            address2=self.address_address2,
            city=self.address_city,
            state=self.address_state,
            country=self.address_country,
            zip_code=self.address_zip_code
        )

    def test_model_can_create_an_address(self):
        """Test the address model can be created."""
        old_count = Address.objects.count()
        self.address.save()
        new_count = Address.objects.count()
        self.assertNotEqual(old_count, new_count)

    def test_model_address_str_representation(self):
        """Test the string representation."""
        self.assertEqual(self.address.__str__(), "{} {} {} {} {} {}".format(
            self.address.address1, self.address.address2, self.address.city,
            self.address.state, self.address.country, self.address.zip_code))


class EmailModelTestCase(TestCase):
    """
    This class defines the test suite for the email model.
    """

    def setUp(self):
        """Define the test client and other test variables."""
        self.email_owner = Person.objects.create(
            first_name="John",
            last_name="Doe",
            date_of_birth=date(1990, 4, 15)
        )
        self.email_email = "john.doe@example.com"
        self.email = Email(
            owner=self.email_owner,
            email=self.email_email
        )

    def test_model_can_create_an_email(self):
        """Test the email model can be created."""
        old_count = Email.objects.count()
        self.email.save()
        new_count = Email.objects.count()
        self.assertNotEqual(old_count, new_count)

    def test_model_email_str_representation(self):
        """Test the string representation."""
        self.assertEqual(self.email.__str__(), "{}".format(self.email.email))


class PhoneNumberModelTestCase(TestCase):
    """
    This class defines the test suite for the phone_number model.
    """

    def setUp(self):
        """Define the test client and other test variables."""
        self.phone_number_owner = Person.objects.create(
            first_name="John",
            last_name="Doe",
            date_of_birth=date(1990, 4, 15)
        )
        self.phone_number_phone_number = "123456789"
        self.phone_number = PhoneNumber(
            owner=self.phone_number_owner,
            phone_number=self.phone_number_phone_number
        )

    def test_model_can_create_an_phone_number(self):
        """Test the phone_number model can be created."""
        old_count = PhoneNumber.objects.count()
        self.phone_number.save()
        new_count = PhoneNumber.objects.count()
        self.assertNotEqual(old_count, new_count)

    def test_model_phone_number_str_representation(self):
        """Test the string representation."""
        self.assertEqual(self.phone_number.__str__(),
                         "{}".format(self.phone_number.phone_number))
