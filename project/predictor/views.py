from django.shortcuts import render
from .formularios.form import FormSuelo
from .modelo.DecisionTreeClassifier import ArbolDecision

# Create your views here.
def index(request):
    datos = []
    if request.method == 'POST':
        form = FormSuelo(request.POST)
        if form.is_valid():
            datos = getOpc(form.data)
    return render(request,'index.html',{'datos':datos})


def getOpc(data):
    modelo = ArbolDecision()

    nitrogeno = data['nitrogeno']
    fosforo = data['fosforo']
    potasio = data['potasio']
    temperatura = data['temperatura']
    humedad = data['humedad']
    ph = data['ph']
    lluvia = data['lluvia']

    return modelo.nAlternativas(
        [[nitrogeno,fosforo,potasio,temperatura,humedad,ph,lluvia]],
        3
    )