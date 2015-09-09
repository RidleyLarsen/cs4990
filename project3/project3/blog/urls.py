from django.conf.urls import include, url, patterns
from .views import CategoryPostList, PostView, PostListView, SearchView, UserView

urlpatterns = patterns(
    'project3.blog.views',
    url(r'^$', PostListView.as_view(), name="post-list"),
    url(r'^(?P<pk>\d+)/$', PostView.as_view(), name="post-detail"),
    url(r'^category/(?P<slug>[-\w]+)/$', CategoryPostList.as_view(), name="category-list"),
    url(r'^user/(?P<user>[-\w]+)/$', UserView.as_view(), name="user-list"),
    url(r'search/', SearchView.as_view(), name="search"),
)
