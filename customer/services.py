from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from django.utils.encoding import (DjangoUnicodeDecodeError, force_str,
                                   smart_bytes, smart_str)
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from rest_framework import generics, status, views
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from customer.models import User
from customer.utils import Util


def building_url_register(user, request):
    token = RefreshToken.for_user(user).access_token

    current_site = get_current_site(request).domain
    relativeLink = reverse('email-verify')
    absurl = 'http://' + current_site + relativeLink + "?token=" + str(token)
    email_body = 'Hi' + ' ' + user.username + ' Use link below to verify your email!\n' + absurl
    data = {'email_body': email_body, 'to_email': user.email, 'email_subject': 'Verify your email'}

    Util.send_email(data=data)


def building_url_reset(uidb64, request, token, user):
    current_site = get_current_site(request=request).domain
    relativeLink = reverse('password-reset-confirm', kwargs={'uidb64': uidb64, 'token': token})
    absurl = 'http://' + current_site + relativeLink
    email_body = 'Hello mafacka,\n Use link below to reset your password!\n' + absurl
    data = {'email_body': email_body, 'to_email': user.email, 'email_subject': 'Reset your password'}

    Util.send_email(data=data)


def check_token(uidb64, token):
    try:
        id = smart_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(id=id)
        if not PasswordResetTokenGenerator().check_token(user, token):
            return Response({'error': 'Token is not valid anymore! Please request a new one'},
                            status=status.HTTP_401_UNAUTHORIZED)

        return Response({'success': True, 'message': 'Credentials Valid', 'uidb64': uidb64, 'token': token},
                        status=status.HTTP_200_OK)

    except DjangoUnicodeDecodeError:
        return Response({'error': 'Token is not valid anymore! Please request a new one'},
                        status=status.HTTP_401_UNAUTHORIZED)
