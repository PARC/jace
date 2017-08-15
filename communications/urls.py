from django.conf.urls import url

from communications import views

urlpatterns = [
    url(r'^$', views.user_list),
]