from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from account.serializers import UserResgistrationSerializer, UserProfile
from rest_framework import status
from rest_framework import generics, permissions
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate



# Create your views here.

class UserRegisterView(generics.ListCreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserResgistrationSerializer
    

class UserLoginView(APIView):
    def post(self, request):
        user = authenticate(username=request.data['username'], password=request.data['password'])
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})
        else:
            return Response({'error': 'Invalid credentials'}, status=401)
 

# # class LoginView(APIView):
# #     def post(self, request):
# #         pass

        



