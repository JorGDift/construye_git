from django.forms import Form
from django import forms


class QuoteUpdateForm(Form):
    status = forms.BooleanField()

