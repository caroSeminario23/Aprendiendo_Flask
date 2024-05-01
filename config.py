from dotenv import load_dotenv # permite cargar variables de entorno desde un archivo .env
import os # permite interactuar con el sistema operativo

load_dotenv() # carga las variables de entorno desde el archivo .env

# obtiene los valores de las variables de entorno
user = os.environ.get('USER') # obtiene el valor de la variable de entorno USER
psw = os.environ.get('PASSWORD') # obtiene el valor de la variable de entorno PASSWORD
host = os.environ.get('HOST') # obtiene el valor de la variable de entorno HOST
database = os.environ.get('DATABASE') # obtiene el valor de la variable de entorno DATABASE
server = os.environ.get('SERVER') # obtiene el valor de la variable de entorno SERVER

# crea la cadena de conexión a la base de datos
DATABASE_CONNECTION = f'{server}://{user}@{host}/{database}' # cadena de conexión a la base de datos