from django.contrib import admin
from AppSeminario.models import Inscritos, Institucion
# Register your models here.

class InscritosAdmin(admin.ModelAdmin):
    list_display = ['nombre']

admin.site.register(Inscritos, InscritosAdmin)

class InstitucionAdmin(admin.ModelAdmin):
    list_display = ['institucion']

admin.site.register(Institucion, InstitucionAdmin)