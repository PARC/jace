from django.conf.urls import url

from communications import views

urlpatterns = [
    url(r'^communications/$', views.user_list),
    url(r'^communications/(?P<pk>[0-9]+)/$', views.user_list),
]