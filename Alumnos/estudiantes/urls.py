from django.urls import path
from .views import get_alumnos
from .views import alumno

urlpatterns = [
    path('estudiantes', get_alumnos),
    path('<int:id_alumno>', alumno),
]