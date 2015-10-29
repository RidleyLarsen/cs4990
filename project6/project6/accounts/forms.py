from django import forms
from django.contrib.auth.models import User


class ProfileForm(forms.Form):
    first_name = forms.fields.CharField(max_length=64, required=True)
    last_name = forms.fields.CharField(max_length=64, required=True)
    address_1 = forms.fields.CharField(max_length=128)
    address_2 = forms.fields.CharField(max_length=128, required=False)
    city = forms.fields.CharField(max_length=128)
    state = forms.fields.CharField(max_length=2)
    zip_code = forms.fields.CharField(max_length=32)
    phone = forms.fields.CharField(max_length=32)

    def clean(self):
        form_data = super(ProfileForm, self).clean()
        return form_data


class ProfileCreateForm(ProfileForm):
    password1 = forms.fields.CharField(label="Password", max_length=64, required=True, widget=forms.PasswordInput())
    password2 = forms.fields.CharField(label="Confirm Password", max_length=64, required=True, widget=forms.PasswordInput())
    email = forms.fields.EmailField(max_length=128, required=True)

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email__iexact=email).count() > 0:
            raise forms.ValidationError(
                'That email address is already in use. Please enter a '
                'different email address.'
            )
        return email