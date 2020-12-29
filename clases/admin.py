from .models import Clase
from django.contrib import admin

""" class ArchivoResource(resources.ModelResource):
    
       
    class Meta:
        model = Clases
        fields = ('fecha', 'titulo', 'autor',)
        
        
 """


  

admin.site.register(Clase)