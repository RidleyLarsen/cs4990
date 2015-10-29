from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.views import password_reset, password_reset_confirm
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.utils import timezone
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, DeleteView, ListView,\
    TemplateView, RedirectView, UpdateView
from django.contrib.messages.views import SuccessMessageMixin

from .forms import CalendarEventForm, EventNotesForm, VolunteerApplication
from .models import Event, Volunteer

# Create your views here.


class Homepage(TemplateView):
    template_name = "home.html"


class HelpView(TemplateView):
    template_name = "help.html"


class VolunteerCreateView(CreateView):
    form_class = VolunteerApplication
    model = Volunteer
    template_name = 'application.html'

    def form_valid(self, form):
        if form.is_valid():
            cleaned_data = form.cleaned_data
        user = User.objects.create_user(
            cleaned_data['username'],
            email=cleaned_data['email'],
            password=cleaned_data['password'],
        )
        user.save()
        self.object = form.save()

        self.object.user = user
        self.object.save()
        return super(VolunteerCreateView, self).form_valid(form)


class VolunteerView(DetailView):
    model = Volunteer
    template_name = 'volunteer_detail.html'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(VolunteerView, self).dispatch(request, *args, **kwargs)


class VolunteerUpdate(UpdateView):
    model = Volunteer
    template_name = 'volunteer_update.html'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(VolunteerUpdate, self).dispatch(request, *args, **kwargs)


class VolunteerListView(ListView):
    model = Volunteer
    template_name = 'volunteer_list.html'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(VolunteerListView, self).dispatch(request, *args, **kwargs)


class EventDetailView(DetailView):
    model = Event
    template_name = 'event/detail.html'

    def get_context_data(self, **kwargs):
        context = super(EventDetailView, self).get_context_data(**kwargs)
        try:
            context['volunteer'] = Volunteer.objects.get(user=self.get_object().user)
        except:
            if self.request.user.is_staff:
                messages.error(self.request, 'You do not have volunteer information associated with your account. Please see the volunteer coordinator for assistance.')
        return context


class EventCreateView(SuccessMessageMixin, CreateView):
    model = Event
    template_name = 'event/create.html'
    form_class = CalendarEventForm
    success_url = '/event/calendar/'
    success_message = 'Event created successfully.'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(EventCreateView, self).dispatch(request, *args, **kwargs)


class EventListView(ListView):
    model = Event
    template_name = "event/list.html"

    def get_queryset(self, *args, **kwargs):
        qs = Event.objects.all()
        pk = self.kwargs.get('pk', None)
        if pk:
            qs = Event.objects.filter(user__id=pk)
        else:
            if self.request.user:
                qs = Event.objects.filter(user=self.request.user)
        if self.request.GET.get('start_date'):
            qs = qs.filter(time_in__gte=self.request.GET['start_date'])
        if self.request.GET.get('end_date'):
            qs = qs.filter(time_out__lte=self.request.GET['end_date'])

        return qs.order_by('-time_in')

    def get_context_data(self, **kwargs):
        context = super(EventListView, self).get_context_data(**kwargs)
        pk = self.kwargs.get('pk', None)
        if pk:
            context['volunteer_user'] = User.objects.get(id=pk)
            context['volunteer'] = Volunteer.objects.get(user=context['volunteer_user'])
        else:
            context['user'] = self.request.user
        if self.request.GET.get('start_date') or self.request.GET.get('end_date'):
            qs = self.get_queryset()
            (hours, minutes, seconds) = (0, 0, 0)
            for event in qs:
                duration = event.duration_tuple()
                hours += duration[0]
                minutes += duration[1]
                seconds += duration[2]
                while seconds > 60:
                    seconds -= 60
                    minutes += 1
                while minutes >= 60:
                    minutes -= 60
                    hours += 1
            context['total_hours'] = '%d hours, %d minutes, %d seconds' % (hours, minutes, seconds)
        else:
            try:
                if pk:
                    context['total_hours'] = Volunteer.objects.get(user__id=pk).total_hours
                else:
                    context['total_hours'] = Volunteer.objects.get(user=self.request.user).total_hours
            except Volunteer.DoesNotExist:
                context['total_hours'] = None
        return context


class EventCalendarView(ListView):
    model = Event
    template_name = 'event/calendar.html'

    def get_queryset(self, *args, **kwargs):
        if self.request.GET.get('no_admin'):
            return Event.objects.filter(user__is_staff=False)
        else:
            return Event.objects.all()

    def get_context_data(self, **kwargs):
        context = super(EventCalendarView, self).get_context_data(**kwargs)
        context['event_form'] = CalendarEventForm()
        return context


class EventUpdateView(UpdateView):
    model = Event
    template_name = 'event/update.html'
    form_class = CalendarEventForm
    success_url = "/event/calendar/"

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(EventUpdateView, self).dispatch(request, *args, **kwargs)


class NotesUpdateView(UpdateView):
    model = Event
    template_name = 'event/update.html'
    form_class = EventNotesForm
    success_url = "/"

    def form_valid(self, form):
        event = Event.objects.get(time_out=None, user=self.request.user)
        event.notes = form.cleaned_data.get('notes', None)
        event.save()
        messages.success(self.request, "Saved your notes successfully.")
        return HttpResponseRedirect('/')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(NotesUpdateView, self).dispatch(request, *args, **kwargs)


class EventDeleteView(DeleteView):
    model = Event
    template_name = 'event/delete.html'
    success_url = '/event/calendar/'


class ClockInView(RedirectView):
    query_string = True

    def get_redirect_url(self):
        return reverse('homepage')

    def get(self, request, *args, **kwargs):
        url = self.get_redirect_url(**kwargs)
        if request.user.is_authenticated():
            evt = Event.objects.create(user=request.user, time_in=timezone.now())
            evt.save()
            messages.success(request, 'Successfully Clocked In.')
        return HttpResponseRedirect(url)


class ClockOutView(RedirectView):
    query_string = True

    def get_redirect_url(self):
        return reverse('homepage')

    def get(self, request, *args, **kwargs):
        url = self.get_redirect_url(**kwargs)
        evt = Event.objects.filter(user=request.user, time_out=None).order_by('time_in')
        try:
            evt = evt[0]
        except IndexError:
            messages.error(request, 'Can\'t clock out if not clocked in.')
            return HttpResponseRedirect(url)
        evt.time_out = timezone.now()
        print evt.time_out
        evt.save()
        messages.success(request, 'Successfully Clocked Out.')
        return HttpResponseRedirect(url)


'''
    User
'''


def reset_confirm(request, uidb64=None, token=None):
    return password_reset_confirm(
        request,
        template_name='registration/password_reset_confirm.html',
        uidb64=uidb64,
        token=token,
        post_reset_redirect=reverse('login')
    )


def reset(request):
    return password_reset(
        request,
        template_name='registration/password_reset_form.html',
        email_template_name='registration/password_reset_email.html',
        subject_template_name='registration/password_reset_subject.txt',
        post_reset_redirect=reverse('reset_done')
    )


def logout_page(request):
    """
    Log users out and re-direct them to the main page.
    """
    logout(request)
    return HttpResponseRedirect('/')
