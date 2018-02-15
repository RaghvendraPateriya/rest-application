from rest_framework.permissions import BasePermission

from .models import Asset, Bug


class UsersPermission(BasePermission):
    """
    Object-level permission to only.
    Assumes the model instance has an `owner` attribute.
    """

    def has_permission(self, request, view):
        print ("--"*20)
        print (request.user)
        print (request.user.id)
        print (request.method, view.__class__.__name__)
        if request.method == "GET":
            if view.__class__.__name__ in ['AssetList']:
                return request.user.has_perm('view_asset', Asset)
            elif view.__class__.__name__ in ['BugList']:
                request.user.has_perm('view_bug', Bug)
        elif request.method == "POST":
            if view.__class__.__name__ in ['AssetDetails']:
                return request.user.has_perm('change_asset', Asset)
            elif view.__class__.__name__ in ['BugDetails']:
                return request.user.has_perm('change_bug', Bug)
        else:
            return False
