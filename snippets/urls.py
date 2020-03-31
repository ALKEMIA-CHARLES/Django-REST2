from django.conf.urls import url
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = format_suffix_patterns([
    url(r'^$', views.api_root),
    url(r'^snippets/$', views.snippet_list.as_view(), name='snippet-list'),
    url(r'^snippets/(?P<pk>\d+)/$', views.snippet_detail.as_view(), name='snippet-detail'),
    url(r'^users/$', views.UserList.as_view(), name='user-list'),
    url(r'^users/(?P<pk>\d+)/$', views.UserDetail.as_view(), name='user-detail'),
    url(r'^snippets/(?P<pk>\d+)/highlight/$', views.SnippetHighlight.as_view(), name='snippet-highlight')
])

