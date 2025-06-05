import os
from django.conf import settings
from django.shortcuts import render, redirect
from.models import Monumento
from django.contrib import messages
# Create your views here.
def inicio(request):
    listadoMonumento=Monumento.objects.all() 
    return render (request,"inicio.html",{'monumentos':listadoMonumento})

def nuevoMonumento(request):
    return render (request,"nuevoMonumento.html")

def guardarMonumento(request):
    nombre=request.POST["nombre"]
    descripcion=request.POST["descripcion"]
    ubicacion=request.POST["ubicacion"]
    #Subiendo archivo con parentesis
    foto=request.FILES.get("logo")
    pdf = request.FILES.get("documento_pdf")
    nuevoMonumento=Monumento.objects.create(nombre=nombre, descripcion=descripcion, ubicacion=ubicacion,logo=foto, documento_pdf=pdf)
    messages.success(request, "Monumento guardado exitosamente")
    return redirect('inicio')


def eliminarMonumento(request, id):
    monumentoEliminar = Monumento.objects.get(id=id)

    # Eliminar archivo logo si existe
    if monumentoEliminar.logo:
        if os.path.isfile(monumentoEliminar.logo.path):
            os.remove(monumentoEliminar.logo.path)

    # Eliminar archivo pdf si existe
    if monumentoEliminar.documento_pdf:
        if os.path.isfile(monumentoEliminar.documento_pdf.path):
            os.remove(monumentoEliminar.documento_pdf.path)

    # Finalmente eliminar el objeto de la base de datos
    monumentoEliminar.delete()
    return redirect('inicio')

def editarMonumento(request, id ):
    monumentoEditar=Monumento.objects.get(id=id)
    return render(request,'editarMonumento.html',{'monumentoEditar':monumentoEditar})

def procesarEdicionMonumento(request):
    id=request.POST["id"]
    nombre=request.POST["nombre"]
    descripcion=request.POST["descripcion"]
    ubicacion=request.POST["ubicacion"]
    nuevo_logo = request.FILES.get("logo")  # archivo nuevo (si se sube uno)
    monumento=Monumento.objects.get(id=id)

    monumento.nombre=nombre
    monumento.descripcion=descripcion
    monumento.ubicacion=ubicacion
    # Si se sube una nueva imagen
    if nuevo_logo:
        # Eliminar imagen anterior si existe
        if monumento.logo:
            ruta_vieja = os.path.join(settings.MEDIA_ROOT, monumento.logo.name)
            if os.path.isfile(ruta_vieja):
                os.remove(ruta_vieja)
        # Asignar nueva imagen
        monumento.logo = nuevo_logo
    # Verificar si se cargó un nuevo PDF
    if 'documento_pdf' in request.FILES:
        if monumento.documento_pdf:
            monumento.documento_pdf.delete()  # borrar PDF anterior
        monumento.documento_pdf = request.FILES['documento_pdf']
    messages.success(request, "Monumento editado exitosamente")
    monumento.save()
    return redirect('inicio')