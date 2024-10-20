from django.shortcuts import render
from .models import Alumno_T

# Create your views here.
def index_vista(request):
    losalumnos=Alumno_T.objects.all()
    # contexto={"losalumnos":losalumnos}
    return render(request,'index.html',{"losalumnos":losalumnos})