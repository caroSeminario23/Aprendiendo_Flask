from utils.db import db # importa la instancia de la clase SQLAlchemy para interactuar con la base de datos
from model.tipo_predio import TipoPredio # importa el decorador dataclass para crear una clase de datos

class Predio(db.Model):
    __tablename__ = 'predio' # crea una tabla con el nombre de la clase en minúsculas
    id_predio = db.Column(db.Integer, primary_key=True) # crea una columna de tipo entero que es la clave primaria
    id_tipo_predio = db.Column(db.Integer, db.ForeignKey('tipo_predio.id_tipo_predio')) # crea una columna de tipo entero que es una clave foránea
    descripcion = db.Column(db.String(100))
    ruc = db.Column(db.String(20))
    telefono = db.Column(db.String(10))
    correo = db.Column(db.String(80))
    direccion = db.Column(db.String(100))
    idubigeo = db.Column(db.String(6))
    id_persona = db.Column(db.Integer, db.ForeignKey('persona.id_persona')) # crea una columna de tipo entero que es una clave foránea
    url_imagen = db.Column(db.String(100))
    total_mdu = db.Column(db.Integer)

    tipo_predio = db.relationship('TipoPredio', backref=db.backref('predio', lazy=True)) # crea una relación con la tabla tipo_predio
    # Backref crea una propiedad en la clase TipoPredio que permite acceder a la clase Predio
    # Lazy=True indica que la relación se cargará cuando se acceda a ella por primera vez

    # crea un método para convertir el objeto en un diccionario
    def __init__(self, id_predio, id_tipo_predio, descripcion, ruc, telefono, correo, direccion, idubigeo, id_persona, url_imagen, total_mdu):
        self.id_predio = id_predio
        self.id_tipo_predio = id_tipo_predio
        self.descripcion = descripcion
        self.ruc = ruc
        self.telefono = telefono
        self.correo = correo
        self.direccion = direccion
        self.idubigeo = idubigeo
        self.id_persona = id_persona
        self.url_imagen = url_imagen
        self.total_mdu = total_mdu

    # crea un método para convertir el objeto en un diccionario
    def __init__(self, id_predio, id_tipo_predio, descripcion, ruc, telefono, correo, direccion):
        self.id_predio = id_predio
        self.id_tipo_predio = id_tipo_predio
        self.descripcion = descripcion
        self.ruc = ruc
        self.telefono = telefono
        self.correo = correo
        self.direccion = direccion