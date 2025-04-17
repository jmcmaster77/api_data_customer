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
> [!IMPORTANT]
> Solo un usuario como rol de admin podra realizar gestion en los endpoint para crear usuario, usuarios, consultar, modificar y marcar como borrado

JWT para realizar gestion - tambien se puede generar un token nuevo en caso de requerirlo en el endpoint gen token con id, username y el password 

```bash
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE3NDQ3OTMxMDUsImV4cCI6MTc2MDM0NTEwNSwiaWQiOjEsInVzZXJuYW1lIjoiYXdhbGtlciIsImZ1bGxuYW1lIjoiQWxsYW4gV2Fsa2VyIiwicm9sIjoiYWRtaW4ifQ.raFWDYlhmmz5d_l_IrN4LNzJBa4IkxHtC5CIoFyuMvI

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

### Endpoint para consultar los usuarios registrados 
teniendo en cuenta que solo entrega un json con id, username, fullname, rol, y fecha con formado D M YY y HH MM, filtrando que el usuario no este marcado como borrado, donde deleted = false para control del borrado logico

```bash
curl --request GET \
  --url http://127.0.0.1:5000/users
```

### Respuesta 

```json
[
    {
        "id": 1,
        "username": "awalker",
        "fullname": "Allan Walker",
        "rol": "admin",
        "fecha": "23/03/25 21:59"
    },
    {
        "id": 2,
        "username": "naruto_uzumaki",
        "fullname": "Naruto Uzumaki",
        "rol": "operator",
        "fecha": "25/03/25 02:07"
    },
    {
        "id": 3,
        "username": "sakura_haruno",
        "fullname": "Sakura Haruno",
        "rol": "operator",
        "fecha": "25/03/25 02:30"
    },
    {
        "id": 4,
        "username": "eren_jaeger",
        "fullname": "Eren Jaeger",
        "rol": "operator",
        "fecha": "25/03/25 02:30"
    },
    {
        "id": 5,
        "username": "mikasa_ackerman",
        "fullname": "Mikasa Ackerman",
        "rol": "operator",
        "fecha": "25/03/25 02:30"
    },
    {
        "id": 6,
        "username": "goku_saiyan",
        "fullname": "Goku Saiyan",
        "rol": "operator",
        "fecha": "25/03/25 02:30"
    },
    {
        "id": 7,
        "username": "luffy_d_monkey",
        "fullname": "Monkey D. Luffy",
        "rol": "operator",
        "fecha": "25/03/25 02:30"
    },
    {
        "id": 8,
        "username": "light_yagami",
        "fullname": "Light Yagami",
        "rol": "operator",
        "fecha": "25/03/25 02:30"
    }
]
```

## Endpoint para consultar la data de un usuario con un json con el tipo de opcion y un parametro, donde la opcion puede ser por id ó username

```bash
curl --request POST \
http://localhost:5000/user_info
```

Json con parametros para busqueda por id 
```bash
{
    "type":"id",
    "param":"1"
}
```

respuesta 

```json
{
    "id": 1,
    "username": "awalker",
    "fullname": "Allan Walker",
    "rol": "admin",
    "registrado": "23/03/25 21:59",
    "deleted": false
}
```

Json con parametros para busqueda por username 
```bash
{
    "type":"username",
    "param":"light_yagami"
}
```
respuesta 

```json
{
    "id": 8,
    "username": "light_yagami",
    "fullname": "Light Yagami",
    "rol": "operator",
    "registrado": "25/03/25 02:30",
    "deleted": false
}
```

En caso de no existir la informacion del usuario 

```json
{
    "message": "la busqueda del usuario con el tipo de busqueda username y el parametro light_yagam no arrojo resultados"
}
```

## Endpoint para modificar la data de un usuario con un json suministrando el id del usuario a consultar y los parametros a cambiar

> [!NOTE]
> el username no puede estar siendo utilizado por otro id, ya que te retornara una respuesta con datos del usuario que esta utilizando ese username

```bash
curl --request POST \
http://localhost:5000/update_data_user
```

Json con el id para su busqueda mas los parametros a cambiar, 
```bash
{
    "id": "9",
    "username": "test_user2",
    "fullname": "Robin Schulz",
    "rol": "operator"
}
```

Respuesta en caso de que el username este registrado para otro usuario

```bash
[
    {
        "mensaje": "el username light_yagami esta siendo utilizado por el id 8 ",
        "username": "light_yagami",
        "fullname": "Light Yagami"
    }
]
```

Respuesta cuando fue encontrada la data del usuario y los cambios realizados.

```json
[
    {
        "datos": "encontrados",
        "id": 9,
        "username": "test_user1",
        "fullname": "test User1",
        "rol": "operator"
    },
    {
        "datos": "actualizados",
        "id": 9,
        "username": "test_user2",
        "fullname": "Robin Schulz",
        "rol": "operator"
    }
]

```

Respuesta de no encontrar el id 

```json
{
    "message": "la busqueda del id 57 no arrojo resultados"
}
```

## Endpoint para marcar la data de un usuario como borrado con un json con el tipo de opcion y un parametro, donde la opcion puede debe ser por id
### Borrado Logico 

```bash
curl --request POST \
http://localhost:5000/mark_user_deleted
```

Json con el id y el parametro deleted.

```bash
{
    "id": "4",
    "deleted": true
}
```

Respuesta 

```json
[
    {
        "datos": "Usuario",
        "id": 4,
        "username": "eren_jaeger",
        "fullname": "Eren Jaeger",
        "rol": "operator",
        "deleted": false
    },
    {
        "operation": "successfully",
        "message": "usuario fue marcado como borrado"
    }
]
```

Respuesta en caso de no conseguir el id 

```json
{
    "message": "la busqueda del id 56 no arrojo resultados"
}
```
## Endpoint para generar el Token para un usuario registrado en la base de datos por medio de un json con id, username y el password ☕

> [!IMPORTANT]
> El token tiene un tiempo de vida de 180 dias, y esta configurado con el tz Venezuela/Caracas
> No se puede generar un token para un usuario marcado como borrado

```bash
curl --request POST \
http://localhost:5000/gen_token
```
Json con los parametros id [integer], username y password

```bash
{
    "id":1,
    "username":"awalker",
    "password":"123456"
}
```

Respuesta con el JWT

```json
{
    "success": true,
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE3NDQ3OTMxMDUsImV4cCI6MTc2MDM0NTEwNSwiaWQiOjEsInVzZXJuYW1lIjoiYXdhbGtlciIsImZ1bGxuYW1lIjoiQWxsYW4gV2Fsa2VyIiwicm9sIjoiYWRtaW4ifQ.raFWDYlhmmz5d_l_IrN4LNzJBa4IkxHtC5CIoFyuMvI"
}
```

Respuesta en caso de no conseguir el id o no hacer match username y password con los datos almacenados en la base de datos 

```json
{
    "success": false,
    "message": "token no generado"
}
```
## Endpoint para validar el Token ☕

```bash
curl --request POST \
http://localhost:5000/verify_token
```

para validar el token con postman en la pestaña Authorizarion indicar Auth Type API Key, Key Authorization pegar el token en el campo Value, Add to Header de esta manera sera incluido en el header.

o por medio de http://localhost:5000/docs en el boton Autozice colocar el token en el campo value para la APIKeyHeader de nombre Authorizarion

Respuesta para token valido 

Status Code 200 OK

```json
[
    {
        "message": "Token Valido"
    },
    {
        "iat": "16 de April de 2025, 06:32:53 UTC",
        "exp": "13 de October de 2025, 06:32:53 UTC",
        "id": 1,
        "username": "awalker",
        "fullname": "Allan Walker",
        "rol": "admin"
    }
]
```

Respuesta para token invalido 

Status Code 401 Unauthorized

```json
[
    {
        "message": "Token error: Signature verification failed"
    }
]
```

> [!NOTE]
> En desarrollo a partir de aqui ^^ ☕ no leer es informacion de otro proyecto -_-

> [!IMPORTANT]
> Para gestionar servicios es requerido el siguiente Token. de utilizar Postman ingresarlo en authenticación APIKeyHeader de nombre Authorizarion

## TOKEN Requerido para realizar gestiones

```bash
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE3NDQ3OTk1NzMsImV4cCI6MTc2MDM1MTU3MywiaWQiOjEsInVzZXJuYW1lIjoiYXdhbGtlciIsImZ1bGxuYW1lIjoiQWxsYW4gV2Fsa2VyIiwicm9sIjoiYWRtaW4ifQ.nkHg4MRm8fS5MQ1019SqksmdAiswY8bA7OawkLC_-sI
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











