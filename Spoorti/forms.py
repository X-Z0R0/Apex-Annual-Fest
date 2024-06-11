# forms.py
from django import forms

class ActionForm(forms.Form):
    ALLOWED_ACTIONS = ['paymentDetail', 'paymentRequest']

    action = forms.CharField()

    def clean_action(self):
        action = self.cleaned_data.get('action')
        if action not in self.ALLOWED_ACTIONS:
            raise forms.ValidationError('Invalid action')
        return action