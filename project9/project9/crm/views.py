from django.views.generic import ListView
from .models import Opportunity


class OpportunityListView(ListView):
    model = Opportunity
