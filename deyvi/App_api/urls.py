
from App_api import views
from django.urls import path
from .views import crear_estudiante, leer_estudiantes, actualizar_estudiante, eliminar_estudiante
urlpatterns = [
    path('crear/', crear_estudiante, name='crear_estudiante'),
    path('leer/', leer_estudiantes, name='leer_estudiantes'),
    path('actualizar/<int:id>/', actualizar_estudiante, name='actualizar_estudiante'),
    path('eliminar/<int:id>/', eliminar_estudiante, name='eliminar_estudiante'),
]