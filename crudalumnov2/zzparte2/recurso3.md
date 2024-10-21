## agregamos input type antes del nombre y correo del alumnno

'''html
    <div class="modal-body">
    <input type="hidden" name="id" value="{{unalumno.id}}">
    <div class="">
        <label for="name">Nombre del Alumno</label>
        <input type="text" name="name" class="form-control"  value= "{{unalumno.nombre}}" id="name" required>
    </div>
    <br>
    <div class="">
        <label for="email">Correo del Alumno</label>
        <input type="email" name="email" class="form-control" value= "{{unalumno.correo}}"id="email" required>
    </div>
'''

## Ahora copiamos el area de modal y lo pegamos antes del fin del for
y borramos el div de agregar alumno + los input

```html
<!-- borrar alumno Modal -->
<div class="modal fade" id="agregarAlumnoModal" tabindex="-1" aria-labelledby="agregarAlumnoModalLabel" aria-hidden="true">
   <div class="modal-dialog">
    <form action="" method="post">
      {% csrf_token %}
      <div class="modal-content">

        <div class="modal-body">

          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Cerrar</button>
            <button type="submit" class="btn btn-primary" name= "actualizar">actualizar nuevo Alumno</button>
          </div>
        </div>
      </div>
    </form>
  </div>
</div> 

```
en borrar alumno modal agregamos unalumno.id
```html
<!-- borrar alumno Modal -->
<div class="modal fade" id="borrarAlumnoModal_{{unalumno.id}}" tabindex="-1" aria-labelledby="agregarAlumnoModalLabel_{{unalumno.id}}" aria-hidden="true">
   <div class="modal-dialog">
      <form action="" method="post">
        {% csrf_token %}
        <div class="modal-content">

          <div class="modal-body">

            <div class="modal-footer">
              <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Cerrar</button>
              <button type="submit" class="btn btn-primary" name= "actualizar">actualizar nuevo Alumno</button>
            </div>
          </div>
        </div>
      </form>
   </div>
</div> 
```
ahora copiamos data-bs-toggle="modal" data-bs-target="#actualizarAlumnoModal_{{unalumno.id}}"
y lo pegamos en la siguiente a href cambiamos actualizar por borrar
y probamos el server
```html
          {% for unalumno in  losalumnos %}
          <tr>
            <th>{{unalumno.id}}</th>
            <td>{{unalumno.nombre}}</td>
            <td>{{unalumno.correo}}</td>
            <td>
              <a href="" data-bs-toggle="modal" data-bs-target="#actualizarAlumnoModal_{{unalumno.id}}" class="btn btn-success btn-sm"><i class="fa-solid fa-pen-to-square"></i> </a>
              <a href="" data-bs-toggle="modal" data-bs-target="#borrarAlumnoModal_{{unalumno.id}}" class="btn btn-danger btn-sm"><i class="fa-solid fa-trash"></i></a>
            </td>
          </tr>
```
agregamos estas seguro con un parrafo y agregamos un input
y cambiamos primary por danger
```html
<!-- borrar alumno Modal -->
<div class="modal fade" id="borrarAlumnoModal_{{unalumno.id}}" tabindex="-1" aria-labelledby="agregarAlumnoModalLabel_{{unalumno.id}}" aria-hidden="true">
   <div class="modal-dialog">
      <form action="" method="post">
        {% csrf_token %}
        <input type="hidden" name="id" value="{{unalumno.id}}">
        <div class="modal-content">
          <div class="modal-body">
            <p>Estas seguro? deseas borrarlo </p>
            <div class="modal-footer">
              <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Cerrar</button>
              <button type="submit" class="btn btn-danger" name= "delete">Borrar Alumno</button>
            </div>
          </div>
        </div>
      </form>
   </div>
</div>
```

```
```