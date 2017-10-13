from django.shortcuts import render
from django.http import HttpResponse
from .models import Indicador
# Create your views here.

def index(request):
	listaIndicadores = Indicador.objects.all()
	context = {'listaIndicadores': listaIndicadores,}
	return render(request,'formularios/index.html', context)
	#return HttpResponse("Bienvenido a los formularios")

def grafico(request, id_grafico):
	context = {'id_grafico': id_grafico,}
	return render(request,'formularios/graficos.html', context)