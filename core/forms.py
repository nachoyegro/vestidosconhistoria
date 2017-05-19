from core.models import Contacto, VendeTuVestido
from django import forms

class ContactForm(forms.ModelForm):
	class Meta:
		exclude = []
		model = Contacto

class VendeTuVestidoForm(forms.ModelForm):
	class Meta:
		exclude = []
		model = VendeTuVestido
