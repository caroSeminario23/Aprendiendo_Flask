from flask_marshmallow import Marshmallow # Importar Marshmallow para serializar y deserializar objetos
from utils.db import db # Importar la instancia de la clase SQLAlchemy para interactuar con la base de datos

ma = Marshmallow(db) # Crear una instancia de Marshmallow con la instancia de la clase SQLAlchemy