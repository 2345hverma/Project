from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from reminders.models import Reminders


class UserSignUpForm(UserCreationForm):

    class Meta:
        model = get_user_model()
        fields = ['username', 'password1', 'password2', 'first_name', 'last_name']


class SetReminderForm(forms.ModelForm):
    date_of_reminder = forms.DateField(input_formats=['%Y-%m-%d'], widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Reminders
        fields = ['label', 'date_of_reminder', 'subject', 'description', 'email', 'contact_no', 'sms_no', 'recur_for']
        # widgets = {
        #     'date_of_reminder': forms.DateTimeInput(attrs={'type': 'date'}),
        # }

    def clean(self):
        cleaned_data = super(SetReminderForm, self).clean()
        email = cleaned_data.get('email')
        contact_no = cleaned_data.get('contact_no')
        sms_no = cleaned_data.get('sms_no')

        if not email and not contact_no and not sms_no:
            raise ValidationError('Email, Contact No. and SMS No. all cannot be empty!')

        return cleaned_data
