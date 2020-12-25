# Create your models here.
from django.db import models

from simple_history.models import HistoricalRecords

# Create your models here.
class Documento(models.Model):
    Cuenta=models.BigIntegerField('Cuenta', null=True)
    Apellido=models.CharField('Apellido', max_length=50, null=True)
    Apellido2= models.CharField(name="Apellido 2", max_length=50, null=True)
    Nombre= models.CharField( max_length=50, null=True)
    Carrera= models.CharField( max_length=50, null=True)
    Generacion=models.IntegerField(name="Gen", null=True)
    Correo=models.EmailField(max_length=254, null=True)
    Modalidad=models.CharField(name='Mod', max_length=50, null=True, )
    Examen1=models.FloatField(name='Examen1', null=True, blank=True)
    Examen2=models.FloatField(name='Examen2', null=True, blank=True)
    Examen3=models.FloatField(name='Examen3', null=True, blank=True)
    Tarea_examen=models.FloatField(name='Tarea_examen', null=True, blank=True)
    Tarea1=models.FloatField(name='Tarea1', null=True, blank=True)
    Tarea2=models.FloatField(name='Tarea2', null=True, blank=True)
    Tarea3=models.FloatField(name='Tarea3', null=True, blank=True)
    DataCamp=models.FloatField(name='DataCamp', null=True, blank=True)
    Puntos_Extras=models.FloatField(name='Puntos_Extras', null=True,blank=True)
    Equipo=models.SmallIntegerField(name='Equipo', null=True, blank=True )


    paginate_by = 10

    def promedio_tarea(self):
        if self.Tarea1:
            a=self.Tarea1
        else:
            a=0
        if self.Tarea2:
            b=self.Tarea2
        else:
            b=0
        if self.Tarea3:
            c=self.Tarea3
        else:
            c=0
        final=(a+b+c)/3
        return(round(final,2))


    def promedio_examen(self):
        if self.Examen1:
            a=self.Examen1
        else:
            a=0
        if self.Examen3:
            b=self.Examen3
        else:
            b=0
        if self.Examen3:
            c=self.Examen3
        else:
            c=0
        if self.Tarea_examen:
            d=self.Tarea_examen
        else:
            d=0
        final= (a+b+c+d)/4   
        return(round(final,2))

    def promedio_final(self):
        if self.Tarea1:
            a=self.Tarea1
        else:
            a=0
        if self.Tarea2:
            b=self.Tarea2
        else:
            b=0
        if self.Tarea3:
            c=self.Tarea3
        else:
            c=0
        if self.Examen1:
            d=self.Examen1
        else:
            d=0
        if self.Examen3:
            e=self.Examen3
        else:
            e=0
        if self.Examen3:
            f=self.Examen3
        else:
            f=0
        if self.Tarea_examen:
            g=self.Tarea_examen
        else:
            g=0    
        if self.Puntos_Extras:
            h=self.Puntos_Extras
        else:
            h=0    
        if self.DataCamp:
            i=self.DataCamp
        else:
            i=0    

        final=((((a+b+c)/3)*0.4)+(((d+e+f+g))/4)*.6)+h+i
    
        
        return (round(final,2))




    class Meta:
        ordering = ['Apellido','-Equipo',]
        verbose_name = "Alumnos"

    def __str__(self):
        return self.Apellido + " " +self.Nombre 
""" 
class UserListView(ListView):
    model = Documento
    template_name = 'proba1/passwords.html'  # Default: <app_label>/<model_name>_list.html
    context_object_name = 'alumnitos'  # Default: object_list
    paginate_by = 10
    queryset = Documento.objects.all()  

    


     """