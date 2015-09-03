from django.conf.urls import include, patterns, url
from project2.portfolio.views import EntryView, HomepageView

urlpatterns = patterns(
    'project2.portfolio.views',
    url(r'^$', HomepageView.as_view(), name="homepage"),
    url(r'portfolio/(?P<pk>\d+?)/$', EntryView.as_view(), name="entry-detail")
)
