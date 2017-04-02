from core.models import Contacto, VendeTuVestido
from django import forms
from django.core.mail import send_mail

class ContactForm(forms.ModelForm):

	def clean(self):
		cd = super(ContactForm, self).clean()
		import pdb;pdb.set_trace()
		if not self.errors:
			send_mail(
			    'Subject here',
			    'Here is the message.',
			    'from@example.com',
			    ['nachoyegro@gmail.com'],
			    fail_silently=False,
			)
		return cd

	class Meta:
		exclude = []
		model = Contacto

class VendeTuVestidoForm(forms.ModelForm):
	class Meta:
		exclude = []
		model = VendeTuVestido
