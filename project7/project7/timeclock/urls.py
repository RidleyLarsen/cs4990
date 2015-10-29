from django.conf import settings
from django.conf.urls import patterns, url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView

from .views import Homepage, VolunteerView, VolunteerCreateView, \
    VolunteerListView, logout_page, EventDetailView, HelpView, \
    EventCalendarView, EventCreateView, EventDeleteView, EventUpdateView, EventListView, \
    ClockInView, ClockOutView, reset, reset_confirm, NotesUpdateView

admin.site.site_header = 'Volunteer Administration'
admin.autodiscover()

urlpatterns = patterns(
    '',
    # Base URLs
    url(r'^$', Homepage.as_view(), name='homepage'),
    url(
        '^register/',
        CreateView.as_view(
            template_name='register.html',
            form_class=UserCreationForm,
            success_url='/'
        )
    ),
    url(r'^accounts/login/?$', 'django.contrib.auth.views.login', {'template_name': 'registration/login.html'}, name="login"),
    url(r'^accounts/logout/?$', logout_page, name="logout"),
    url(r'^volunteer/(?P<pk>\d+)/$', VolunteerView.as_view(), name='volunteer_detail'),
    url(r'^volunteer/apply/$', VolunteerCreateView.as_view(), name='volunteer_create'),
    url(r'^volunteer/list/$', VolunteerListView.as_view(), name='volunteer_list'),
    url(r'^admin/', admin.site.urls),
    url(r'^help/', HelpView.as_view(), name="help"),

    url(r'^event/(?P<pk>\d+)/$', EventDetailView.as_view(), name="event_detail"),
    url(r'^event/add/$', EventCreateView.as_view(), name='event_create'),
    url(r'^event/update/(?P<pk>\d+)/$', EventUpdateView.as_view(), name="event_update"),
    url(r'^event/notes/(?P<pk>\d+)/$', NotesUpdateView.as_view(), name="event_notes_update"),
    url(r'^event/list/(?P<pk>\d+)/$', EventListView.as_view(), name='event_list'),
    url(r'^event/(?P<pk>\d+)/delete/$', EventDeleteView.as_view(), name="event_delete"),
    url(r'^event/calendar/', EventCalendarView.as_view(), name="event_calendar"),

    url(r'^clockin/$', ClockInView.as_view(), name='clock_in'),
    url(r'^clockout/$', ClockOutView.as_view(), name='clock_out'),

    # user forgot password
    url(r'^user/password/reset/$', reset, name="password_reset"),
    url(r'^user/password/reset/done/$', 'django.contrib.auth.views.password_reset_done', name="reset_done"),
    url(r'^user/password/reset/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', reset_confirm, name="password_reset_confirm"),
    url(r'^user/password/done/$', 'django.contrib.auth.views.password_reset_complete'),

    # user password change
    url(r'^user/password/change/$', 'django.contrib.auth.views.password_change', name="password_change"),
    url(r'^user/password/done/$', 'django.contrib.auth.views.password_change_done', name="password_change_done"),

)

if settings.DEBUG:
    # This is not suitable for production use!
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
