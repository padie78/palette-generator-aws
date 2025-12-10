# Usa una imagen base oficial de Python optimizada
FROM python:3.10-slim

# Establece el directorio de trabajo
WORKDIR /app

# Copia los archivos de dependencia e instala las librerías
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copia el código de la aplicación
COPY application.py ./

# Expone el puerto 8080 (EB por defecto)
EXPOSE 8080

# Comando para ejecutar la aplicación
CMD ["python", "application.py"]