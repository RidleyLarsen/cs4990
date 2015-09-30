"""project4 URL Configuration

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

from inventory.views import HomepageView, CategoryDetailView, ItemDetailView, ItemQuantityAdjustView, SearchView

urlpatterns = [
    url(r'^$', HomepageView.as_view(), name="homepage"),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^category/(?P<pk>\d+)/$', CategoryDetailView.as_view(), name="category-detail"),
    url(r'^item/(?P<pk>\d+)/$', ItemDetailView.as_view(), name="item-detail"),
    url(r'^item/(?P<pk>\d+)/delta/(?P<delta>[-\w]+)/$', ItemQuantityAdjustView.as_view(), name="item-adjust-quantity"),
    url(r'search/', SearchView.as_view(), name="search"),
]
