# Especificar la imagen base de Python
FROM python:3.11

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar el archivo requirements.txt al contenedor
COPY requirements.txt /app/

# Instalar las dependencias desde requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto del código fuente al contenedor
COPY . /app/

# Exponer el puerto en el que tu aplicación escucha (reemplaza 8000 con el puerto correcto)
EXPOSE 8000

# Comando para ejecutar tu aplicación con Uvicorn (ajusta main.py por el nombre de tu archivo principal)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
