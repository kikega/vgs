from django.core.urlresolvers import reverse


def menu(request):
	menu = {'menu': [{'nombre': 'Panel', 'url': reverse('panel')}, {'nombre': 'Temario', 'url': reverse('temario')}, {'nombre': 'Entrenamiento', 'url': reverse('entrenamiento')}, {'nombre': 'Test', 'url': reverse('test')}, {'nombre': 'Repaso', 'url': reverse('repaso')}, ]}
	for item in menu['menu']:
		if request.path == item['url']:
			item['active'] = True
	return menu

