Proyecto de api rest en django usando django rest framework

paso a paso

install python

install django

install paquetes(mysqlclient, virtualenv, ...)

python -m virtualenv venv #crear entorno virtual 

.\venv\Scripts\activate #activar el entorno virtual

pip install Django #instalamos django en el ev

pip install djangorestframework

django-admin startproject drf . #cremos el proyecto de django rest framework

django-admin startapp api #creamos api 

creo modelos y serializers

python manage.py migrate #se crea la base de datos de sqlite3 -por defecto 

python manage.py makemigrations #creamos migracion para los modelos 

python manage.py migrate #aplica migracion dentro de la bbdd

python manage.py createsuperuser #admin admin

python manage.py runserver #ejecutamos el servidor de desarrollo

http://localhost:8000/admin/login/?next=/admin/ #admin panel 

pip install djangorestframework

creo serializer

creo fichero urls y edito el otro urls

python -m pip install django-cors-headers #instalo cors-headers
