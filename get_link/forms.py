from django import forms

# Create your forms here.

class FormGetLink(forms.Form):
    url_address = forms.URLField()
