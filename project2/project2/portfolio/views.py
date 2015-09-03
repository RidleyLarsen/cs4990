from django.shortcuts import render
from django.views.generic import DetailView, ListView

from .models import PortfolioEntry

class HomepageView(ListView):
    model = PortfolioEntry
    template_name = "base_home.html"

class EntryView(DetailView):
    model = PortfolioEntry
    template_name = "portfolio/entry_detail.html"
