from django.shortcuts import render, get_object_or_404
from .models import Clase

def clases(request):
    clases = Clase.objects.order_by('-fecha')
    return render(request, 'clases/clases.html', {'clases':clases})

def detail(request, clase_id):
    clase = get_object_or_404(Clase, pk=clase_id)
    return render(request, 'clases/detail.html',{'clase':clase})


# Create your views here.
