# AppsMovilesAPI

## Requerimientos:
1. Python 3
2. virtualenv (el repositorio incluye las librerías necesarias)

## Cómo correr la API
### Linux:
1. Abrir una terminal en la carpeta del repositorio
2. Activar virtualenv: *source pythonAPI/bin/activate*
3. Ejecutar la aplicación de python: *python3 usersAPI.py*

### Windows:
Pendiente

## Como usar la API
Esta estructura varía un poco con respecto a la que nos piden en el curso, pero los datos esenciales son los mismos.
### signup POST
- url: https://localhost:5000/users
- header:
  - key: Content-Type
  - value: application/vnd.api+json
- body:
  {
    "data": {
        "type": "user",
        "attributes": {
            "userName": "Nombre_de_usuario",
            "name": "Nombre Apellido,
            "password": "myPassword"}}}
            
### login POST
Pendiente
