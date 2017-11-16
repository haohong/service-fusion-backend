from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter

from .views import PersonViewSet


router = DefaultRouter()
router.register(r'people', PersonViewSet, base_name='person')

urlpatterns = [
    url(r'^', include(router.urls)),
]
