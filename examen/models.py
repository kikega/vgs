from django.db import models

# Create your models here.
class Tema(models.Model):
	tema = models.IntegerField()
	categoria = models.CharField(max_length=100, blank=True, null=True)
	descripcion = models.CharField(max_length=200, blank=True)
	#pregunta = models.IntegerField(blank=True)
	#erronea = models.IntegerField(blank=True)

	class Meta:
		ordering = ['tema']

	def __str__(self):
		return '%s. %s' % (self.tema, self.descripcion)


class Capitulo(models.Model):
	id = models.AutoField(primary_key=True)
	tema = models.ForeignKey(Tema)
	capitulo = models.CharField(max_length=10)
	titulo = models.CharField(max_length=200)
	contenido = models.TextField()
	

	class Meta:
		ordering = ['capitulo']
		verbose_name = "Capitulo"
		verbose_name_plural = "Capitulos"

	def __str__(self):
		return '%s %s' % (self.capitulo, self.titulo)


class Pregunta(models.Model):
	pregunta = models.TextField(max_length=255)
	res_a = models.TextField(max_length=255)
	res_b = models.TextField(max_length=255)
	res_c = models.TextField(max_length=255)
	correcta = models.CharField(max_length=1)
	tema = models.ForeignKey('Tema')
	capitulo = models.ForeignKey('Capitulo')

	def __str__(self):
		return '%s %s %s %s' % (self.pregunta, self.res_a, self.res_b, self.res_c)


class Examen(models.Model):
	fecha = models.DateField(auto_now=True)
	acertadas = models.IntegerField()
	erroneas = models.IntegerField()
	nota = models.FloatField()

	def __str__(self):
		return str(self.fecha)


class Errores(models.Model):
	pregunta = models.TextField(null=True, max_length=255)
	correcta = models.TextField(null=True, max_length=255)

	def __str__(self):
		return '%s %s' % (self.pregunta, self.correcta)

