from django.http import JsonResponse
from .models import Libro

def introducir_libro(request):
    Libro.objects.create(titulo=request.POST['titulo'], num_paginas=request.POST['num_paginas'])
    return JsonResponse({'message': 'Libro introducido correctamente'}, status=201)

def obtener_todos_libros(request):
    libros = list(Libro.objects.values())
    return JsonResponse(libros, safe=False)

def borrar_libro(request, id):
    try:
        Libro.objects.get(id=id).delete()
        return JsonResponse({'message': 'Libro eliminado correctamente'}, status=204)
    except Libro.DoesNotExist:
        return JsonResponse({'error': 'El libro no existe'}, status=404)