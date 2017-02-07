from core.models import Vestido
from django.db.models import Q

VEST_KWARGS = {'startswith':'tipo__nombre__istartswith', 'contains': 'tipo__nombre__icontains'}

class BuscadorVestidos(object):

	def formatted_kwargs(self, kwargs):
		new_kwargs = {}
		for key in kwargs.keys():
			if key in VEST_KWARGS:
				new_kwargs[VEST_KWARGS[key]] = kwargs[key][0]
			else:
				new_kwargs[key] = kwargs[key][0]
		return new_kwargs

	def get_vestidos(self, **kwargs):
		formatted_kwargs = self.formatted_kwargs(kwargs)
		if 'tipo' in formatted_kwargs:
			return Vestido.objects.filter(tipo__nombre=formatted_kwargs['tipo'])
		if 'and' in formatted_kwargs:
			and_value = formatted_kwargs.pop('and', None)
			if 'tipo__nombre__istartswith' in formatted_kwargs:
				return Vestido.objects.filter(Q(tipo__nombre__istartswith=formatted_kwargs['tipo__nombre__istartswith']) & Q(tipo__nombre__istartswith=and_value))
			elif 'tipo__nombre__icontains' in formatted_kwargs:
				return Vestido.objects.filter(Q(tipo__nombre__icontains=formatted_kwargs['tipo__nombre__icontains']) & Q(tipo__nombre__icontains=and_value))
		elif 'or' in formatted_kwargs:
			value = formatted_kwargs.pop('or', None)
			if 'tipo__nombre__istartswith' in formatted_kwargs:
				return Vestido.objects.filter(Q(tipo__nombre__istartswith=formatted_kwargs['tipo__nombre__istartswith']) | Q(tipo__nombre__istartswith=value))
			elif 'tipo__nombre__icontains' in formatted_kwargs:
				return Vestido.objects.filter(Q(tipo__nombre__icontains=formatted_kwargs['tipo__nombre__icontains']) | Q(tipo__nombre__icontains=value))
		else:
			return Vestido.objects.filter(**formatted_kwargs)
		return Vestido.objects.none()
