from core.models import Contact
from django import forms

class ContactForm(forms.ModelForm):

	class Meta:
		exclude = []
		model = Contact
