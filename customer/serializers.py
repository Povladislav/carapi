import jwt
from django.conf import settings
from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed

from customer.models import User


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=22, min_length=6, write_only=True)

    def validate(self, attrs):
        username = attrs.get('username', '')

        if not username.isalnum():
            raise serializers.ValidationError('The username should only contain alphanumeric characters')
        return attrs

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

    class Meta:
        model = User
        fields = ['username', 'password', 'email']


class EmailVerificationSerializer(serializers.ModelSerializer):
    token = serializers.CharField(max_length=555)

    class Meta:
        model = User
        fields = ['token']


class PasswordCreateSerializer(serializers.Serializer):
    new_password = serializers.CharField(min_length=6, max_length=68, write_only=True)
    token = serializers.CharField(min_length=1, write_only=True)

    def validate(self, attrs):
        token = attrs.get('token')
        password = attrs.get('new_password')

        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=settings.SIMPLE_JWT['ALGORITHM'])
        except Exception as e:
            raise AuthenticationFailed('The reset link is invalid', 401)
        user = User.objects.get(id=payload['user_id'])

        if not user.is_verified:
            raise serializers.ValidationError('User is not verified!')
        user.set_password(password)
        user.save()
        return (user)

    class Meta:
        fields = ['new_password', 'new_token']


class PasswordRestoreSerializer(serializers.Serializer):
    email = serializers.EmailField(min_length=2)

    def validate(self, attrs):
        try:
            email = attrs.get('email')
        except Exception as e:
            raise serializers.ValidationError('Cannot find email!', 401)
        return attrs

    class Meta:
        fields = ['email']


class EnterPasswordSerializer(serializers.Serializer):
    new_password = serializers.CharField(min_length=6, max_length=68, write_only=True)

    def validate(self, attrs):
        return super().validate(attrs)

    class Meta:
        fields = ['new_password']
