from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

# API endpoints
urlpatterns = format_suffix_patterns([
    #url(r'^$', views.api_root),
    url(r'^asset/$', views.AssetList.as_view(), name='asset-list'),
    url(r'^asset/(?P<pk>[0-9]+)/$', views.AssetDetails.as_view(),
        name='asset-detail'),

    url(r'^bug/$', views.BugList.as_view(), name='bug-list'),
    url(r'^bug/(?P<pk>[0-9]+)/$', views.BugDetails.as_view(),
        name='bug-detail'),

    url(r'^permission/$', views.PermissionList.as_view(), name='permission-list'),

    url(r'^users/$', views.UserList.as_view(), name='user-list'),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetails.as_view(),
        name='user-detail'),

    url(r'^assignperm/$', views.AssignPermissions.as_view({'post': 'create'})),

    url(r'^api-auth/', include('rest_framework.urls'))

])
