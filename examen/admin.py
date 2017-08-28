from django.contrib import admin
from pagedown.widgets import AdminPagedownWidget
from examen.models import *

# Register your models here.
class PreguntaAdmin(admin.ModelAdmin):
	list_display = ('id', 'pregunta', 'tema', 'capitulo')
	list_filter = ('tema',)
	list_editable = ('tema', 'capitulo')


class TemaAdmin(admin.ModelAdmin):
	list_display = ('tema', 'descripcion')


class CapituloAdmin(admin.ModelAdmin):
	list_filter = ('tema', )
	formfield_overrides = {
		models.TextField: {'widget': AdminPagedownWidget},
	}


class ExamenAdmin(admin.ModelAdmin):
	list_display = ('fecha', 'acertadas', 'erroneas', 'nota')


admin.site.register(Tema, )
admin.site.register(Capitulo, CapituloAdmin)
admin.site.register(Pregunta, PreguntaAdmin)
admin.site.register(Examen, ExamenAdmin)
admin.site.register(Errores)
admin.site.register(Oposicion)
