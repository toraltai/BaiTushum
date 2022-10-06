from django.urls import path,re_path

from .views import RegistrationSpecAPIView, RegistrationClientAPIView, UserLogoutView

app_name = 'users'

urlpatterns = [
    path('users/', RegistrationSpecAPIView.as_view()),
    path('client/', RegistrationClientAPIView.as_view()),
    path('logout/', UserLogoutView.as_view()),

]
