from utils.db import db

class TipoPredio(db.Model):
    # crea una tabla con el nombre de la clase en minúsculas
    __tablename__ = 'tipo_predio'
    id_tipo_predio = db.Column(db.Integer, primary_key=True)
    descripcion = db.Column(db.String(100))

    # crea un método para convertir el objeto en un diccionario
    def __init__(self, id_tipo_predio, nomre_predio):
        self.id_tipo_predio = id_tipo_predio
        self.nomre_predio = nomre_predio