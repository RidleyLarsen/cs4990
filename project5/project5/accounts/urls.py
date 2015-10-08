from django.conf.urls import patterns, url

from .views import _password_change, _login, logout_page, reset, reset_confirm, ProfileView, ProfileCreateView, ProfileUpdateView

urlpatterns = patterns(
    'project.accounts.views',
    # Examples:
    # url(r'^blog/', include('blog.urls')),
    url(r'^profile/$', ProfileView.as_view(), name="detail"),
    url(r'^create/$', ProfileCreateView.as_view(), name="create"),
    url(r'^update/$', ProfileUpdateView.as_view(), name="update"),
    url(
        r'^login/?$',
        _login,
        {
            'template_name': 'registration/login.html'
        }, name="login"
    ),
    url(r'^logout/$', logout_page, name="logout"),
    url(r'^password/reset/$', reset, name="password_reset"),
    url(r'^password/reset/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', reset_confirm, name="password_reset_confirm"),
    url(r'^password/change/$', _password_change, name="password_change"),
)

urlpatterns += patterns(
    '',

    # user forgot password
    url(r'^password/reset/done/$', 'django.contrib.auth.views.password_reset_done', name="password_reset_done"),
    url(r'^password/done/$', 'django.contrib.auth.views.password_reset_complete'),

    # user password change
    url(r'^password/done/$', 'django.contrib.auth.views.password_change_done', name="password_change_done"),
)