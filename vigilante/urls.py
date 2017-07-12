from django.conf.urls import include, url
from django.contrib import admin
from examen.views import *

urlpatterns = [
    # Examples:
    # url(r'^$', 'vigilante.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', index.as_view(), name='index'),
    url(r'^panel/$', PanelView.as_view(), name='panel'),
    url(r'^panel/entrenamiento/$', entrenamiento.as_view(), name='entrenamiento'),
    url(r'^panel/entrenamiento/busca-capitulos/$', CapitulosAjaxView.as_view()),
    url(r'^panel/repaso/$', RepasoView.as_view(), name='repaso'),
    url(r'^panel/temario/$', temario.as_view(), name='temario'),
    url(r'^panel/temario/(?P<tema>\d{1,2})/$', tema, name='tema'),
    url(r'^panel/test/$', test, name='test'),
    url(r'^panel/test/corregir/$', corregir, name='corregir'),
]
