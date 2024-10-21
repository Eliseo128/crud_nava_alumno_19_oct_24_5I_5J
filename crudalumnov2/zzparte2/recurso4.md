## Ahora nos vamos a la vista y escribimos lo siguiente

```py
from django.shortcuts import render
from .models import Alumno_T
from django.contrib import messages
# from django import Q

# Create your views here.
def index_vista(request):
    losalumnos=Alumno_T.objects.all()
    
    if request.method == "POST":
        if "agregar" in request.POST:
            nombre=request.POST.get("nombre")
            correo=request.POST.get("correo")
            losalumnos.objects.create(
                nombre=nombre,
                correo=correo
            )
            messages.success(request,"el registro del alumno fue guardado exitosamente")
    # contexto={"losalumnos":losalumnos}
    return render(request,'index.html',{"losalumnos":losalumnos})
```

## en index agregamos un if y un for de django + un div y el mensaje

```html
  <body class="bg-light">
      
      <div class="container mt-5 p-5 rounded shadow bg-white">

        <!-- if django  tabla-->
       {% if messages %}
        {% for message in messages %}
        <div class="alert alert-success text-center mb-3">
          {{message}}
        </div>
        {% endfor %}
       
       {% endif %}
```
## para el caso de actualizar en views 

```py
from django.shortcuts import render
from .models import Alumno_T
from django.contrib import messages


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
    # contexto={"losalumnos":losalumnos}
    return render(request,'index.html',{"losalumnos":losalumnos})

```
## para el caso de actualizar en index

```html
        <!--  actualizamos Alumno Modal -->
        <div class="modal fade" id="actualizarAlumnoModal_{{unalumno.id}}" tabindex="-1" aria-labelledby="actualizarAlumnoModalLabel_{{unalumno.id}}" aria-hidden="true">
          <div class="modal-dialog">
           <form action="" method="post">
            {% csrf_token %}
            <div class="modal-content">
              <div class="modal-header">
                <h5 class="modal-title fs-5" id="actualizarAlumnoModalLabel_{{unalumno.id}}">actualizar Nuevo Alumno</h5>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
              </div>
              <div class="modal-body">
                <input type="hidden" name="id" value="{{unalumno.id}}">
                <div class="">
                  <label for="nombre">Nombre del Alumno</label>
                  <input type="text" name="nombre" class="form-control"  value= "{{unalumno.nombre}}" id="nombre" required>
                </div>
                <br>
                <div class="">
                  <label for="correo">Correo del Alumno</label>
                  <input type="email" name="correo" class="form-control" value= "{{unalumno.correo}}"id="correo" required>
                </div>
        
              </div>
              <div class="modal-footer">
                <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Cerrar</button>
                <button type="submit" class="btn btn-primary" name= "actualizar">actualizar  Alumno</button>
              </div>
            </div>
           </form>
          </div>
        </div>  
```
## ahora nos vamos a la opcion borrar en views
```py
        elif "borrar" in request.POST:
            id=request.POST.get("id")
            Alumno_T.objects.get(id=id).delete()
            messages.success(request,"el registro se borro exitosamente")
```

## en index opcion buscar
```html
            <div >
                <form action="" method="post" class="d-flex">
                  <input type="search" name="buscarquery" class="form-control" placeholder="buscando ...">
                  <button class ="btn btn-success mx-2" name = "buscar">Buscar</button>
                </form>

            </div>
```

## en views opcion buscar agregamos 
- from django.db.models import Q

```py
 elif "buscar" in request.POST:
            consulta=request.POST.get("buscarconsulta")
            losalumnos=Alumno_T.objects.filter(Q(nombre__icontains=consulta) | Q(correo__icontains=consulta))

```
## en index agregamos  {% csrf_token %}

```html

         <div >
                <form action="" method="post" class="d-flex">
                  {% csrf_token %}
                  <input type="search" value="{{consulta}}" name="buscarconsulta" class="form-control" placeholder="buscando ...">
                  <button class ="btn btn-success mx-2" name = "buscar">Buscar</button>
                </form>

            </div>
```