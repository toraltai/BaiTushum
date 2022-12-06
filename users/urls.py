from rest_framework.routers import DefaultRouter

from django.urls import path
from .views import UserLogoutView, RegisterSpecAPIView, UserAPIView

app_name = 'users'


urlpatterns = [
    # path('register/client/', RegisterClientAPIView.as_view()),
    path('register/spec/', RegisterSpecAPIView.as_view()),
    path('user/<int:pk>/', UserAPIView.as_view()),
    path('logout/', UserLogoutView.as_view()),
]