from django import forms
from leads.models import Agent

class AgenModelForm(forms.ModelForm):
    class Meta:
        model = Agent
        fields = (
            'user',

        )