

from django.urls import path, include
from .views import RegisterClientAPIView, UserLogoutView, RegisterSpecAPIView, UserAPIView

app_name = 'users'


urlpatterns = [
    path('register/client/', RegisterClientAPIView.as_view()),
    path('register/spec/', RegisterSpecAPIView.as_view()),
    path('user/<int:pk>/', UserAPIView.as_view()),
    path('logout/', UserLogoutView.as_view()),
]