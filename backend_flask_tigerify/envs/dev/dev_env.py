import os
from dotenv import load_dotenv

'''
En Python, os es un módulo que proporciona una manera de interactuar con el sistema operativo
en el que se está ejecutando el programa. Permite a los desarrolladores trabajar con diferentes
aspectos del sistema, como el sistema de archivos, 
la configuración regional, las variables de entorno, entre otros.
'''

'''
dotenv es una librería de Python que carga variables de entorno desde un archivo .env. 
Un archivo .env es simplemente un archivo de texto que contiene pares de clave-valor de variables 
de entorno, separados por igual (=) y cada par en una nueva línea.

Esta librería es comúnmente utilizada en proyectos de Python para manejar variables de entorno
que contienen información sensible, como claves API, contraseñas de bases de datos, etc. 
Al utilizar dotenv, se puede mantener esta información sensible fuera del código fuente y 
separar las configuraciones específicas del entorno en un archivo de configuración,
lo que facilita la configuración y el despliegue en diferentes entornos.
'''

# Estas configuraciones debemos cargarlas en main.py

load_dotenv()

class DevConfig:
    DEBUG = os.getenv('DEBUG_MODE') #DEBUG_MODE es la clave que está en el .env

# Esta clave dev apunta a toda la clase, la metemos en un diccionario,
# así podemos acceder a todo lo que pongamos en la clase
config = {
    'dev': DevConfig
}

# Creamos un metodo para activar las variables de entorno del .env de la database config
# Usaremos este diccionario en el main.py
def get_database_config():
    database_config = {
        'MYSQL_HOST': os.getenv('MYSQL_HOST'),
        'MYSQL_USER': os.getenv('MYSQL_USER'),
        'MYSQL_PASSWORD': os.getenv('MYSQL_PASSWORD'),
        'DATABASE_NAME': os.getenv('DATABASE_NAME'),
        'SQLALCHEMY_TRACK_MODIFICATIONS': os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS')
    }
    return database_config # Devolvemos todo este diccionario