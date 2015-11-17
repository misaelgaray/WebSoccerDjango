from django.db import models

#metodo para obtener la ruta donde se guardaran las mimagens
def get_upload_file_name(instance, filename):
	return 'img/%s' % (filename)

# Create your models here.
class Equipos(models.Model):
	nombre_equipo = models.CharField(max_length=50)
	puntos = models.IntegerField()
	p_jugados = models.IntegerField()
	p_ganados = models.IntegerField()
	p_empatados = models.IntegerField()
	p_perdidos = models.IntegerField()
	goles_totales = models.IntegerField()
	img_equipo = models.FileField(upload_to=get_upload_file_name,blank=True, null=True)

	def __str__(self):
		return self.nombre_equipo

class Jugador(models.Model):
	id_equipo = models.ForeignKey(Equipos)
	nombre_jugador = models.CharField(max_length=50)
	posicion = models.CharField(max_length=15)
	edad = models.IntegerField()
	goles = models.IntegerField(blank=True, null=True)
	t_amarillas = models.IntegerField(blank=True, null=True)
	t_rojas = models.IntegerField(blank=True, null=True)

	def __str__(self):
		return self.nombre_jugador

class Seleccion(models.Model):
	id_jugador = models.ForeignKey(Jugador)

