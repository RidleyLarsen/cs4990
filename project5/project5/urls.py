"""project5 URL Configuration

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
from accounts.views import logout_page, RegisterView
from kaizen.views import CategoryCreateView, CategoryListView, MySuggestionsView, SuggestionView, SuggestionDeleteView, SuggestionCreateView, SuggestionListView, SuggestionUpdateView

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', SuggestionListView.as_view(), name="suggestion-list"),
    url(r'^comments/', include('django_comments.urls')),
    url(r'^accounts/logout/', logout_page, name="logout"),
    url(r'^accounts/register/', RegisterView.as_view(), name="registration_register"),
    url(r'^accounts/', include('registration.backends.simple.urls', namespace="accounts")),
    url(r'^kaizen/categories/$', CategoryListView.as_view(), name="category-list"),
    url(r'^kaizen/categories/add/$', CategoryCreateView.as_view(), name="category-add"),
    url(r'^kaizen/my/', MySuggestionsView.as_view(), name="my-suggestions"),
    url(r'^kaizen/add/', SuggestionCreateView.as_view(), name="suggestion-add"),
    url(r'^kaizen/(?P<pk>\d+)/$', SuggestionView.as_view(), name="suggestion-detail"),
    url(r'^kaizen/(?P<pk>\d+)/edit/', SuggestionUpdateView.as_view(), name="suggestion-update"),
    url(r'^kaizen/(?P<pk>\d+)/delete/', SuggestionDeleteView.as_view(), name="suggestion-delete"),
]
