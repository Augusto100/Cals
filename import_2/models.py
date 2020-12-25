from django.db import models




# Create your models here.
class Archivo(models.Model):
    contenido=models.CharField('Contenido', max_length=50)
    orden= models.CharField('Orden', max_length=50)
    userid = models.IntegerField(primary_key=True)
    

    def __str__(self):
       return self.contenido
   

   


    