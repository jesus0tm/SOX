
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('biblioteca.urls')),
    path('api2/', include('gestor_contraseña.urls')),
]
