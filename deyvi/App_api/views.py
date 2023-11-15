from typing import Any
from django import http
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json
from django.shortcuts import render, get_object_or_404
from .models import Estudiante


def crear_estudiante(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        grupo = request.POST.get('grupo')
        año = request.POST.get('año')
        Estudiante.objects.create(nombre=nombre, grupo=grupo, año=año)
        return JsonResponse({'message': 'Estudiante creado exitosamente'})
    else:
        return JsonResponse({'message': 'Método no permitido'}, status=405)

def leer_estudiantes(request):
    estudiantes = Estudiante.objects.all()
    data =[]
    for i in estudiantes :
        data.append(i)
    return JsonResponse(data, safe=False)

def actualizar_estudiante(request, id):
    estudiante = get_object_or_404(Estudiante, pk=id)
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        grupo = request.POST.get('grupo')
        año = request.POST.get('año')
        estudiante.nombre = nombre
        estudiante.grupo = grupo
        estudiante.año = año
        estudiante.save()
        return JsonResponse({'message': 'Estudiante actualizado exitosamente'})
    else:
        return JsonResponse({'message': 'Método no permitido'}, status=405)

def eliminar_estudiante(request, id):
    estudiante = get_object_or_404(Estudiante, pk=id)
    estudiante.delete()
    return JsonResponse({'message': 'Estudiante eliminado exitosamente'})

# Create your views here.
