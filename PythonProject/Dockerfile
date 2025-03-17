# Imagen base
FROM python:3.9

# Establecer directorio de trabajo
WORKDIR /app

# Copiar archivos
COPY src/ /app/

# Instalar dependencias
RUN pip install -r requirements.txt

# Exponer el puerto
EXPOSE 5000

# Comando de ejecución
CMD ["python", "app.py"]
