from django import forms
from django.core.validators import EmailValidator

class SubmissionForm(forms.Form):
	name = forms.CharField(label="Name: ", max_length=100, required=True)
	email = forms.CharField(label="Mail: ", max_length=50, required=True, validators=[EmailValidator()])
