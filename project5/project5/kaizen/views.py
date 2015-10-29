from django.core.urlresolvers import reverse
from django.views.generic import CreateView, DetailView, DeleteView, ListView, UpdateView
from .models import Category, Suggestion


class CategoryListView(ListView):
    def get_queryset(self, *args, **kwargs):
        return Category.objects.all()


class CategoryCreateView(CreateView):
    model = Category
    fields = ('name', )

    def get_success_url(self):
        return "{0}?cat={1}".format(reverse('suggestion-list'), self.object.pk)


class SuggestionListView(ListView):
    def get_queryset(self, *args, **kwargs):
        if self.request.GET.get('cat'):
            try:
                return Suggestion.objects.filter(categories__in=[Category.objects.get(pk=self.request.GET.get('cat'))]).order_by('-timestamp')
            except Category.DoesNotExist:
                return Suggestion.objects.none()
        return Suggestion.objects.all().order_by('-timestamp')

    def get_context_data(self, *args, **kwargs):
        context = super(SuggestionListView, self).get_context_data(*args, **kwargs)
        try:
            context['category'] = Category.objects.get(pk=self.request.GET.get('cat'))
        except Category.DoesNotExist:
            pass
        return context


class MySuggestionsView(ListView):
    def get_queryset(self, *args, **kwargs):
        try:
            return Suggestion.objects.filter(user=self.request.user).order_by('-timestamp')
        except:
            return Suggestion.objects.none()

    def get_context_data(self, *args, **kwargs):
        context = super(MySuggestionsView, self).get_context_data(*args, **kwargs)
        context['my_suggestions'] = True
        return context


class SuggestionView(DetailView):
    model = Suggestion


class SuggestionCreateView(CreateView):
    model = Suggestion
    fields = ('title', 'description', 'categories')

    def get_initial(self, *args, **kwargs):
        initial = super(SuggestionCreateView, self).get_initial(*args, **kwargs)
        initial.update(**self.request.GET.dict())
        from pprint import pprint
        pprint(initial)
        return initial

    def get_success_url(self):
        return reverse('suggestion-detail', args=(self.object.pk, ))

    def form_valid(self, form):
        idea = form.save(commit=False)
        idea.user = self.request.user
        idea.save()
        return super(SuggestionCreateView, self).form_valid(form)


class SuggestionUpdateView(UpdateView):
    model = Suggestion
    fields = ('title', 'description', 'categories')

    def get_success_url(self):
        return reverse('suggestion-detail', args=(self.object.pk, ))


class SuggestionDeleteView(DeleteView):
    model = Suggestion

    def get_success_url(self):
        return reverse('suggestion-list')
