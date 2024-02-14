from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import HttpResponse
from django.http import JsonResponse
import pdb
from django.views.decorators.csrf import csrf_exempt
import json
import requests
from prueba2.models import  registro
from django.views.decorators.csrf import csrf_exempt
from django.db import models

# Create your views here.
# Validate that the api is working
def index(request):
    response={
        "response": "working"
    }
    return JsonResponse(response)

def añadir(request):      
    string_body = request.body.decode('utf8').replace("'", '"')      
    body = json.loads(string_body)     
    #pdb.set_trace()     
    nuevo_usuario = registro(usuario=['Mola'], contraseña=['contraseña'])     
    nuevo_usuario.save()     
    #body['usuario']          
    response = {"Info": "correcta"}     
    return JsonResponse(response)

