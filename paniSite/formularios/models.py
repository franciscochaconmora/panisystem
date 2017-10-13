from django.db import models

# Create your models here.
class Indicador(models.Model):
  indicador_text = models.CharField(max_length=200)
  fecha_publicacion = models.DateTimeField('date published')
  
  def __str__(self):
    return self.indicador_text
  
  
class Opciones(models.Model):
  indicador = models.ForeignKey(Indicador, on_delete=models.CASCADE)
  eleccion = models.CharField(max_length=200)
  cantidad = models.IntegerField(default=0)
  
  def __str__(self):
    return self.eleccion