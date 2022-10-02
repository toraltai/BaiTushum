from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import *

r = DefaultRouter()
r.register('client', APIClient)
r.register('entity', APIEntity)
r.register('company', APICompany)
r.register('property', APIProperty)
r.register('guarant', APIGuarantor)
r.register('convers', APIConvers)
r.register('dataKK', APIDataKK)

urlpatterns = [
    path('api/', include(r.urls)),
]
