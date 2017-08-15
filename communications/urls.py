from django.conf.urls import url

from communications import views

urlpatterns = [
    url(r'^users', views.user_list),
]