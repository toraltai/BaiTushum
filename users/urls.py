from django.urls import path
from .views import RegistrationAPIView,LoginSerializerAPIView
from rest_framework_simplejwt.views import TokenObtainPairView


app_name = 'users'

urlpatterns = [
    path('users/',RegistrationAPIView.as_view()),
    path('users/login/',TokenObtainPairView.as_view(), name='token_obtain_pair')
]