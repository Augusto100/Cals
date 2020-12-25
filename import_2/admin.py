from django.contrib import admin
from .models import Archivo
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from import_export.fields import Field





class ArchivoResource(resources.ModelResource):
    
       
    class Meta:
        model = Archivo
        fields = ('id', 'contenido', 'orden',)
        
        


class ArchivoAdmin(ImportExportModelAdmin):
    resource_class = ArchivoResource
    list_display = [ "contenido", ]
   
  

admin.site.register(Archivo, ArchivoAdmin)




""" class ArchivoResource(resources.ModelResource):
        
        contenido = Field(attribute='contenido', column_name='Contenido')
        orden = Field(attribute='orden', column_name='Orden')
        class Meta:
            model = Archivo """