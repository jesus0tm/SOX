from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
# Validate that the api is working
def index(request):
    response={
        "response": "working"
    }
    return JsonResponse(response)

#def crear_contrasena():

    
# Create your views here.

