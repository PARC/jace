from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from communications import views

urlpatterns = [
    url(r'^snippets/$', views.user_list.as_view()),
    url(r'^snippets/(?P<pk>[0-9]+)/$', views.user_detail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
