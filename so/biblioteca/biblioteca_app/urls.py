from django.urls import path
from . import views

urlpatterns = [
    path('introducir-libro/', views.introducir_libro),
    path('obtener-todos-libros/', views.obtener_todos_libros),
    path('borrar-libro/<int:id>/', views.borrar_libro),
]