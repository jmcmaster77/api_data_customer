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
insumos_ventas.txt

```bash
4/7/2025|15332813|Jorge Martin|calle Real de Altavista casa #163 piso 2 ap 2 Catia Caracas Venezuela |0414-5506698|jmcmaster77@gmail.com|10.99|1|2
4/7/2025|11234567|Luke Skywalker|Calle Fuerza, 123, Sector Tatooine, Galaxia Lejana|0414-8735698|luke.skywalker@galaxyfaraway.com|25.50|3|4
4/7/2025|24356789|Leia Organa|Avenida Rebelión, 456, Distrito Alderaan, Galaxia Central|0424-4561984|leia.organa@rebellionforce.com|15.75|1|3
4/7/2025|15478902|Han Solo|Paseo Halcón, 789, Puerto Corellia, Sistema Estelar|0412-7895632|han.solo@millenniumfalcon.com|42.30|4|1
4/7/2025|28945678|Sarah Connor|Calle Skynet, 321, Zona Cyberdyne, Ciudad del Futuro|0414-6984523|sarah.connor@skynetwatcher.com|18.90|2|4
4/7/2025|17654321|Ellen Ripley|Sector Nostromo, 654, Estación LV-426, Espacio Exterior|0424-5217896|ellen.ripley@nostromo.com|33.45|3|2
4/7/2025|13467890|John Carter|Plaza Marte, 987, Ciudad Helium, Planeta Rojo|0412-3698541|john.carter@marsadventure.com|27.80|4|1
4/7/2025|19987654|James T. Kirk|Avenida Estelar, 159, Base Estrella, Flota Espacial|0424-4781236|james.kirk@enterprisefleet.com|60.25|1|3
4/7/2025|21345678|Spock Vulcan|Calle Lógica, 753, Sector Vulcano, Zona Galáctica|0414-7825693|spock.vulcan@logicalmind.com|12.15|2|4
4/7/2025|26789012|Jean-Luc Picard|Camino Federación, 246, Sede Enterprise, Cuadrante Alpha|0412-8967542|jean.picard@starfleetcommand.com|29.99|4|2
4/7/2025|24567890|Nyota Uhura|Calle Comunicación, 369, Distrito Galáctico, Sector Comms|0414-5632147|nyota.uhura@galacticcomms.com|49.50|3|1
4/7/2025|18903456|Dana Scully|Avenida Expediente X, 852, Zona FBI, Washington DC|0424-8541362|dana.scully@xfilesagent.com|35.20|1|3
4/7/2025|22345678|Fox Mulder|Calle Verdad, 147, Sector Paranormal, Ciudad Alienígena|0412-7215896|fox.mulder@truthseeker.com|22.40|2|4
4/7/2025|17567890|Rick Deckard|Camino Blade Runner, 951, Distrito Replicante, Los Ángeles Futurista|0414-6584712|rick.deckard@bladehunter.com|55.85|4|2
4/7/2025|25432198|Roy Batty|Calle Sueño, 753, Sector Nexus, Ciudad Android|0424-3879541|roy.batty@androiddreams.com|40.00|3|3
4/7/2025|29456781|Neo Anderson|Avenida Matrix, 369, Piso Red Pill, Ciudad Digital|0412-4978563|neo.anderson@matrixreboot.com|19.75|1|1
4/7/2025|15678903|Trinity Morpheus|Calle Libertad, 852, Sector Zion, Mundo Subterráneo|0414-6523987|trinity.morpheus@redpilljourney.com|70.90|2|4
4/7/2025|20765432|Paul Atreides|Camino Arena, 147, Distrito Arrakis, Dunas Eternas|0424-8154723|paul.atreides@arrakislegacy.com|30.10|4|2
4/7/2025|20765432|Gaius Baltar|Avenida Ciencia, 951, Sector Cylon, Galáctica 12|0412-6379512|gaius.baltar@cylonscience.com|45.25|3|3
4/7/2025|20765432|Shepard Book|Calle Serenity, 753, Distrito Firefly, Espacio Inexplorado|0414-8936451|shepard.book@serenitycrew.com|28.30|1|1
4/7/2025|19876543|Kara Thrace|Camino Estelar, 369, Sector Colonial, Flota Espacial|0424-5782163|kara.thrace@galacticpilots.com|50.60|2|4
```

Respuesta 

```json
[
    {
        "message": "archivo insumo_ventas.txt recibido"
    },
    {
        "archivo generado": "P:\\CODE\\py3\\api_data_customer\\src\\incoming\\insumo_ventas_20-04-2025_16_26_20.txt"
    }
]
```

> [!CAUTION]
> En Devs ☕

> [!NOTE]
> En consturccion ☕