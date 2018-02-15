from django.contrib.auth.models import User, Permission

from rest_framework.authentication import (SessionAuthentication,
                                           BasicAuthentication)
from rest_framework import generics, permissions, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView


from .models import Asset, Bug
from .permissions import UsersPermission
from .serializers import (AssetSerializer, BugSerializer, UserSerializer)
from . import utils


class AssetList(generics.ListCreateAPIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated, UsersPermission)

    queryset = Asset.objects.all()
    serializer_class = AssetSerializer


class AssetDetails(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated, UsersPermission)

    queryset = Asset.objects.all()
    serializer_class = AssetSerializer


class BugList(generics.ListCreateAPIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)

    queryset = Bug.objects.all()
    serializer_class = BugSerializer


class BugDetails(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)

    queryset = Bug.objects.all()
    serializer_class = BugSerializer


class UserList(generics.ListCreateAPIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)

    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetails(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)

    queryset = User.objects.all()
    serializer_class = UserSerializer


class PermissionList(APIView):

    def get(self, request, format=None):
        return Response(utils.PERMISSIONS)


class AssignPermissions(viewsets.ViewSet):
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        if ((request.user.is_staff or request.user.is_superuser) and
                request.user.is_active):
            data = request.data
            print (">>"*10, data)
            if data:
                utils.assign_permission(data['user_id'], data['model'], data['model_id'], data['permission'])
            return Response(status=status.HTTP_201_CREATED)