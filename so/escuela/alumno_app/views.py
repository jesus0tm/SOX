from django.http import JsonResponse
from .models import Alumno
from django.views.decorators.csrf import csrf_exempt
import json

def mi_vista_sin_proteccion_csrf(request):
    # Tu lógica de vista aquí
    return JsonResponse("Esta vista no tiene protección CSRF.")





@csrf_exempt
def introducir_alumno(request):
    string_body = request.body.decode('utf8').replace("'", '"') 
    body = json.loads(string_body)
    #pdb.set_trace()
    nuevo_alumno = Alumno(nombre=body['nombre'], dni=body['dni'])
    nuevo_alumno.save()
    return JsonResponse({'message': 'Alumno introducido correctamente'})

@csrf_exempt
def obtener_todos_alumno(request):
    alumno = list(Alumno.objects.values())
    return JsonResponse(alumno, safe=False)

@csrf_exempt
def borrar_alumno(request, id):
    Alumno.objects.get(id=id).delete()
    return JsonResponse({'message': 'Alumno eliminado correctamente'})