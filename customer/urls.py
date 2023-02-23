from django.urls import path

from customer.views import (EnterNewPasswordView, PasswordRestoreView,
                            RegisterView, ResetPasswordView, VerifyEmail)

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("reset-password", ResetPasswordView.as_view(), name="reset-password"),
    path("restore-password", PasswordRestoreView.as_view(), name="restore-password"),
    path("email-verify/", VerifyEmail.as_view(), name="email-verify"),
    path("password-verify/", EnterNewPasswordView.as_view(), name="password-verify"),
]
