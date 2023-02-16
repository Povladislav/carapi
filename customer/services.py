from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from rest_framework_simplejwt.tokens import RefreshToken

from customer.utils import Util


def building_url_register(user, request):
    token = RefreshToken.for_user(user).access_token

    current_site = get_current_site(request).domain
    relativeLink = reverse('email-verify')
    absurl = 'http://' + current_site + relativeLink + "?token=" + str(token)
    email_body = 'Hi' + ' ' + user.username + ' Use link below to verify your email!\n' + absurl
    data = {'email_body': email_body, 'to_email': user.email, 'email_subject': 'Verify your email'}

    Util.send_email(data=data)


def building_url_restore(user, request):
    token = RefreshToken.for_user(user).access_token

    current_site = get_current_site(request).domain
    relativeLink = reverse('password-verify')
    absurl = 'http://' + current_site + relativeLink + "?token=" + str(token)
    email_body = 'Hi' + ' ' + user.username + ' Use link below to restore your email!\n' + absurl
    data = {'email_body': email_body, 'to_email': user.email, 'email_subject': 'Restore your password'}

    Util.send_email(data=data)
