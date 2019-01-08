from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from tutorial.quickstart.serializers import UserSerialiser, GroupSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endopoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerialiser


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows grups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
