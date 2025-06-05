from django.db import models
from Aplicaciones.Monumentos.models import Monumento

# Create your models here.
class VisitaGuiada(models.Model):
    id=models.AutoField(primary_key=True)
    monumento = models.ForeignKey(Monumento, on_delete=models.CASCADE)
    fecha = models.CharField(max_length=300)
    guia = models.CharField(max_length=100)
    logo=models.FileField(upload_to='cargos', null=True, blank=True)
    def __str__(self):
        return f"Visita a {self.monumento.nombre} - {self.fecha}"