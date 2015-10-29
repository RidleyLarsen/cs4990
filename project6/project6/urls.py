"""project6 URL Configuration

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
from django.conf import settings
from django.conf.urls import include, patterns, url
from django.contrib import admin
from accounts.views import logout_page, RegisterView
from birdsong.views import CreateNoteView, FeedView, FollowProfileView, MyFeedView, NoteView, TagNoteView

import project6.accounts.urls

urlpatterns = [
    url(r'^$', MyFeedView.as_view(), name="feed"),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^profile/', include(project6.accounts.urls, namespace="profiles")),
    url(r'^profile/follow/', FollowProfileView.as_view(), name="profile-follow"),

    url(r'^accounts/logout/', logout_page, name="logout"),
    url(r'^accounts/register/', RegisterView.as_view(), name="registration_register"),
    url(r'^accounts/', include('registration.backends.simple.urls', namespace="accounts")),

    url(r'^note/add/$', CreateNoteView.as_view(), name="note-add"),
    url(r'^tag/(?P<tag>\w+)/$', TagNoteView.as_view(), name="note-by-tag"),
    url(r'^note/(?P<pk>\d+)/$', NoteView.as_view(), name="note-detail"),
]

urlpatterns += patterns('',
    (r'^%s/(?P<path>.*)$' % settings.MEDIA_URL.strip('/'),
        'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT,
         'show_indexes': True}),
)
