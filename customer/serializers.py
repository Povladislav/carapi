from rest_framework import serializers

from customer.models import User


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=22, min_length=6, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'email']

        def validate(self, attrs):
            email = attrs.get('email', '')
            username = attrs.get('username', '')

            if not username.isalnum():
                raise serializers.ValidationError('The username should only contain alphanumeric characters')
            return attrs

        def create(self, validated_data):
            return User.objects.create_user(**validated_data)


class EmailVerificationSerializer(serializers.ModelSerializer):
    token = serializers.CharField(max_length=555)

    class Meta:
        model = User
        fields = ['token']
