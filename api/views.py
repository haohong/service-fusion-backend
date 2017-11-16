from rest_framework import viewsets

from .models import Person
from .serializers import PersonSerializer


class PersonViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides CRUD operations on person model
    """
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
