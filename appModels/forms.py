from django import forms
from .models import Jugador

class JugadorForm(forms.ModelForm):
	
	class Meta:
		model = Jugador
		fields = ['id_equipo','nombre_jugador', 'posicion', 'edad']

	
