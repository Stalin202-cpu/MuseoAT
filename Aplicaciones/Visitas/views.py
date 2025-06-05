import os
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render,redirect
from.models import VisitaGuiada
from Aplicaciones.Monumentos.models import Monumento
from django.contrib import messages

# Create your views here.
def inicio2(request):
    listadoVisitas = VisitaGuiada.objects.all()
    return render(request, "inicio2.html", {'visitas': listadoVisitas})

def nuevaVisita(request):
    monumentos = Monumento.objects.all()
    return render(request, "nuevaVisita.html", {'monumentos': monumentos})


def guardarVisita(request):
    if request.method == "POST":
        monumento_id = request.POST.get("monumento")  # en vez de request.POST["monumento"]
        fecha = request.POST.get("fecha")
        guia = request.POST.get("guia")
        foto=request.FILES.get("logo")
        if not monumento_id:
            return HttpResponse("Error: Monumento no seleccionado", status=400)

        # Aquí puedes guardar la visita
        from .models import VisitaGuiada, Monumento
        monumento = Monumento.objects.get(pk=monumento_id)
        VisitaGuiada.objects.create(monumento=monumento, fecha=fecha, guia=guia,logo=foto)
        messages.success(request, "Visita guardado exitosamente")
        return redirect('/inicio2')
    
def eliminarVisita(request, id):
    visita = VisitaGuiada.objects.get(id=id)
    visita.delete()
    return redirect('/inicio2')

def editarVisita(request, id):
    visita = VisitaGuiada.objects.get(id=id)
    monumentos = Monumento.objects.all()
    return render(request, "editarVisita.html", {'visita': visita, 'monumentos': monumentos})

def procesarEdicionVisita(request):
    id = request.POST["id"]
    fecha = request.POST["fecha"]
    guia = request.POST["guia"]
    monumento_id = request.POST["monumento"]
    nuevo_logo = request.FILES.get("logo")  # archivo nuevo (si se sube uno)
    visita = VisitaGuiada.objects.get(id=id)
    visita.fecha = fecha
    visita.guia = guia
    visita.monumento = Monumento.objects.get(id=monumento_id)

# Si se sube una nueva imagen
    if nuevo_logo:
        # Eliminar imagen anterior si existe
        if visita.logo:
            ruta_vieja = os.path.join(settings.MEDIA_ROOT, visita.logo.name)
            if os.path.isfile(ruta_vieja):
                os.remove(ruta_vieja)
        # Asignar nueva imagen
        visita.logo = nuevo_logo
    messages.success(request, "Visita editado exitosamente")
    visita.save()
    return redirect('/inicio2')