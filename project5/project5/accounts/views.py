from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth import login as login_func
from django.contrib.auth.views import login as auth_login
from django.contrib.auth.views import password_change, password_reset, password_reset_confirm
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.views.generic import DetailView
from django.views.generic.edit import FormView

from registration.views import RegistrationView
from .forms import ProfileForm, ProfileCreateForm
from .mixins import LoginRequiredMixin
from .models import Profile


def logout_page(request):
    """
    Log users out and re-direct them to the main page.
    """
    logout(request)
    return HttpResponseRedirect('/')


def _password_change(request):
    return password_change(
        request,
        template_name='registration/password_change_form.html',
        post_change_redirect=reverse('accounts:detail'),
    )


def reset_confirm(request, uidb64=None, token=None):
    return password_reset_confirm(
        request,
        template_name='registration/password_reset_confirm.html',
        uidb64=uidb64,
        token=token,
    )


def reset(request):
    return password_reset(
        request,
        template_name='registration/password_reset_form.html',
        email_template_name='registration/password_reset_email.html',
        subject_template_name='registration/password_reset_subject.txt',
        post_reset_redirect=reverse('accounts:password_reset_done')
    )


def _login(request, *args, **kwargs):
    if request.method == 'POST':
        if not request.POST.get('remember_me', None):
            request.session.set_expiry(0)
    return auth_login(request, *args, **kwargs)


class ProfileView(LoginRequiredMixin, DetailView):
    model = Profile
    template_name = "profile/detail.html"

    def get_object(self):
        if self.request.user.is_authenticated():
            return Profile.objects.get(user=self.request.user)
        else:
            return None

    def get_context_data(self, *args, **kwargs):
        context = super(ProfileView, self).get_context_data(*args, **kwargs)
        return context


class ProfileCreateView(FormView):
    form_class = ProfileCreateForm
    template_name = "profile/create.html"
    success_url = '/'

    def form_valid(self, form):
        form_data = form.cleaned_data
        email = form_data.pop('email')
        password = form_data.pop('password1')
        user_data = {
            'first_name': form_data.pop('first_name'),
            'last_name': form_data.pop('last_name'),
            'username': email,
            'email': email,
            'password': password,
        }
        form_data.pop('password2')
        user = User.objects.create_user(**user_data)
        user.save()
        form_data['user'] = user
        profile = Profile.objects.create(**form_data)
        profile.save()
        authentication = authenticate(username=email, password=password)
        login(self.request, authentication)
        return HttpResponseRedirect(reverse('accounts:detail'))


class ProfileUpdateView(LoginRequiredMixin, FormView):
    form_class = ProfileForm
    template_name = "profile/update.html"
    success_url = "/accounts/profile/"

    def get_form(self, form_class):
        user_data = Profile.objects.get(user=self.request.user).__dict__
        user_data.update({
            'first_name': (self.request.user.first_name or self.request.POST.get('first_name')),
            'last_name': (self.request.user.last_name or self.request.POST.get('last_name')),
            'email': (self.request.user.email or self.request.POST.get('email')),
        })
        return self.form_class(user_data)

    def form_valid(self, form):
        form_data = form.cleaned_data
        self.request.user.first_name = form_data.pop('first_name')
        self.request.user.last_name = form_data.pop('last_name')
        self.request.user.save()
        instance = Profile.objects.get(user=self.request.user)
        for attr, value in form_data.iteritems():
            setattr(instance, attr, value)
        instance.save()
        return HttpResponseRedirect(reverse('accounts:detail'))


class RegisterView(RegistrationView):
    def get_success_url(self, request, user):
        return reverse('home')

    def register(self, request, form):
        user = User.objects.create_user(
            username=form.cleaned_data.get('username'),
            email=form.cleaned_data.get('email'),
            password=form.cleaned_data.get('password1')
        )
        login_func(request, user)
        return user
