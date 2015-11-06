from django.views.generic import ListView
from .models import Pin

# Create your views here.

class PinList(ListView):
    model = Pin
