from django.shortcuts import render, render_to_response
from django.views.generic import TemplateView, ListView
from examen.models import Tema, Capitulo, Pregunta, Examen, Errores
from django.core import serializers
from django.http import HttpResponse
from django.template import RequestContext
from django.db.models import Max, Min
import random

# Create your views here.
class index(TemplateView):
	template_name = 'index.html'


class PanelView(ListView):
	template_name = 'panel.html'
	model = Examen

	def get_context_data(self, **kwargs):
		# Obtenemos el contexto
		context = super(PanelView, self).get_context_data(**kwargs)
		context['aprobados'] = Examen.objects.filter(nota__gte=50).count()
		context['realizados'] = Examen.objects.all().count()
		context['maxima'] = Examen.objects.all().aggregate(Max('nota'))
		context['minima'] = Examen.objects.all().aggregate(Min('nota'))
		return context


class temario(ListView):
	template_name = 'temario.html'
	model = Tema


def tema(request, tema):
	sig, ant = 0, 0
	antdisable = False
	sigdisable = False
	total_temas = Tema.objects.count()
	tema_actual = int(tema)
	t = Tema.objects.get(tema=tema)
	if tema_actual >= 1:
		sig = tema_actual + 1
		ant = tema_actual - 1
	if ant == 0:
		antdisable = True
	if sig >= total_temas:
		sigdisable = True
	capitulos = Capitulo.objects.filter(tema_id=tema)
	return render(request, 'tema.html', {'capitulos': capitulos, 'tema': t, 'sig': str(sig), 'ant': str(ant), 'antdisable': antdisable, 'sigdisable': sigdisable}, )


def test(request):
	i = 0
	lista = []
	random.seed()
	total = Pregunta.objects.count()

	# Obtenemos 100 numeros aleatorios de todos los registros sin repetir
	while i < 80:
		p = random.randint(1, total)
		if p not in lista:
			lista.append(p)
			i += 1
	lista.sort()
	preguntas = Pregunta.objects.filter(id__in=lista)
	return render(request, 'test.html', {'preguntas': preguntas})


def corregir(request):
	# Creo las variables que recibo del formulario
	acertadas, erroneas, no_contestadas, nota = 0, 0, 0, 0
	examen = Examen()
	Errores.objects.all().delete()
	pregunta = Pregunta()

	# Corregimos el examen y almacenamos el resultado en la BB.DD.
	if request.method == 'GET':
		for i in range(1, 81):
			error = Errores()
			id_pregunta = "id"
			id_pregunta += str(i)
			contestada = "r"
			contestada += str(i)
			correcta = "c"
			correcta += str(i)
			pregunta = Pregunta.objects.get(pk=request.GET[id_pregunta])
			if contestada in request.GET:
				if request.GET[contestada] == request.GET[correcta]:
					acertadas += 1
				else:
					erroneas += 1
					error.pregunta = pregunta.pregunta
					if pregunta.correcta == 'a':
						error.correcta = pregunta.res_a
					if pregunta.correcta == 'b':
						error.correcta = pregunta.res_b
					if pregunta.correcta == 'c':
						error.correcta = pregunta.res_c
					error.save()
			else:
				no_contestadas += 1
				error.pregunta = pregunta.pregunta
				if pregunta.correcta == 'a':
					error.correcta = pregunta.res_a
				if pregunta.correcta == 'b':
					error.correcta = pregunta.res_b
				if pregunta.correcta == 'c':
					error.correcta = pregunta.res_c
				error.save()

	errores = Errores.objects.all()
	# Calculo de la puntuacion segun convocatoria
	nota = ((acertadas - (erroneas / 2)) * 10) / 8
	examen.acertadas = acertadas
	examen.erroneas = erroneas + no_contestadas
	examen.nota = nota
	examen.save()
	contexto = {'acertadas': acertadas, 'erroneas': erroneas, 'no_contestadas': no_contestadas, 'nota': nota, 'errores': errores, }
	return render(request, 'corregir.html', contexto)


class entrenamiento(ListView):
	template_name = 'entrenamiento.html'
	model = Tema
	context_object_name = 'temas'


class RepasoView(TemplateView):
	template_name = 'repaso.html'


class CapitulosAjaxView(TemplateView):

	def get(self, request, *args, **kwargs):
		temaid = request.GET['id']
		capitulos =  Capitulo.objects.filter(tema__id=temaid)
		data = serializers.serialize('json', capitulos, fields=('titulo', 'contenido'))
		return HttpResponse(data, content_type='application/json')
