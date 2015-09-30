from django.views.generic import DetailView, ListView, TemplateView, View

from django.http import HttpResponse

from .models import Category, Item
'''
    # Pages:
        Index page with a list of categories
        Clicking on a category shows you all items for that category
        Clicking +1 on an item increments the quantity available.
        Clicking on a -1 decrements the quantity for the item.
        Use ajax for form submission. A library like jQuery is completely fine.
    # Extra Credit Ideas:
        A search form
'''


class ItemQuantityAdjustView(View):
    def get(self, *args, **kwargs):
        try:
            item = Item.objects.get(pk=self.kwargs.get('pk'))
            item.quantity = item.quantity + 1 if self.kwargs.get('delta') == "up" else item.quantity - 1
            item.save()
            return HttpResponse(item.quantity, status=200)
        except:
            return HttpResponse(status=500)


class HomepageView(TemplateView):
    template_name = "base_home.html"

    def get_context_data(self, *args, **kwargs):
        context = super(HomepageView, self).get_context_data(*args, **kwargs)
        context.update({
            "categories": Category.objects.filter(parent_category=None)
        })
        return context


class ItemDetailView(DetailView):
    model = Item


class CategoryDetailView(DetailView):
    model = Category


class CategoryItemListView(ListView):
    model = Item

    def get_queryset(self, *args, **kwargs):
        return Item.objects.filter(category__pk__in=[self.kwargs.get('category_pk')])


class CategoryListView(ListView):
    model = Category


class SearchView(ListView):
    '''
        Disclaimer: This is not a great search view. It was shamelessly copied from the blog project.
    '''
    template_name = "search.html"
    model = Item
    paginate_by = 10

    def get_queryset(self):
        if self.request.GET.get('q'):
            return Item.objects.filter(name__icontains=self.request.GET.get('q'))
        else:
            return Item.objects.none()

    def get_context_data(self, *args, **kwargs):
        context = super(SearchView, self).get_context_data(*args, **kwargs)
        return context
