# servicio.py
from datos import (
    agregar_producto_db,
    obtener_productos_db,
    obtener_producto_db,
    actualizar_producto_db,
    eliminar_producto_db
)

def agregar_producto(nombre, precio):
    producto = {
        'id': len(obtener_productos_db()) + 1,
        'nombre': nombre,
        'precio': precio
    }
    agregar_producto_db(producto)
    return producto

def listar_productos():
    return obtener_productos_db()

def obtener_producto_por_id(id_producto):
    return obtener_producto_db(id_producto)

def actualizar_producto(id_producto, nombre, precio):
    return actualizar_producto_db(id_producto, nombre, precio)

def eliminar_producto(id_producto):
    return eliminar_producto_db(id_producto)
