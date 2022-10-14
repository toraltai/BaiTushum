from django.urls import path, include
from rest_framework.routers import SimpleRouter

from .views import RegisterClientAPIView, UserLogoutView, \
    SpecUserViewAPIView, ClientUserViewAPIView, RegisterSpecAPIView, UserAPIView

app_name = 'users'
router = SimpleRouter()
router.register(r'spec', SpecUserViewAPIView)
router.register(r'client', ClientUserViewAPIView)

urlpatterns = [
    path('users/', include(router.urls)),
    path('register/client/', RegisterClientAPIView.as_view()),
    path('register/spec/', RegisterSpecAPIView.as_view()),
    path('user/<int:pk>/', UserAPIView.as_view()),
    path('logout/', UserLogoutView.as_view()),

    # path('users/', RegistrationAccountAPIView.as_view()),
    # path('users_client/', RegistrationAccountCLientAPIView.as_view()),
    # path('client/', RegistrationClientAPIView.as_view()),

]

