from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import CreateView, DetailView, ListView, View
from django.core.urlresolvers import reverse
from django.utils import timezone

from .models import Choice, Question


class ChoiceVoteView(View):
    def get(self, *args, **kwargs):
        try:
            choice = Choice.objects.get(pk=self.kwargs.get('pk'))
            choice.votes = choice.votes + 1 if self.kwargs.get('vote') == "up" else choice.votes - 1
            choice.save()
            return HttpResponse(choice.votes, status=200)
        except:
            return HttpResponse(status=500)


class QuestionList(ListView):
    model = Question


class QuestionDetailView(DetailView):
    model = Question

    def get_queryset(self, *args, **kwargs):
        return Question.objects.filter(pk=self.kwargs.get('pk'))


class QuestionCreateView(CreateView):
    model = Question
    fields = ('question_text',)
    success_url = "/"

    def form_valid(self, form):
        question = form.save(commit=False)
        question.pub_date = timezone.now()
        return super(QuestionCreateView, self).form_valid(form)

class ChoiceCreateView(CreateView):
    model = Choice
    fields = ('choice_text',)

    def form_valid(self, form):
        choice = form.save(commit=False)
        choice.question = Question.objects.get(pk=self.kwargs.get('pk'))
        return super(ChoiceCreateView, self).form_valid(form)

    def get_success_url(self, *args, **kwargs):
        return reverse('question-detail', kwargs={'pk': self.kwargs.get('pk')})
