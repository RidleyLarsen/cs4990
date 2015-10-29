from django.http import HttpResponse
from django.views.generic import CreateView, ListView, DetailView, View
from django.contrib import messages
from project6.accounts.models import Profile
from .models import Note



class FeedView(ListView):
    template_name = "birdsong/feed.html"

    def get_context_data(self, *args, **kwargs):
        context = super(FeedView, self).get_context_data(*args, **kwargs)
        context.update(**self.kwargs)
        return context

    def get_queryset(self, *args, **kwargs):
        return Note.objects.all()


class MyFeedView(ListView):
    template_name = "birdsong/user_feed.html"
    model = Note

    def get_context_data(self, *args, **kwargs):
        context = super(MyFeedView, self).get_context_data(*args, **kwargs)
        context['user'] = self.request.user.username
        return context

    def get_queryset(self, *args, **kwargs):
        if self.request.user.is_authenticated():
            profile = Profile.objects.get(user=self.request.user)
            profiles = list(profile.following.all())
            profiles.append(profile)
            return Note.objects.filter(profile__in=profiles).order_by('-timestamp')
        else:
            return Note.objects.all().order_by('-timestamp')


class TagNoteView(ListView):
    template_name = "birdsong/tag_notes.html"

    def get_queryset(self, *args, **kwargs):
        return Note.objects.filter(tags__name__in=[self.kwargs.get('tag')])

    def get_context_data(self, *args, **kwargs):
        context = super(TagNoteView, self).get_context_data(*args, **kwargs)
        context.update(**self.kwargs)
        return context


class NoteView(DetailView):
    model = Note

    def get_object(self, queryset=None):
        raise NotImplementedError


class CreateNoteView(CreateView):
    model = Note
    fields = ('text', )

    def form_valid(self, form):
        note = form.save(commit=False)
        reply_pk = self.request.GET.get('r', None)
        if reply_pk:  # Reply
            note.reply_to = Note.objects.get(pk=reply_pk)
        note.profile = Profile.objects.get(user=self.request.user)
        note.save()
        messages.success(self.request, "Duly noted.")
        return HttpResponse(status=200)


class FollowProfileView(View):
    def post(self, request, *args, **kwargs):
        profile = Profile.objects.get(user=request.user)
        if (request.POST.get('follow', None)):
            profile.following.add(Profile.objects.get(user__pk=request.POST.get('user_pk')))
        else:
            profile.following.remove(Profile.objects.get(user__pk=request.POST.get('user_pk')))
        profile.save()
        return HttpResponse(status=200)
