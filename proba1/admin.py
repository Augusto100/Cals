
# Register your models here.
from django.contrib import admin
from .models import Documento
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from import_export.fields import Field




class ArchivoResource(resources.ModelResource):
    
    
    class Meta:
        model = Documento
        fields = ('id','Cuenta', 'Apellido', 'Apellido 2','Nombre','Carrera','Gen','Mod', 'Correo','Calif')
        
        


class ArchivoAdmin(ImportExportModelAdmin):

    resource_class = ArchivoResource
    list_display=('Apellido','Nombre', 'Cuenta')
    search_fields=('Apellido','Nombre', 'Cuenta')
    list_filter=('Equipo',)


    




admin.site.register(Documento, ArchivoAdmin)





""" class ArchivoResource(resources.ModelResource):
        
        contenido = Field(attribute='contenido', column_name='Contenido')
        orden = Field(attribute='orden', column_name='Orden')
        class Meta:
            model = Archivo """