from django.core.urlresolvers import reverse
from rest_framework.test import APITestCase
from rest_framework import status

from ..models import Person


class PersonViewTestCase(APITestCase):
    """Test suite for the person api views."""

    def setUp(self):
        """Define the test client and other test variables."""
        # Initialize client and force it to use authentication

        self.person_data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'date_of_birth': '1990-04-15',
            'addresses': [{
                'address1': '123 Abc',
                'address2': '',
                'city': 'Los Angeles',
                'state': 'California',
                'country': 'US',
                'zip_code': '23432'
            }],
            'emails': [{
                'email': 'john.doe@gmail.com'
            }],
            'phone_numbers': [{
                'phone_number': '+12345678910'
            }]
        }
        self.response = self.client.post(
            reverse('api:person-list'),
            self.person_data,
            format='json')

    def test_create_person(self):
        """Test the api has person creation capability."""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_get_person(self):
        """Test the api can get a given person."""
        person = Person.objects.get()
        response = self.client.get(
            reverse('api:person-detail', kwargs={'pk': person.id}),
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, person.first_name)
        self.assertContains(response, person.last_name)

    def test_update_person(self):
        """Test the api can update a given person."""
        person = Person.objects.get()
        change_person = {
            'first_name': 'Jane',
            'last_name': 'Doe',
            'date_of_birth': '1992-03-21',
        }
        res = self.client.patch(
            reverse('api:person-detail', kwargs={'pk': person.id}),
            change_person,
            format='json'
        )

        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_delete_person(self):
        """Test the api can delete a person."""
        person = Person.objects.get()
        response = self.client.delete(
            reverse('api:person-detail', kwargs={'pk': person.id}),
            format='json',
            follow=True
        )

        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
