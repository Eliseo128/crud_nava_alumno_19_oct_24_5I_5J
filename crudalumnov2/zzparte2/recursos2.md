en views agregamos el modelo alumno_T + codigo


```python
from django.shortcuts import render
from .models import Alumno_T

# Create your views here.
def index_vista(request):
    losalumnos=Alumno_T.objects.all()
    contexto={"losalumnos":losalumnos}
    return render(request,'index.html',contexto=contexto)
```
de la tabla borramos 2 tr cortar ctrl x  y agregamos un un ciclo for en el primer tr
- asi queda
```html
       <!-- Modal  tabla-->
       <table class="table mt-3 table-bordered" >
        <thead>
          <tr>
            <th scope="col">ID</th>
            <th scope="col">Nombre Alumno</th>
            <th scope="col">Correo Alumno</th>
            <th scope="col">Accion</th>
          </tr>
        </thead>
        <tbody>
          {% for unalumno in  losalumnos %}
          <tr>
            <th>{{unalumno.id}}</th>
            <td>{{unalumno.nombre}}</td>
            <td>{{unalumno.correo}}</td>
            <td>@mdo</td>
          </tr>
          
          {% endfor %}
  
        </tbody>
      </table>
```
font awesome https://fontawesome.com/ y dentro d td  agregamos href + icono
```html
       <table class="table mt-3 table-bordered" >
        <thead>
          <tr>
            <th scope="col">ID</th>
            <th scope="col">Nombre Alumno</th>
            <th scope="col">Correo Alumno</th>
            <th scope="col">Accion</th>
          </tr>
        </thead>
        <tbody>
          {% for unalumno in  losalumnos %}
          <tr>
            <th>{{unalumno.id}}</th>
            <td>{{unalumno.nombre}}</td>
            <td>{{unalumno.correo}}</td>
            <td>
              <a href="" class="btn btn-success"><i class="fa-solid fa-pen-to-square"></i> </a>
            </td>
          </tr>
          
          {% endfor %}
  
        </tbody>
      </table>
```
Ahora agregamos boton borrar con otro href
```html
       <!-- Modal  tabla-->
       <table class="table mt-3 table-bordered" >
        <thead>
          <tr>
            <th scope="col">ID</th>
            <th scope="col">Nombre Alumno</th>
            <th scope="col">Correo Alumno</th>
            <th scope="col">Accion</th>
          </tr>
        </thead>
        <tbody>
          {% for unalumno in  losalumnos %}
          <tr>
            <th>{{unalumno.id}}</th>
            <td>{{unalumno.nombre}}</td>
            <td>{{unalumno.correo}}</td>
            <td>
              <a href="" class="btn btn-success btn-sm"><i class="fa-solid fa-pen-to-square"></i> </a>
              <a href="" class="btn btn-danger btn-sm"><i class="fa-solid fa-trash"></i></a>
            </td>
          </tr>
          
          {% endfor %}
  
        </tbody>
      </table>
```


## copiamos modal fade id agregarAlumnoModal y lo pegamos antes del final del ciclo for
- y modificamos agregar por actualizar 
- mas le agregamos _{{id}} de Alumno_T
```html
        <div class="modal fade" id="actualizarAlumnoModal_{{id}}" tabindex="-1" aria-labelledby="actualizarAlumnoModalLabel_{{id}}" aria-hidden="true">
          <div class="modal-dialog">
           <form action="" method="post">
            {% csrf_token %}
            <div class="modal-content">
              <div class="modal-header">
                <h5 class="modal-title fs-5" id="actualizarAlumnoModalLabel_{{id}}">actualizar Nuevo Alumno</h5>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
              </div>
              <div class="modal-body">
                <div class="">
                  <label for="name">Nombre del Alumno</label>
                  <input type="text" name="name" class="form-control" id="name" required>
                </div>
                <br>
                <div class="">
                  <label for="email">Correo del Alumno</label>
                  <input type="email" name="email" class="form-control" id="email" required>
                </div>
        
              </div>
              <div class="modal-footer">
                <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Cerrar</button>
                <button type="submit" class="btn btn-primary" name= "actualizar">actualizar nuevo Alumno</button>
              </div>
            </div>
           </form>
          </div>
        </div>
```

## copiamos data-bs-toggle="modal" data-bs-target="#agregarAlumnoModal"
- y lo pegamos en 
xxxx
```html
          {% for unalumno in  losalumnos %}
          <tr>
            <th>{{unalumno.id}}</th>
            <td>{{unalumno.nombre}}</td>
            <td>{{unalumno.correo}}</td>
            <td>
              <a href="" data-bs-toggle="modal" data-bs-target="#agregarAlumnoModal" class="btn btn-success btn-sm"><i class="fa-solid fa-pen-to-square"></i> </a>
              <a href="" class="btn btn-danger btn-sm"><i class="fa-solid fa-trash"></i></a>
            </td>
          </tr>
        <!--  actualizamos Alumno Modal -->
```

## Ahora copiamos actualizarAlumnoModal_{{id}} y lo pegamos en el boton agregar actualizar
- verificamos en el navegador y observe como quedo
```html
          {% for unalumno in  losalumnos %}
          <tr>
            <th>{{unalumno.id}}</th>
            <td>{{unalumno.nombre}}</td>
            <td>{{unalumno.correo}}</td>
            <td>
              <a href="" data-bs-toggle="modal" data-bs-target="#actualizarAlumnoModal_{{id}}" class="btn btn-success btn-sm"><i class="fa-solid fa-pen-to-square"></i> </a>
              <a href="" class="btn btn-danger btn-sm"><i class="fa-solid fa-trash"></i></a>
            </td>
          </tr>
        <!--  actualizamos Alumno Modal -->
```

## ahora en cada  input  agregamos value  a {{}} y observamos el server
```html
      <div class="">
                  <label for="name">Nombre del Alumno</label>
                  <input type="text" name="name" class="form-control"  value= "{{unalumno.nombre}}" id="name" required>
                </div>
                <br>
                <div class="">
                  <label for="email">Correo del Alumno</label>
                  <input type="email" name="email" class="form-control" value= "{{unalumno.correo}}"id="email" required>
                </div>
```

## ahora modificamos el id de actualizar
```html
          {% for unalumno in  losalumnos %}
          <tr>
            <th>{{unalumno.id}}</th>
            <td>{{unalumno.nombre}}</td>
            <td>{{unalumno.correo}}</td>
            <td>
              <a href="" data-bs-toggle="modal" data-bs-target="#actualizarAlumnoModal_{{unalumno.id}}" class="btn btn-success btn-sm"><i class="fa-solid fa-pen-to-square"></i> </a>
              <a href="" class="btn btn-danger btn-sm"><i class="fa-solid fa-trash"></i></a>
            </td>
          </tr>
        <!--  actualizamos Alumno Modal -->
        <div class="modal fade" id="actualizarAlumnoModal_{{unalumno.id}}" tabindex="-1" aria-labelledby="actualizarAlumnoModalLabel_{{unalumno.id}}" aria-hidden="true">
          <div class="modal-dialog">
           <form action="" method="post">
            {% csrf_token %}
```
en el boton summit o enviar name="update"
```html
<button type="submit" class="btn btn-primary" name= "update">actualizar nuevo Alumno</button>
```
minuto 32
```
```