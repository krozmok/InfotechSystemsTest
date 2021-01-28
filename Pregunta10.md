# Defina indice en base datos, como hacer un flujo de respaldo, como operar con null

## Indice
* Es una estructura de datos enfocada en mejorar la velocidad de acceso a registros de una tabla, por medio de un identificador único por fila de una tabla en una base de datos y la manera más simple de definir un Index en SQL Server es:

```sql
    CREATE INDEX index_name
    ON table_name (column1, column2, ...);
```

## Como hacer un flujo de respaldo
* La manera más simple para crear un backup de la base de datos es con un script:
```sql
    BACKUP DATABASE databasename
    TO DISK = 'filepath';
```
* Sin embargo dependiendo de la herramienta a usar existen opciones para poder automatizar este proceso. Esta por ejemplo en SQL Server la creación de Trabajos (Jobs), o en otros casos hasta se podría utilizar la linea de comandos de windows con MySQL para crear un BAT que permita el uso de MySQLDump para realizar copias de seguridad.

## Como operar con NULL

* Pues según la documentación de T-SQL existen varias formas de manipular NULL para realizar operaciones con estas, siendo la más usada :
```sql 
    ISNULL()
```
* Esta sentencia varia dependiendo la herramienta a usar, si usamos Transact SQL (Version de SQL modificada con mejoras por microsoft) esta usa 2 parametros, en cambio si usamos MySQL en su compilador esta sentencisa usa 1 parametro. En base a esto podemos manejar valores nulos para poder operar con ellos.