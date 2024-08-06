from django.shortcuts import render
from .serializers import *
from rest_framework import status, generics, permissions
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from knox.views import LoginView as KnoxLoginView
from rest_framework.authtoken.serializers import AuthTokenSerializer
from django.contrib.auth import authenticate, login


# Create your views here.

class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)


class RegisterUserAPI(generics.GenericAPIView):
    serializer_class = UserRegisterSerializer

    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        user = User.objects.get(username=serializer.data['username'])
        token_obj, _ = Token.objects.get_or_create(user=user)
        return Response({'status': 200, 'payload': serializer.data, 'token': str(token_obj)})


class UserLoginAPIView(APIView):

    def post(self, request, *args, **kargs):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            response = {
                "username": {
                    "detail": "User Doesnot exist!"
                }
            }
            if User.objects.filter(username=request.data['username']).exists():
                user = User.objects.get(username=request.data['username'])
                token, created = Token.objects.get_or_create(user=user)
                response = {
                    'success': True,
                    'username': user.username,
                    'email': user.email,
                    'token': token.key
                }
                return Response(response, status=status.HTTP_200_OK)
            return Response(response, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
