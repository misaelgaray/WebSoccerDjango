from django.shortcuts import render
from appModels.models import Equipos, Jugador
from forms import JugadorForm

def main_page(request):
	equipos = Equipos.objects.all()
	return render(request,'index.html',{'equipos' : equipos})

def ame_page(request, param):
	#Elemntos de Busqueda para llenar plantilla
	equipo = Equipos.objects.filter(id=param)
	equipos = Equipos.objects.all()
	jugadores = Jugador.objects.filter(id_equipo=param)

	#formulario jugadores
	form = JugadorForm()

	#bander validacion
	error =False

	if request.POST:
		valid_form = JugadorForm(request.POST)
		if valid_form.is_valid():
			valid_form.save()
			return render(request,'ame.html',{'equipos' : equipos, 'equipo': equipo, 'jugadores': jugadores, 'form':form})
		else:
			error= True
	else:
		valid_form = JugadorForm()
	
	
	return render(request,'ame.html',{'equipos' : equipos, 'equipo': equipo, 'jugadores': jugadores, 'form':form, 'error': error})

#def process_form(request):




	
	
