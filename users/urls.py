from django.urls import path
from .views import RegistrationSpecAPIView,RegistrationClientAPIView

app_name = 'users'

urlpatterns = [
    path('users/',RegistrationSpecAPIView.as_view()),
    path('client/',RegistrationClientAPIView.as_view())
]