from account.serializers import UserResgistrationSerializer 
from .models import UserProfile
from rest_framework import viewsets
from rest_framework import permissions
# from . import permissions

from rest_framework import filters

class UserRegisterView(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserResgistrationSerializer
    permission_classes = (permissions.AllowAny,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)



