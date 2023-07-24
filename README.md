# Imagine_Apps_Tarea1_API
API:
	
 * La api trabaja con una base de datos alojada en Supabase, que trabaja con el motor de bases de datos **PostgreSql**.

* No está desplegada en Azure Kubernetes por restricciones de cuenta gratuita. La aplicación está desplegada en Azure Container Instance

* # Link despliegue en Azure: http://api-docker-yohan.brazilsouth.azurecontainer.io:8000/docs

* Si no funciona el link, al clonar el repositorio se interactúa con la Api por medio del enlace http://localhost:8000/docs

* La base de datos está alimentada con los datos que obtuve de la **tarea 3: Análisis de datos**. Son los datos después de la 
	  limpieza y transformación que realicé para cumplir dicha tarea. El archivo original de la tarea 3 tiene más de 1'000,000 de
	  registros y la base de datos en Supabase la formé con 100 registros tomados aleatoriamente de más del millón de registros 
	  originales.

 * La API usa **autenticación por token** por medio de la librería de supabase.

 * El CRUD funciona a excepcion del método PUT que no logré configurarlo óptimamente.

 * Existen **pruebas unitarias** para los métodos Get, Post y Delete
