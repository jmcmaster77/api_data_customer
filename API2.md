## API Rest Data From Customer

Endpoints del para la operaciones de extracion de data

> [!IMPORTANT]
> dependiendo del rol del usuario podra: 
> rol admin acceso a todos los endpoint como el logger y los data historica del cliente.
> rol operator solo acceso a los endpoint para extraer data del cliente para sus procesos.

JWT de un admin

```bash
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE3NDQ3OTMxMDUsImV4cCI6MTc2MDM0NTEwNSwiaWQiOjEsInVzZXJuYW1lIjoiYXdhbGtlciIsImZ1bGxuYW1lIjoiQWxsYW4gV2Fsa2VyIiwicm9sIjoiYWRtaW4ifQ.raFWDYlhmmz5d_l_IrN4LNzJBa4IkxHtC5CIoFyuMvI
```

JWT de un operator

```bash
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE3NDQ4NzI4OTEsImV4cCI6MTc2MDQyNDg5MSwiaWQiOjUsInVzZXJuYW1lIjoibWlrYXNhX2Fja2VybWFuIiwiZnVsbG5hbWUiOiJNaWthc2EgQWNrZXJtYW4iLCJyb2wiOiJvcGVyYXRvciJ9.MlxAMpEigJZ8D5BqDoNg4oTZUrbaiIw86Gqk_gwFpN4
```

## Consulta del log 

> [!IMPORTANT]
> Solo puede ser solicitada por un usuario que tenga rol de admin

```bash
curl --request POST \
  --url http://127.0.0.1:5000/log
```

Respuesta con la data del log 

```bash
2025-04-19 23:18:01,792 - INFO - API running on port: 5000
2025-04-19 23:18:02,917 - ERROR - usuario: naruto_uzumaki con el id:2 ya se encuentra registrado
2025-04-19 23:18:02,919 - ERROR - usuario: sakura_haruno con el id:3 ya se encuentra registrado
2025-04-19 23:18:02,921 - ERROR - usuario: eren_jaeger con el id:4 ya se encuentra registrado
2025-04-19 23:18:02,923 - ERROR - usuario: mikasa_ackerman con el id:5 ya se encuentra registrado
2025-04-19 23:18:02,925 - ERROR - usuario: goku_saiyan con el id:6 ya se encuentra registrado
2025-04-19 23:18:02,928 - ERROR - usuario: luffy_d_monkey con el id:7 ya se encuentra registrado
2025-04-19 23:18:02,931 - ERROR - usuario: light_yagami con el id:8 ya se encuentra registrado
2025-04-19 23:29:41,074 - INFO - API running on port: 5000
2025-04-19 23:29:46,435 - WARNING - Se valida un token para el usuario id 7 luffy_d_monkey usuario con condicion borrado
2025-04-19 23:29:55,220 - WARNING - Se valida un token para el usuario id 2 naruto_uzumaki usuario con condicion borrado
2025-04-19 23:30:29,383 - INFO - Se valida un token para el usuario id 8 light_yagami satisfactoriamente
2025-04-20 00:10:17,894 - INFO - API running on port: 5000
2025-04-20 00:11:55,336 - WARNING - Se intento solicitar el log por 8 - light_yagami sin autorizacion
2025-04-20 00:12:15,895 - INFO - Solicitud del log por 1 - awalker
```

En caso de ser solicitada por un usuario con rol de operador 

```json
{
    "message": "Usuario no tiene autorizacion"
}
```

> [!CAUTION]
> En Devs ☕

> [!NOTE]
> En consturccion ☕