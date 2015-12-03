from django.views.generic import ListView, TemplateView
from .models import Opportunity


class HomepageView(TemplateView):
    template_name = "base_home.html"


class OpportunityListView(ListView):
    model = Opportunity
