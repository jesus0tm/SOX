from django.urls import path
from . import views

urlpatterns = [
    path('introducir-usuario/', views.introducir_usuario),
    path('Modificar-contraseña/', views.Modificar_usuario),
    path('borrar-usuario/<int:id>/', views.borrar_usuario),
]
