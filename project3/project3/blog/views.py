from django.contrib.auth.models import User
from django.shortcuts import render
from django.views.generic import DetailView, ListView
from django.utils import timezone

from .models import Category, Post


class PostView(DetailView):
    model = Post


class PostListView(ListView):
    model = Post
    paginate_by = 10

    def get_queryset(self):
        return Post.objects.filter(active=True, pub_date__lte=timezone.now()).order_by('-pub_date')

class CategoryPostList(ListView):
    model = Post
    paginate_by = 10
    template_name = "blog/post_list.html"

    def get_queryset(self):
        category = Category.objects.get(slug=self.kwargs.get('slug'))
        return Post.objects.filter(categories__in=[category], active=True, pub_date__lte=timezone.now())

    def get_context_data(self, *args, **kwargs):
        context = super(CategoryPostList, self).get_context_data(*args, **kwargs)
        context['is_category'] = True
        context['category'] = Category.objects.get(slug=self.kwargs.get('slug'))
        return context


class SearchView(ListView):
    '''
        Disclaimer: This is not a great search view.
    '''
    model = Post
    paginate_by = 10

    def get_queryset(self):
        if self.request.GET.get('q'):
            return Post.objects.filter(title__icontains=self.request.GET.get('q')).order_by('-pub_date')
        else:
            return Post.objects.none()

    def get_context_data(self, *args, **kwargs):
        context = super(SearchView, self).get_context_data(*args, **kwargs)
        context['search'] = True
        return context


class UserView(ListView):
    model = Post
    paginate_by = 10

    def get_queryset(self):
        return Post.objects.filter(author__username=self.kwargs.get('user')).order_by('-pub_date')

    def get_context_data(self, *args, **kwargs):
        context = super(UserView, self).get_context_data(*args, **kwargs)
        context['user_obj'] = User.objects.get(username=self.kwargs.get('user'))
        return context
