from django.conf.urls import url

from communications import views

urlpatterns = [
    url(r'^communications/users', views.user_list),
    url(r'^communications/intervnetion', views.intervention_list),
    url(r'^communications/surveys', views.survey_list),
    url(r'^communications/questions', views.question_list),
    url(r'^communications/answers', views.answer_list),
    url(r'^communications/users/(?P<pk>[0-9]+)/$', views.user_detail),
    url(r'^communications/intervention/(?P<pk>[0-9]+)/$', views.Intervention_detail),
    url(r'^communications/survey/(?P<pk>[0-9]+)/$', views.Survey_detail),
    url(r'^communications/questions/(?P<pk>[0-9]+)/$', views.question_detail),
    url(r'^communications/answers/(?P<pk>[0-9]+)/$', views.answer_detail),
]
