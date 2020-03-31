from django.conf.urls import url
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns =[
    url(r'^snippets/$', views.snippet_list.as_view()),
    url(r'^snippets/(?P<pk>\d+)/$', views.snippet_detail.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)