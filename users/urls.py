from rest_framework.routers import DefaultRouter

from django.urls import path
from .views import RegisterSpecAPIView, UserAPIView, LogoutView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


app_name = 'users'


urlpatterns = [
    # path('register/client/', RegisterClientAPIView.as_view()),
    path('register/spec/', RegisterSpecAPIView.as_view()),
    path('user/<int:pk>/', UserAPIView.as_view()),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('logout/', LogoutView.as_view()),
]