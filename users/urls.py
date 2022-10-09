from django.urls import path,include
from .views import RegistrationAccountAPIView,RegistrationAccountCLientAPIView, UserLogoutView, SpecUserViewAPIView,ClientUserViewAPIView
from rest_framework.routers import SimpleRouter

app_name = 'users'
router = SimpleRouter()
router.register(r'spec',SpecUserViewAPIView)
router.register(r'client',ClientUserViewAPIView)

urlpatterns = [
    path('users/', RegistrationAccountAPIView.as_view()),
    path('users_client/', RegistrationAccountCLientAPIView.as_view()),
    path('users/',include(router.urls)),
    path('logout/', UserLogoutView.as_view()),

]

