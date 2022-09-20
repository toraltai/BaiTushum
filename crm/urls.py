from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter

from .views import *

r = DefaultRouter()
r.register('client', APIClient)
r.register('entity', APIEntity )
r.register('credit_spec', APICreditSpecialist)
r.register('occup', APIOccupation)
r.register('company', APICompany)
r.register('property', APIProperty)
r.register('guarant', APIGuarantor)
r.register('teleph_convers', APITelephConvers)
r.register('meet_convers', APIMeetConvers)
r.register('dataKK', APIDataKK)


urlpatterns = [
    path('api/', include(r.urls)),
]
