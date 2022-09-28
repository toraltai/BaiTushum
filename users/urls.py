from django.urls import path
from .views import RegistrationSpecAPIView

app_name = 'users'

urlpatterns = [
    path('users/',RegistrationSpecAPIView.as_view()),
]