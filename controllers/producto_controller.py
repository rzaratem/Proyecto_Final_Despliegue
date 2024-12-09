from flask import Blueprint, jsonify, request
from models.heladeria import Producto, Ingrediente
from db import db

# Se crea blueprint
producto_blueprint = Blueprint('producto_bp', __name__)

# Endpoint para consultar todos los productos
@producto_blueprint.route('/productos', methods=['GET'])
def obtener_productos():
    productos = Producto.query.all()
    resultado = [
        {
            "id": p.id,
            "nombre_producto": p.nombre_producto,
            "tipo_producto": p.tipo_producto,
            "calorias": p.calorias,
            "costo": p.costo,
            "precio": p.precio,
            "created_at": p.created_at,
            "updated_at": p.updated_at
        }
        for p in productos
    ]
    return jsonify(resultado), 200


# Endpoint para consultar un producto por su ID
@producto_blueprint.route('/productos/<int:id>', methods=['GET'])
def obtener_producto_por_id(id):
    producto = Producto.query.get(id)
    if producto:
        resultado = {
            "id": producto.id,
            "nombre_producto": producto.nombre_producto,
            "tipo_producto": producto.tipo_producto,
            "calorias": producto.calorias,
            "costo": producto.costo,
            "precio": producto.precio,
            "created_at": producto.created_at,
            "updated_at": producto.updated_at
            
        }
        return jsonify(resultado), 200
    return jsonify({"mensaje": "Producto no encontrado"}), 404


# Endpoint para consultar un producto por nombre
@producto_blueprint.route('/productos/buscar', methods=['GET'])
def buscar_producto_por_nombre():
    nombre = request.args.get('nombre', '').lower()
    productos = Producto.query.filter(Producto.nombre_producto.ilike(f"%{nombre}%")).all()
    if productos:
        resultado = [
            {
                "id": p.id,
                "nombre_producto": p.nombre_producto,
                "tipo_producto": p.tipo_producto,
                "calorias": p.calorias,
                "costo": p.costo,
                "precio": p.precio
            }
            for p in productos
        ]
        return jsonify(resultado), 200
    return jsonify({"mensaje": "Producto no encontrado"}), 404


# Endpoint para consultar todos los ingredientes
@producto_blueprint.route('/ingredientes', methods=['GET'])
def obtener_ingredientes():
    ingredientes = Ingrediente.query.all()
    resultado = [
        {
            "id": i.id,
            "nombre": i.nombre,
            "precio": i.precio,
            "calorias": i.calorias,
            "inventario": i.inventario,
            "es_vegetariano": i.es_vegetariano
        }
        for i in ingredientes
    ]
    return jsonify(resultado), 200


# Endpoint para consultar un ingrediente por su ID
@producto_blueprint.route('/ingredientes/<int:id>', methods=['GET'])
def obtener_ingrediente_por_id(id):
    ingrediente = Ingrediente.query.get(id)
    if ingrediente:
        resultado = {
            "id": ingrediente.id,
            "nombre": ingrediente.nombre,
            "precio": ingrediente.precio,
            "calorias": ingrediente.calorias,
            "inventario": ingrediente.inventario
        }
        return jsonify(resultado), 200
    return jsonify({"mensaje": "Ingrediente no encontrado"}), 404
