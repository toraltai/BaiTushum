from django.urls import path
from .views import RegistrationAPIView,LoginSerializerAPIView
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView,TokenVerifyView
app_name = 'users'

urlpatterns = [
    path('users/',RegistrationAPIView.as_view()),

]