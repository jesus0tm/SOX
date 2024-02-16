from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from .models import contraseñas
from django.views.decorators.csrf import csrf_exempt
import json

def mi_vista_sin_proteccion_csrf(request):
    # Tu lógica de vista aquí
    return JsonResponse("Esta vista no tiene protección CSRF.")




@csrf_exempt
def introducir_usuario(request):
    string_body = request.body.decode('utf8').replace("'", '"') 
    body = json.loads(string_body)
    nuevo_usuario = contraseñas(nombre=body['nombre'], contraseña=body['contraseña'])
    nuevo_usuario.save()
    return JsonResponse({'message': 'Contraseña introducido correctamente'})

@csrf_exempt
def borrar_usuario(request, id):
    contraseñas.objects.get(id=id).delete()
    return JsonResponse({'message': 'Contraseña eliminada correctamente'})

@csrf_exempt
def Modificar_usuario(request):
   string_body = request.body.decode('utf8').replace("'", '"') 
   body = json.loads(string_body)
   modificar = contraseñas.objects.filter(body=id['id'])
   modificar.update(body=contraseñas['contraseñas'])
