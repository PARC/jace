from django.conf.urls import url

from communications import views

urlpatterns = [
    url(r'^users/$', views.user_list),
    url(r'^users/(?P<pk>[0-9]+)/$', views.user_detail),
]