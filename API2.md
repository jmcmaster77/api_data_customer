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
4/7/2025|15332813|Jorge Martin|calle Real de Altavista casa #163 piso 2 ap 2 Catia Caracas Venezuela |0414-5506698|jmcmaster77@gmail.com|27,23|2|4|547
4/7/2025|11234567|Luke Skywalker|Calle Fuerza, 123, Sector Tatooine, Galaxia Lejana|0414-8735698|luke.skywalker@galaxyfaraway.com|22,53|3|4|547
4/7/2025|24356789|Leia Organa|Avenida Rebelión, 456, Distrito Alderaan, Galaxia Central|0424-4561984|leia.organa@rebellionforce.com|19,03|1|4|547
4/7/2025|15478902|Han Solo|Paseo Halcón, 789, Puerto Corellia, Sistema Estelar|0412-7895632|han.solo@millenniumfalcon.com|57,53|4|3|547
4/7/2025|28945678|Sarah Connor|Calle Skynet, 321, Zona Cyberdyne, Ciudad del Futuro|0414-6984523|sarah.connor@skynetwatcher.com|56,49|2|4|547
4/7/2025|17654321|Ellen Ripley|Sector Nostromo, 654, Estación LV-426, Espacio Exterior|0424-5217896|ellen.ripley@nostromo.com|66,86|3|2|547
4/7/2025|13467890|John Carter|Plaza Marte, 987, Ciudad Helium, Planeta Rojo|0412-3698541|john.carter@marsadventure.com|21,72|1|4|547
4/7/2025|19987654|James T. Kirk|Avenida Estelar, 159, Base Estrella, Flota Espacial|0424-4781236|james.kirk@enterprisefleet.com|76,39|4|1|547
4/7/2025|21345678|Spock Vulcan|Calle Lógica, 753, Sector Vulcano, Zona Galáctica|0414-7825693|spock.vulcan@logicalmind.com|20,83|2|3|547
4/7/2025|26789012|Jean-Luc Picard|Camino Federación, 246, Sede Enterprise, Cuadrante Alpha|0412-8967542|jean.picard@starfleetcommand.com|59,84|4|4|547
4/7/2025|24567890|Nyota Uhura|Calle Comunicación, 369, Distrito Galáctico, Sector Comms|0414-5632147|nyota.uhura@galacticcomms.com|41,74|4|4|547
4/7/2025|18903456|Dana Scully|Avenida Expediente X, 852, Zona FBI, Washington DC|0424-8541362|dana.scully@xfilesagent.com|53,6|4|1|547
4/7/2025|22345678|Fox Mulder|Calle Verdad, 147, Sector Paranormal, Ciudad Alienígena|0412-7215896|fox.mulder@truthseeker.com|12,11|4|1|547
4/7/2025|17567890|Rick Deckard|Camino Blade Runner, 951, Distrito Replicante, Los Ángeles Futurista|0414-6584712|rick.deckard@bladehunter.com|87,17|1|3|547
4/7/2025|25432198|Roy Batty|Calle Sueño, 753, Sector Nexus, Ciudad Android|0424-3879541|roy.batty@androiddreams.com|35,14|3|4|547
4/7/2025|29456781|Neo Anderson|Avenida Matrix, 369, Piso Red Pill, Ciudad Digital|0412-4978563|neo.anderson@matrixreboot.com|71,4|1|1|547
4/7/2025|15678903|Trinity Morpheus|Calle Libertad, 852, Sector Zion, Mundo Subterráneo|0414-6523987|trinity.morpheus@redpilljourney.com|81,82|3|2|547
4/7/2025|20765432|Paul Atreides|Camino Arena, 147, Distrito Arrakis, Dunas Eternas|0424-8154723|paul.atreides@arrakislegacy.com|16,01|1|1|547
4/7/2025|20765432|Gaius Baltar|Avenida Ciencia, 951, Sector Cylon, Galáctica 12|0412-6379512|gaius.baltar@cylonscience.com|31,18|4|1|547
4/7/2025|20765432|Shepard Book|Calle Serenity, 753, Distrito Firefly, Espacio Inexplorado|0414-8936451|shepard.book@serenitycrew.com|83,56|3|1|547
4/7/2025|19876543|Kara Thrace|Camino Estelar, 369, Sector Colonial, Flota Espacial|0424-5782163|kara.thrace@galacticpilots.com|20,45|1|4|547
```

Respuesta cuando el archivo fue recibido y cargado a la base de datos

```json
[
    {
        "message": "archivo insumo_ventas_547.txt recibido"
    },
    {
        "archivo generado": "P:\\CODE\\py3\\api_data_customer\\src\\incoming\\insumo_ventas_547_20-04-2025_21_15_58.txt"
    },
    {
        "Cantidad registros": "21"
    }
]
```

Respuesta si un lote de un registro es distinto en el archivo indicando la inconsistencia 

```json
{
    "message": "Se intento cargar un archivo insumo_ventas_547.txt con lotes diferentes en los registros {'547', '546'}"
}
```

Respuesta si un lote ya se encuentra registrado en la BD

```json
{
    "message": "Se intento cargar un archivo insumo_ventas_547.txt pero el 547 ya existe en la BD"
}
```

> [!CAUTION]
> En Devs ☕

> [!NOTE]
> En consturccion ☕