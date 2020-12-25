from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
import random
from sklearn.datasets import load_iris
import pandas as pd
import csv
from .models import Documento



from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.
def home(request):
    return render(request, 'proba1/home.html')



   

def password(request):

    alumnos=Documento.objects.all()


    



    """ characters = list('abcdefghijklmnopqrstuvwxyz')
    hola="hola"

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()'))
    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))

    length = int(request.GET.get('length',12))
    thepassword = ''
    thepassword2 = ''
    for x in range(length):
        thepassword += random.choice(characters)
        thepassword2 = 'adiós'
    if request.GET.get('numero1'):
        numero1=request.GET.get('numero1')
    if request.GET.get('numero2'):
        numero2=request.GET.get('numero2')
    
    if request.GET.get('numero1'):
        numero1=request.GET.get('numero1')
    else:
        numero1=0
    if request.GET.get('numero2'):
        numero2=request.GET.get('numero2')
    else:
        numero2=0

    

    
    suma=int(numero1)+int(numero2)
    multiplicacion=int(numero1)*int(numero2)
    data = load_iris()
    df = pd.DataFrame(data.data, columns=data.feature_names)
    df=df.rename(columns={"sepal length (cm)": "uno", 
                            "sepal width (cm)": "dos",
                            "petal length (cm)":"tres",
                            "petal width (cm)":"cuatro"})
    

    alldata=[]
    for i in range(df.shape[0]):
        temp=df.iloc[i]
        alldata.append(dict(temp))
    
    l=df.shape[0]
    h=[]
    for i in range(l):
        h.append(i)
    
    df = pd.DataFrame(list(Documento.objects.all().values()))
    df2=df.columns
    print(df.columns)
    califfinal=df['Calif']+10
     """
    

    return render(request, 'proba1/password.html', {'alumnos':alumnos,
    
    
    })
