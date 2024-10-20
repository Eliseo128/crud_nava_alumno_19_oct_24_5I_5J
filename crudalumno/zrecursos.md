https://github.com/Aashishkumar123/django-cruds-project
- bootstrap 5
- link https://getbootstrap.com/docs/5.2/getting-started/introduction/

link  https://fonts.google.com/selection?preview.text=hola

link https://cdnjs.com/libraries/font-awesome

- video  https://youtu.be/UsYx0226LwA?si=4MqfSDHpHxJOKFUP
- en body 

```html
      <div class="container mt-5 p-5 rounded shadow bg-white">


      </div>
```
- el boton

```html
<div class="container mt-5 p-5 rounded shadow bg-white">
      <div class="">
      <a href="" class="btn btn-primary px-5 btn-sm">Agregar nuevo Alumno</a>
      </div>

</div>
```
- agregamos div class, form,  input, boton

 ```html
      <div class="">
      <form action="" method="post">
            <input type="search" name="search" class="form-control" placeholder="buscando ...">
            <button class ="btn btn-success ">Buscar</button>
      </form>
      </div>
```

- layout
 ```html
<div class="container mt-5 p-5 rounded shadow bg-white">

      <div class="d-flex justify-content-between align-items-center">
      <a href="" class="btn btn-primary px-5 btn-sm">Agregar nuevo Alumno</a>
      

      <div class="d-flex">
            <form action="" method="post">
            <input type="search" name="search" class="form-control" placeholder="buscando ...">
            <button class ="btn btn-success ">Buscar</button>
            </form>

      </div>

      </div>
</div>
```
- reacomodando
```html
<div >
      <form action="" method="post" class="d-flex">
      <input type="search" name="search" class="form-control" placeholder="buscando ...">
      <button class ="btn btn-success mx-3">Buscar</button>
      </form>

</div>
```



```html
      <div class="d-flex justify-content-between align-items-center">
      <a href="" class="btn btn-primary px-4 py-2 btn-sm">Agregar nuevo Alumno</a>


      <div >
            <form action="" method="post" class="d-flex">
            <input type="search" name="search" class="form-control" placeholder="buscando ...">
            <button class ="btn btn-success mx-2">Buscar</button>
            </form>

      </div>

      </div>
```

- modal

- https://getbootstrap.com/docs/5.0/components/modal/

Lounch demo modal
```html
<!-- Modal -->
<div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
  <div class="modal-dialog">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title" id="exampleModalLabel">Modal title</h5>
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
      </div>
      <div class="modal-body">
        ...
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
        <button type="button" class="btn btn-primary">Save changes</button>
      </div>
    </div>
  </div>
</div>
```


- sleccionar palabra y pressiona ctrl + F2
- de bootstrap modal copiamos  data-bs-toggle="modal" data-bs-target="#exampleModal"
y lo pegamos en a href

```html
 <a href="" data-bs-toggle="modal" data-bs-target="#exampleModal" class="btn btn-primary px-4 py-2 btn-sm">Agregar nuevo Alumno</a>
```
- modificamos por agregar Alumno modal
- 
```html
  <a href="" data-bs-toggle="modal" data-bs-target="#agregarAlumnoModal" class="btn btn-primary px-4 py-2 btn-sm">Agregar nuevo Alumno</a>
```
remplazamos los puntitos 
```
       <div class="modal-body">
        ...
      </div>
```
asi queda en modal
```html
<!-- Modal -->
<div class="modal fade" id="agregarAlumnoModal" tabindex="-1" aria-labelledby="agregarAlumnoModalLabel" aria-hidden="true">
  <div class="modal-dialog">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title" id="agregarAlumnoModalLabel">Agregar Nuevo Alumno</h5>
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
      </div>
      <div class="modal-body">
        <div class="">
          <label for="name">Nombre del Alumno</label>
          <input type="text" name="name" class="form-control" id="name">
        </div>

      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
        <button type="button" class="btn btn-primary">Save changes</button>
      </div>
    </div>
  </div>
</div>
```
- agregamos br y copiamos div alumno por su correo
```html
<!-- Modal -->
<div class="modal fade" id="agregarAlumnoModal" tabindex="-1" aria-labelledby="agregarAlumnoModalLabel" aria-hidden="true">
  <div class="modal-dialog">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title" id="agregarAlumnoModalLabel">Agregar Nuevo Alumno</h5>
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
      </div>
      <div class="modal-body">
        <div class="">
          <label for="name">Nombre del Alumno</label>
          <input type="text" name="name" class="form-control" id="name">
        </div>
        <br>
        <div class="">
          <label for="email">Correo del Alumno</label>
          <input type="email" name="email" class="form-control" id="email">
        </div>

      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
        <button type="button" class="btn btn-primary">Agregar nuevo Alumno</button>
      </div>
    </div>
  </div>
</div>
```
cerrar codigo cortar y copiar   ctrl X ,desde class modal-content -->
y agregar form mas {% csrf_token %}
se ve de la siguiente manera
```html
<!-- Modal -->
<div class="modal fade" id="agregarAlumnoModal" tabindex="-1" aria-labelledby="agregarAlumnoModalLabel" aria-hidden="true">
  <div class="modal-dialog">
   <form action="" method="post">
    {% csrf_token %}
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title" id="agregarAlumnoModalLabel">Agregar Nuevo Alumno</h5>
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
      </div>
      <div class="modal-body">
        <div class="">
          <label for="name">Nombre del Alumno</label>
          <input type="text" name="name" class="form-control" id="name">
        </div>
        <br>
        <div class="">
          <label for="email">Correo del Alumno</label>
          <input type="email" name="email" class="form-control" id="email">
        </div>

      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
        <button type="button" class="btn btn-primary">Agregar nuevo Alumno</button>
      </div>
    </div>
   </form>
  </div>
</div>
```
agregamos los campos requeridos  required  input 
- + en el segundo boton agregar alumno colocar submit + name="agregar"


```html
<!-- Modal -->
<div class="modal fade" id="agregarAlumnoModal" tabindex="-1" aria-labelledby="agregarAlumnoModalLabel" aria-hidden="true">
  <div class="modal-dialog">
   <form action="" method="post">
    {% csrf_token %}
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title" id="agregarAlumnoModalLabel">Agregar Nuevo Alumno</h5>
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
        <button type="submit" class="btn btn-primary" name= "Agregar">Agregar nuevo Alumno</button>
      </div>
    </div>
   </form>
  </div>
</div>
```
Agregar tabla desde modal bootstrap
```html
       <table class="table mt-3 table-bordered" >
        <thead>
          <tr>
            <th scope="col">#</th>
            <th scope="col">First</th>
            <th scope="col">Last</th>
            <th scope="col">Handle</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <th scope="row">1</th>
            <td>Mark</td>
            <td>Otto</td>
            <td>@mdo</td>
          </tr>
          <tr>
            <th scope="row">2</th>
            <td>Jacob</td>
            <td>Thornton</td>
            <td>@fat</td>
          </tr>
          <tr>
            <th scope="row">3</th>
            <td colspan="2">Larry the Bird</td>
            <td>@twitter</td>
          </tr>
        </tbody>
      </table>
```
