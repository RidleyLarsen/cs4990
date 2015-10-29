from django import forms
from django.forms import ModelForm

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Div, HTML, Layout, Fieldset, ButtonHolder, Submit

from .models import Event, Volunteer


class VolunteerApplication(ModelForm):
    username = forms.fields.CharField(max_length=32)
    password = forms.fields.CharField(max_length=32, widget=forms.PasswordInput())
    birthday = forms.fields.DateField()

    class Meta:
        model = Volunteer
        exclude = ('active', 'date')

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset(
                'Your Information',
                'name',
                'birthday',
                'address',
                'address_2',
                'city',
                'state',
                'zip_code',
                'phone',
                'email',
            ),
            Fieldset(
                'Emergency Contact',
                'emergency_contact',
                'emergency_contact_phone',
                'emergency_contact_relationship',
            ),
            Div('work_experience'),
            Fieldset(
                'User Details',
                'username',
                'password',
            ),
            ButtonHolder(
                Submit('submit', 'Submit Application', css_class='btn btn-primary')
            )
        )
        super(VolunteerApplication, self).__init__(*args, **kwargs)


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        exclude = ('user', )


class CalendarEventForm(forms.ModelForm):
    time_in = forms.DateTimeField(input_formats=('%m/%d/%Y %I:%M %p',))
    time_out = forms.DateTimeField(input_formats=('%m/%d/%Y %I:%M %p',), required=False)

    class Meta:
        model = Event
        fields = ('user', 'time_in', 'time_out', 'notes', )


class EventNotesForm(forms.ModelForm):
    class Meta:
        model = Event
        exclude = ('user', 'time_in', 'time_out')
