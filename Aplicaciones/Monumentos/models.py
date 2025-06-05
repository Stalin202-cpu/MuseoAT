from django.db import models

# Create your models here.
class Monumento(models.Model):
    id=models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=500)
    ubicacion = models.CharField(max_length=255)
    logo=models.FileField(upload_to='cargos', null=True, blank=True)
    documento_pdf = models.FileField(upload_to='pdfs', null=True, blank=True)
    def __str__(self):
        return self.nombre