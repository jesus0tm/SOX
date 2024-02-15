from django.http import JsonResponse
from .models import Libro
from django.views.decorators.csrf import csrf_exempt
import json

def mi_vista_sin_proteccion_csrf(request):
    # Tu lógica de vista aquí
    return JsonResponse("Esta vista no tiene protección CSRF.")





@csrf_exempt
def introducir_libro(request):
    string_body = request.body.decode('utf8').replace("'", '"') 
    body = json.loads(string_body)
    #pdb.set_trace()
    nuevo_libro = Libro(titulo=body['titulo'], num_paginas=body['num_paginas'])
    nuevo_libro.save()
    return JsonResponse({'message': 'Libro introducido correctamente'})

@csrf_exempt
def obtener_todos_libros(request):
    libros = list(Libro.objects.values())
    return JsonResponse(libros, safe=False)

@csrf_exempt
def borrar_libro(request, id):
    Libro.objects.get(id=id).delete()
    return JsonResponse({'message': 'Libro eliminado correctamente'})