from django.urls import path,re_path,include

from .views import RegistrationAccountAPIView, UserLogoutView

app_name = 'users'

urlpatterns = [
    path('users/', RegistrationAccountAPIView.as_view()),
    # path('client/', RegistrationClientAPIView.as_view()),
    path('logout/', UserLogoutView.as_view()),
]
