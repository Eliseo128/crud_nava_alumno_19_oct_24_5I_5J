from django.shortcuts import render
from .models import Alumno_T
from django.contrib import messages
from django.db.models import Q


# Create your views here.
def index_vista(request):
    losalumnos=Alumno_T.objects.all()
    
    if request.method == "POST":
        if "agregar" in request.POST:
            nombre=request.POST.get("nombre")
            correo=request.POST.get("correo")
            Alumno_T.objects.create(
                nombre=nombre,
                correo=correo
            )
            messages.success(request,"el registro del alumno fue guardado exitosamente")
        elif "actualizar" in request.POST:
            id=request.POST.get("id")
            nombre=request.POST.get("nombre")
            correo=request.POST.get("correo")
            actualiza_Alumno_t=Alumno_T.objects.get(id=id)
            actualiza_Alumno_t.nombre=nombre
            actualiza_Alumno_t.correo=correo
            actualiza_Alumno_t.save()
            messages.success(request,"el registro se actualizo exitosamente")
            
        elif "borrar" in request.POST:
            id=request.POST.get("id")
            Alumno_T.objects.get(id=id).delete()
            messages.success(request,"el registro se borro exitosamente")
            
        elif "buscar" in request.POST:
            consulta=request.POST.get("buscarconsulta")
            losalumnos=Alumno_T.objects.filter(Q(nombre__icontains=consulta) | Q(correo__icontains=consulta))
            
            
            
       
    
    return render(request,'index.html',{"losalumnos":losalumnos})