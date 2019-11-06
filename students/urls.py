from django.conf.urls import url, include
from rest_framework import routers
from .views import StudentViewSet, AddressViewSet

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'students', StudentViewSet)
router.register(r'addresses', AddressViewSet)
