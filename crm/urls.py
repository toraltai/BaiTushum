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
# r.register('activity', APIActivity)

urlpatterns = [
    path('api/', include(r.urls)),
    path('api/activity/', APIActivity.as_view()),
    path('test/', DashboardView.as_view())
]
