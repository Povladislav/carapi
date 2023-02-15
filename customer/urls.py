from django.urls import path

from customer.views import (PasswordTokenCheckAPI, RegisterView,
                            RequestPasswordResetEmail, SetNewPasswordAPIView,
                            VerifyEmail)

urlpatterns = [
    path('register/', RegisterView.as_view(), name="register"),
    path('password-reset/<uidb64>/<token>/', PasswordTokenCheckAPI.as_view(), name="password-reset-confirm"),
    path('request-reset-email', RequestPasswordResetEmail.as_view(), name='request-reset-email'),
    path('password-reset-complete', SetNewPasswordAPIView.as_view(), name='password-reset-complete'),
    path('email-verify/', VerifyEmail.as_view(), name="email-verify")
]
