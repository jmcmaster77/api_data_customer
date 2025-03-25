## API Rest Data From Customer

Endpoints del para gestion de usuarios

> [!TIP] 
> Para Realizar pruebas con la API con Postman 

### Endpoint Test Server 
```bash
curl --request GET \
  --url http://127.0.0.1:5000/
```

### Respuesta 
```json
{
    "status": "Server Up"
}
```

### Endpoint para agregar un usuario
```bash
curl --request POST \
  --url http://127.0.0.1:5000/create_user
```

```json
{
    "username":"awalker",
    "password":"123456",
    "fullname":"Allan Walker",
    "rol":"admin"
}
```

### Respuesta en caso de satisfactorio
imagen aqui ukenene

### Respuesta en caso de existir el usuario
```json
{
    "message": "usuario: awalker con el id:1 ya se encuentra registrado"
}
```

### Endpoint para agregar un lote de usuarios
```bash
curl --request POST \
  --url http://127.0.0.1:5000/create_users
```

```json
[
  {
    "username": "naruto_uzumaki",
    "password": "Rasengan123!",
    "fullname": "Naruto Uzumaki",
    "rol": "operator"
  },
  {
    "username": "sakura_haruno",
    "password": "CherryBlossom456!",
    "fullname": "Sakura Haruno",
    "rol": "operator"
  },
  {
    "username": "eren_jaeger",
    "password": "TitanSlayer789!",
    "fullname": "Eren Jaeger",
    "rol": "operator"
  },
  {
    "username": "mikasa_ackerman",
    "password": "BladeMaster001!",
    "fullname": "Mikasa Ackerman",
    "rol": "operator"
  },
  {
    "username": "goku_saiyan",
    "password": "KamehamehaX3!",
    "fullname": "Goku Saiyan",
    "rol": "operator"
  },
  {
    "username": "luffy_d_monkey",
    "password": "OnePieceKing007!",
    "fullname": "Monkey D. Luffy",
    "rol": "operator"
  },
  {
    "username": "light_yagami",
    "password": "KiraJustice999!",
    "fullname": "Light Yagami",
    "rol": "operator"
  }
]
```

### Respuesta en caso de existir el usuario 
```json
{
    "result": {
        "Resgistros": [
            {
                "1": "usuario: naruto_uzumaki con el id:2 ya se encuentra registrado"
            },
            {
                "2": "usuario registrado con el id: 3"
            },
            {
                "3": "usuario registrado con el id: 4"
            },
            {
                "4": "usuario registrado con el id: 5"
            },
            {
                "5": "usuario registrado con el id: 6"
            },
            {
                "6": "usuario registrado con el id: 7"
            },
            {
                "7": "usuario registrado con el id: 8"
            }
        ]
    }
}
```

> [!NOTE]
> En desarrollo a partir de aqui ^^ ☕ no leer es informacion de otro proyecto -_-

> [!IMPORTANT]
> Para gestionar servicios es requerido el siguiente Token Bearer. de utilizar Postman ingresarlo en authenticación Header 

## TOKEN Requerido para realizar gestiones

```bash
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE3MzgyODYxMTgsImV4cCI6MTc1MzgzODExOCwiaWQiOjEsInVzZXJuYW1lciI6ImptYXJ0aW4iLCJmdWxsbmFtZSI6IkpvcmdlIE1hcnRpbiIsInJvbGVzIjpbImFkbWluIiwiZWRpdCJdfQ.UjMFfVUpQeXMx9xKAqcsK8Yfu_G7C1mBPQSTvZ4HVw0
```
Registrando el token en la interface web


> [!NOTE]
> Usuario de prueba para generar un nuevo token. es Ray y la clave seria ray12345. de realizar la peticion por postman se podrian realizar con el siguiente json.

```json
{
	"id": 0,
    "username": "Ray",
    "password": "ray12345"
}
```

## Consulta de Personas

```bash
curl --request GET \
  --url http://localhost:5000/personas
```

respuesta 

```json
[
  {
    "_id": "66229e47bc3c56e3ecc20f60",
    "idp": 1,
    "fullname": "Jorge Martin",
    "email": "jm@exam.com",
    "registrado": "2024-04-19T12:33:03.969000"
  },
  {
    "_id": "6622ac13ccae731d7fd6a290",
    "idp": 2,
    "fullname": "Eloy Martin",
    "email": "em@edit.com",
    "registrado": "2024-04-22T01:55:38.923000"
  },
  {
    "_id": "6622acc442e08ffe18f94c4c",
    "idp": 3,
    "fullname": "Jorge Martin",
    "email": "jm@exs.com",
    "registrado": "2024-04-19T12:33:03.969000"
  },
]
```
## Registro de Persona

```bash
curl --request POST \
http://localhost:5000/personas
```

respuesta 

```json
{
  "mensajes":"Persona Registrada"
}
```

> [!NOTE]
> la base de datos requiere un usuario jm y el pass es 15332, con el cual de requerir hacer una conexion con una instancia distinta de mongodb las variables de entorno seria

```bash
MONGO_URI = 'mongodb://localhost:27017/'
```
o modificar las variables de entorno el el archo .env

> [!CAUTION]
> En Devs ☕











