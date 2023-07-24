# Imagine_Apps_Tarea1_API
API:
	
 * La api trabaja con una base de datos alojada en Supabase, que trabaja con el motor de bases de datos PostgreSql.

* No esta desplegada en Azure Kubernetes por restricciones de cuenta gratuita. La aplicación esta desplegada en Azure Container Instance

* # Si no funciona el link, al clonar el repositorio se interactua con la Api por medio del enlace http://localhost:8000/docs

* Link despliegue en Azure: https://imagine-apps-yohan-rodriguez.brazilsouth.azurecontainer.io

 * La base de datos esta alimentada con los datos que obtuve de la tarea 3: Análisis de datos. Son los datos después de la 
	  limpieza y transformación que realicé para cumplir la Tarea 3. El archivo original de la tarea 3 tiene más de 1'000,000 de
	  registros y la base de datos en Supabase la formé con 100 registros tomados aleatoriamente de más millon de registros 
	  originales.

 * La API usa autenticación por token por medio de la libreria de supabase.

 * El CRUD funciona a excepcion del método PUT que no logré copnfigurarlo optimamente.

 * Exsiten pruebas unitarias para los métodos Get, Post y Delete
