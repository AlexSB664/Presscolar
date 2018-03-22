"""prescolapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from django.contrib.auth.views import login, logout_then_login
from alumnos.views import Index, AlumnoCreate, AlumnoReporte, busquedaTurores,ReporteNoChafa, busquedaAlumno
from maestros.views import RegisterMaestro
from padres.views import LogIn, Index2
#para las fotos
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'login/', login, {'template_name': 'log/in.html'}, name='login'),
    url(r'^$',Index, name='index'),
    url(r'^index2',Index2, name='index2'),
    #url para alumnos 
    url(r'^alumnos/detalles',AlumnoReporte.as_view(),name='alumnos_reporte'),
    url(r'^alumnos/agregar',AlumnoCreate.as_view(),name='alumnos_agregar'),
    url(r'^alumnos/paginador',ReporteNoChafa.as_view(),name='alumnos_pagina'),
    url(r'^cerrar', logout_then_login, name='logout' ),
    #url(r'^alumnos/formulario/$',Alumno_Formulario, name='Alumno_Form'),
    url(r'^maestros/agregar',RegisterMaestro.as_view(),name='maestro_agregar'),
    url(r'^tutores/Alumno',RegisterMaestro.as_view(),name='maestro_agregar'),
    url(r'^tutores/busqueda',busquedaTurores,name='filtroTutores'),
    url(r'^alumnos/Buscar', busquedaAlumno, name='filtroAlumno'),

	]
#para las fotos
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
