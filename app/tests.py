import json

from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

from rest_framework.test import APITestCase, APIClient

from .models import Asset, Bug
from . import utils


class CreateAPIViewTestCase(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user("admin", "admin@example.com", "rest")
        self.asset = Asset(id=1, name='Asset-1', owner=self.user, member=self.user)

    def test_list_asset_with_permission(self):
        user = User.objects.create_user("john", "john@example.com", "rest")
        utils.assign_permission(user.id, 'Asset', 1, 'view_asset')
        self.client.get('')

    def test_list_asset_without_permission(self):
        pass

    def test_list_bug_without_permission(self):
        pass

    def test_list_bug_with_permission(self):
        pass

class DetailAPIViewTestCase(APITestCase):
    pass

