
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics, status, views
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from customer.serializers import *
from customer.services import building_url_register, building_url_restore
from customer.tasks import *


class RegisterView(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user_data = serializer.data
        user = User.objects.get(email=user_data['email'])
        building_url_register(user, request)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class VerifyEmail(views.APIView):
    serializer_class = EmailVerificationSerializer
    permission_classes = [AllowAny]
    token_param_config = openapi.Parameter('token', in_=openapi.IN_QUERY, description='Description',
                                           type=openapi.TYPE_STRING)

    @swagger_auto_schema(manual_parameters=[token_param_config])
    def get(self, request):
        token = request.GET.get('token')
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=settings.SIMPLE_JWT['ALGORITHM'])
            user = User.objects.get(id=payload['user_id'])
            if not user.is_verified:
                user.is_verified = True
                user.save()
            return Response({'email': 'Successfully activated!'}, status=status.HTTP_200_OK)
        except jwt.ExpiredSignatureError as identifier:
            return Response({'error': 'Activation link expired!'}, status=status.HTTP_400_BAD_REQUEST)
        except jwt.exceptions.DecodeError as identifier:
            return Response({'error': 'Invalid token!'}, status=status.HTTP_400_BAD_REQUEST)


class ResetPasswordView(generics.GenericAPIView):
    serializer_class = PasswordCreateSerializer

    def patch(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response({'success': True, 'message': 'Password reset success '}, status=status.HTTP_200_OK)


class PasswordRestoreView(generics.GenericAPIView):
    serializer_class = PasswordRestoreSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user_data = serializer.data
        user = User.objects.get(email=user_data['email'])
        building_url_restore(user, request)
        return Response(serializer.data, status=status.HTTP_200_OK)


class EnterNewPasswordView(generics.GenericAPIView):
    serializer_class = EnterPasswordSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        token = request.GET.get('token')
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=settings.SIMPLE_JWT['ALGORITHM'])
        user = User.objects.get(id=payload['user_id'])
        user_data = serializer.data
        user.set_password(user_data.get('new_password'))
        user.save()

        return Response({'success', 'Password successfully changed!'}, 200)
