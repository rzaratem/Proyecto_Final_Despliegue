from db import db
from sqlalchemy import text,Boolean

class User(db.Model):
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(255))
    email = db.Column(db.String(120), index=True, unique=True)
    fullname = db.Column(db.String(255), index=True, unique=True)
    es_admin = db.Column(db.Boolean(1), index=True, unique=True)
    es_empleado = db.Column(db.Boolean(1), index=True, unique=True)
    created_at = db.Column(db.DateTime, nullable = False, default = db.func.current_timestamp(), server_default=text('CURRENT_TIMESTAMP'))

    def __repr__(self):
        return f'<User {self.username}>'


class Producto(db.Model):
    __tablename__ = 'productos'
    id = db.Column(db.Integer, primary_key = True)
    nombre_producto = db.Column(db.String(120), nullable = False, unique = True)
    tipo_producto = db.Column(db.String(100), nullable = False)
    calorias = db.Column(db.String(50), nullable = False)
    costo = db.Column(db.Integer, nullable = False)
    precio = db.Column(db.Integer, nullable = False)
    created_at = db.Column(db.DateTime, nullable = False, default = db.func.current_timestamp(), server_default=text('CURRENT_TIMESTAMP'))
    updated_at = db.Column(db.DateTime, nullable = False, default = db.func.current_timestamp(), server_default=text('CURRENT_TIMESTAMP'), onupdate = db.func.current_timestamp())


 #Clase para ingredientes
class Ingrediente(db.Model):
    __tablename__ = 'ingredientes'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(250), nullable=False)
    precio = db.Column(db.Integer)
    calorias = db.Column(db.Integer)
    inventario = db.Column(db.Integer)
    es_vegetariano = db.Column(db.String (2))
    created_at = db.Column(db.DateTime, nullable = False, default = db.func.current_timestamp(), server_default=text('CURRENT_TIMESTAMP'))
    updated_at = db.Column(db.DateTime, nullable = False, default = db.func.current_timestamp(), server_default=text('CURRENT_TIMESTAMP'), onupdate = db.func.current_timestamp())