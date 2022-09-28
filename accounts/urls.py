from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from accounts.views import *

urlpatterns = [
    path('register/', RegisterApiView.as_view()),
    path('register/spec_user/', RegisterSpecApiView.as_view()),
    path('active/<uuid:activation_code>/', ActivationView.as_view()),
    path('change_password/', ChangePasswordView.as_view()),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('reset_password/', ForgotPasswordView.as_view()),
    path('create_new_password/', ForgotPasswordComplete.as_view())
]