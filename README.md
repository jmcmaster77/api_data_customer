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

### Requerimientos e instalación 

Se recomienda un entorno virtual. 

### Configurando el entorno virtual 

```bash
python -m virtualenv venv
```

### Activando el entorno virtual en windows (cmd)

```bash
.\venv\Scripts\activate.bat
```

### Activando el entorno virtual en windows (powershell)

```bash
.\venv\Scripts\Activate.ps1
```

### Activando el entorno virtual en linux

```bash
source ./venv/bin/activate
```

### Instalado las dependencias

```bash
pip install -r requirements.txt
```

### Base de dato 

api_data_customers

entre los archivos hay un respaldo de la bd api_data_customers_20425.db

para restaurar por powershell 

```bash
Get-Content api_data_customers_20425.db | mariadb -u root -p api_data_customers
```

### Realizar respaldo a la base de datos 

```bash
mariadb-dump -u root -p api_data_customers > api_data_customers_20425.db
```

### Documentación adicional 

> [!NOTE]
> En consturccion ☕

En el siguiente apartado, se puede ver la documentación mas detallasa de la api.

[Documentación detallada para generar token, verificar token, crear, usuario, usuarios por lote, consultar lote de usuarios, informacion detalla del usuario, modificar, marcar como borrado, y recuperar usuario borrado](API.md)

[Documentación detallada para operaciones de data del cliente](API2.md)
