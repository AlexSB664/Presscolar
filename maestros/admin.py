from django.contrib import admin
from .models import grupos, maestros, DiarioTrabajo
# Register your models here.

admin.site.register(grupos)
admin.site.register(maestros)
admin.site.register(DiarioTrabajo)