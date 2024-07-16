# Paso a Paso para Configurar Proyecto Django Rest Framework

1. **Instalar Python:**
   - Descargar e instalar Python desde [python.org](https://www.python.org/).

2. **Instalar Django:**
   ```bash
   pip install django

    Instalar paquetes adicionales:
        Instalar los paquetes necesarios como mysqlclient, virtualenv, etc.

    Crear y activar entorno virtual:

    bash

python -m virtualenv venv  # Crear entorno virtual
.\venv\Scripts\activate    # Activar el entorno virtual en Windows

Instalar Django dentro del entorno virtual:

bash

pip install Django

Crear el proyecto Django Rest Framework:

bash

django-admin startproject drf .

Crear una aplicación dentro del proyecto:

bash

django-admin startapp api

Definir modelos y realizar otras configuraciones necesarias.

Migrar la base de datos inicial:

bash

python manage.py migrate

Crear migraciones para los modelos definidos:

bash

python manage.py makemigrations

Aplicar las migraciones en la base de datos:

bash

python manage.py migrate

Crear un superusuario para acceder al panel de administración:

bash

python manage.py createsuperuser

Iniciar el servidor de desarrollo:

bash

python manage.py runserver

Acceder al panel de administración:

    Abre tu navegador y visita http://localhost:8000/admin/login/?next=/admin/.

Instalar Django REST framework y otras dependencias:

bash

pip install djangorestframework
python -m pip install django-cors-headers
