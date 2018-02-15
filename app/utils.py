import importlib
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

from rest_framework.response import Response
from rest_framework import status
from guardian.shortcuts import assign_perm


PERMISSIONS = (
       'view_asset',
       'add_asset',
       'change_asset',
       'delete_asset',
       'view_bug',
       'add_bug',
       'change_bug',
       'delete_bug',
)


def class_for_name(module_name, class_name):
    # load the module, will raise ImportError if module cannot be loaded
    module = importlib.import_module(module_name)
    # get the class, will raise AttributeError if class cannot be found
    cls = getattr(module, class_name)
    return cls


def assign_permission(user_id, model, model_id, permissions):
    try:
      user_obj = User.objects.get(id=user_id)
      model_obj = class_for_name("app.models", model.title()).objects.get(id=model_id)
      if permissions in PERMISSIONS:
          assign_perm(permissions, user_obj, model_obj)
    except ObjectDoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)