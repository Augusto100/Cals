from django.db import models

# Create your models here.
class Clase(models.Model):
    Autores = [
    ('Augusto', 'Augusto'),
    ('Alex', 'Alex'),
    ('Mani', 'Mani'),
   
    ]

    titulo = models.CharField('titulo',max_length=100,null=True)
    fecha=models.DateField( auto_now=False, auto_now_add=False, null=True)
    autor =models.CharField(choices=Autores, max_length=50, null=True)
    descripcion = models.CharField( max_length=50, null=True)
    pdf = models.FileField(upload_to='static/media', null=True)

    def __str__(self):
        return self.titulo 
    

