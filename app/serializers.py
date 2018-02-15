from django.contrib.auth.models import User, Permission
from rest_framework import serializers

from .models import Asset, Bug


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class AssetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Asset
        fields = '__all__'


class BugSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Bug
        fields = '__all__'
