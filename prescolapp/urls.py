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
from django.conf.urls import url, include
from django.contrib.auth.views import logout_then_login
from alumnos.views import Index, AlumnoCreate, AlumnoReporte, busquedaTurores,ReporteNoChafa, busquedaAlumno,Detail_ninja, Update_Alumno, Detail_Alumno, AgregarAlumConEstilo, EvaluarAlumno
from maestros.views import agregarMaestro, actualizarMaestro, MaestroReporte, buscarMaestros,DetalleMaestro, crearGrupo, buscarSinGrupo, buscarGrupo, GrupoReporte, infoGrupo, actualizaGrupo,buscarEnelGrupo
from padres.views import LogIn, Index2, login, addTutor, tutorAsign,updateTutores, TutoresReporte, Detail_Tutor, ActualizarTutores
#para las fotos
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'login/', login, name='login'),
    url(r'^$',Index, name='index'),
    url(r'^index2',Index2, name='index2'),
    #url para alumnos 
    url(r'^alumnos/detalles/',AlumnoReporte.as_view(),name='alumnos_reporte'),
    url(r'^alumnos/agregar/',AgregarAlumConEstilo.as_view(),name='alumnos_agregarxd'),
    #url(r'^alumnos/agregar2',AlumnoCreate.as_view(),name='alumnos_agregar'),
    url(r'^alumnos/paginador/',ReporteNoChafa.as_view(),name='alumnos_pagina'),
    url(r'^cerrar', logout_then_login, name='logout' ),
    #url(r'^maestros/agregar', StudentSignUpView.as_view(), name='student_signup'),
    url(r'^tutores/busqueda/',busquedaTurores,name='filtroTutores'),
    url(r'^alumnos/Buscar/', busquedaAlumno, name='filtroAlumno'),
    path('detalleAlumno/<slug:slug>', Detail_ninja.as_view(), name='detail_view' ),
    path('maestros/nuevo/', agregarMaestro.as_view(), name="add_teacher"),
    url(r'^padres/agregar/', addTutor.as_view(), name="AddTutor"),
    path('updateAlumno/<slug:slug>', Update_Alumno.as_view(), name="UpdateAlumno"),
    path('detalles/<slug:slug>', Detail_Alumno.as_view()),
    path('evaluar/<slug:slug>', EvaluarAlumno.as_view()),
    path('addtutor/<slug:slug>', tutorAsign),
    path('Actualizar/Tutores', updateTutores),
    path('tutor/buscar', TutoresReporte.as_view(), name='filtroTutor'),
    path('detalles/tutor/<slug:slug>', Detail_Tutor),
    path('actualiza/tutor/<slug:slug>', ActualizarTutores),
    path('actualiza/maestro/<slug:slug>',actualizarMaestro),
    path('maestro/buscar', MaestroReporte.as_view(), name='reporteMaestro'),
    path('detalles/maestro/<slug:slug>', DetalleMaestro),
    path('maestros/busqueda/', buscarMaestros),
    path('grupo/crear', crearGrupo, name='crearGrupo'),
    path('alumnosNG/busqueda/', buscarSinGrupo),
    path('grupos/busqueda/', buscarGrupo),
    path('grupo/buscar', GrupoReporte.as_view(), name='reporteGrupo'),
    path('detalles/grupos/<slug:slug>',infoGrupo),
    path('actualiza/grupo/<slug:slug>', actualizaGrupo ),
    path('buscar/alumnosSG/<slug:slug>/', buscarEnelGrupo),
	]
#para las fotos
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
