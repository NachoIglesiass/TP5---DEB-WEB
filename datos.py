# datos.py
productos = []

def agregar_producto_db(producto):
    productos.append(producto)

def obtener_productos_db():
    return productos

def obtener_producto_db(id_producto):
    for producto in productos:
        if producto['id'] == id_producto:
            return producto
    return None

def actualizar_producto_db(id_producto, nombre, precio):
    producto = obtener_producto_db(id_producto)
    if producto:
        producto['nombre'] = nombre
        producto['precio'] = precio
        return producto
    return None

def eliminar_producto_db(id_producto):
    producto = obtener_producto_db(id_producto)
    if producto:
        productos.remove(producto)
        return True
    return False
