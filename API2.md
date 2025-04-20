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

## Endpoint para consulta del log 

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
## Endpoint para enviar archivo de carga de datos a la bd

```bash
curl --request POST \
  --url http://127.0.0.1:5000/incoming
```

> [!NOTE]
> Este archivo debe llevar el siguiente formato
filename.txt

```bash
1|2922.14|50403|01140230512300079116|3|454|0|04/04/2025|04/03/2025|0
1|2255.58|50403|01140525815250150212|3|454|0|04/04/2025|04/03/2025|0
1|2579.25|50403|01140525825250150158|3|454|0|04/04/2025|04/03/2025|0
1|1651.59|50403|01140525815250150220|3|454|0|04/04/2025|04/03/2025|0
1|402.62|50403|01140525815250150131|3|454|0|04/04/2025|04/03/2025|0
1|132.93|50403|01140525845250150174|3|454|0|04/04/2025|04/03/2025|0
1|906.96|50403|01140525855250150182|3|454|0|04/04/2025|04/03/2025|0
```

Respuesta 

```json
[
    {
        "message": "archivo insumo_ccerac_old.txt recibido generado"
    },
    {
        "archivo generado": "P:\\CODE\\py3\\api_data_customer\\src\\incoming\\insumo_ccerac_old_20-04-2025_14_11_09.txt"
    }
]
```

> [!CAUTION]
> En Devs ☕

> [!NOTE]
> En consturccion ☕