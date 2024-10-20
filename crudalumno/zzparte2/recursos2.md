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
```
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
```
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
```
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


xxxx minuto 28:38
```

```



xxxx
```

```






