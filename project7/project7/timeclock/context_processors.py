from django.utils import timezone

from .forms import EventNotesForm
from .models import Event


def clocked_in(request):
    clocked_in = False
    event = None
    notes_form = None
    if request.user.is_authenticated():
        now = timezone.now()
        events = Event.objects.filter(user=request.user, time_in__lte=now, time_out=None)
        try:
            clocked_in = True if events[0] else False
            event = events[0]
            notes_form = EventNotesForm(instance=event)
        except Event.DoesNotExist:
            clocked_in = False
        except IndexError:
            clocked_in = False
    return {
        'clocked_in': clocked_in,
        'event': event,
        'notes_form': notes_form,
    }
