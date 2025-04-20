# Project name
## API Rest Data From Customer

## Version 

Versión en desarrollo v.0.5

## Description

Api escrita en python, fastAPI con conexion a una base de datos alojada en mariadb manejada con un ORM SQLAlchemy donde se obtiene datos del cliente por medio de distintas consultas y autenticacion con JWT 

> [!NOTE]
> Esta api está configurada con el puerto 5000 para la api y el puerto 3306 para el servidor de mariadb.

> [!IMPORTANT]
> Si tienes un servidor de mariadb activo si el puerto no es el puerto por defecto validar y modificar en las variables de entorno.


### Los enpoints se encuentran publicados en el siguiente link 

http://localhost:5000/docs

> [!TIP] 
> verificar que el servidor está en ejecución

## Requerimientos e instalación 

Se recomienda un entorno virtual. 

## configurando el entorno virtual 

```bash
python -m virtualenv venv
```

## activando el entorno virtual en windows (cmd)

```bash
.\venv\Scripts\activate.bat
```

## activando el entorno virtual en windows (powershell)

```bash
.\venv\Scripts\Activate.ps1
```

## activando el entorno virtual en linux

```bash
source ./venv/bin/activate
```

## instalado las dependencias

```bash
pip install -r requirements.txt
```

### Documentación adicional 

> [!NOTE]
> En consturccion ☕

En el siguiente apartado, se puede ver la documentación mas detallasa de la api.

[Documentación detallada para generar token, verificar token, crear, usuario, usuarios por lote, consultar lote de usuarios, informacion detalla del usuario, modificar, marcar como borrado, y recuperar usuario borrado](API.md)

[Documentación detallada para operaciones de data del cliente](API2.md)
