from django.conf.urls import url
from . import views
from rest_framework import renderers
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter

# snippet_list = SnippetViewSet.as_view({
#     'get': 'list',
#     'post': 'create'
# })
# snippet_detail = SnippetViewSet.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy'
# })
# snippet_highlight = SnippetViewSet.as_view({
#     'get': 'highlight'
# }, renderer_classes=[renderers.StaticHTMLRenderer])
# user_list = UserViewSet.as_view({
#     'get': 'list'
# })
# user_detail = UserViewSet.as_view({
#     'get': 'retrieve'
# })

urlpatterns = format_suffix_patterns([
    url(r'^$', views.api_root),
    url(r'^snippets/$', views.snippet_list.as_view(), name='snippet-list'),
    url(r'^snippets/(?P<pk>\d+)/$', views.snippet_detail.as_view(), name='snippet-detail'),
    url(r'^users/$', views.UserList.as_view(), name='user-list'),
    url(r'^users/(?P<pk>\d+)/$', views.UserDetail.as_view(), name='user-detail'),
    url(r'^snippets/(?P<pk>\d+)/highlight/$', views.SnippetHighlight.as_view(), name='snippet-highlight')
])


