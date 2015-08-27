"""project1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from polls.views import ChoiceCreateView, ChoiceVoteView, QuestionCreateView, QuestionDetailView, QuestionList

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', QuestionList.as_view(), name="home"),
    url(r'^questions/add/$', QuestionCreateView.as_view(), name="question-create"),
    url(r'^questions/(?P<pk>\d+)/$', QuestionDetailView.as_view(), name="question-detail"),
    url(r'^questions/(?P<pk>\d+)/choice/add/$', ChoiceCreateView.as_view(), name="choice-create"),
    url(r'^choice/(?P<pk>\d+)/vote/(?P<vote>[-\w]+)/$', ChoiceVoteView.as_view(), name="choice-vote"),
]
