from django import forms
from django.forms import ModelForm
from .models import Contact

class Contactform(ModelForm):
	class Meta:
		model=Contact
		fields = ['fname', 'lname', 'email', 'message']

