from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from communications import views

token = "42istheanswer"
# (?P<token>.*)
urlpatterns = [
    url(r'^reports/$', views.report_list.as_view()),
    url(r'^users/$', views.user_list.as_view()),
    url(r'^surveys/$', views.survey_list.as_view()),
    url(r'^questions/$', views.question_list.as_view()),
    url(r'^answers/$', views.answer_list.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)
