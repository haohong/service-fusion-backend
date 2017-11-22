from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter

from .views import PersonViewSet


router = DefaultRouter()
router.register(r'customers', PersonViewSet, base_name='customer')

urlpatterns = [
    url(r'^', include(router.urls)),
]
