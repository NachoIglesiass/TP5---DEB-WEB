# app.py
from flask import Flask, request, jsonify
from servicio import agregar_producto, listar_productos, obtener_producto_por_id, actualizar_producto, eliminar_producto

app = Flask(__name__)

# GET /productos → Listar todos los productos
@app.route('/productos', methods=['GET'])
def get_productos():
    return jsonify({'productos': listar_productos()})

# POST /productos → Agregar un producto
@app.route('/productos', methods=['POST'])
def create_producto():
    data = request.json
    producto = agregar_producto(data['nombre'], data['precio'])
    return jsonify({'mensaje': 'Producto agregado', 'producto': producto}), 201

# GET /productos/<id> → Obtener un producto por ID
@app.route('/productos/<int:producto_id>', methods=['GET'])
def get_producto(producto_id):
    producto = obtener_producto_por_id(producto_id)
    if producto:
        return jsonify(producto)
    return jsonify({'mensaje': 'Producto no encontrado'}), 404

# PUT /productos/<id> → Actualizar un producto
@app.route('/productos/<int:producto_id>', methods=['PUT'])
def update_producto(producto_id):
    data = request.json
    producto_actualizado = actualizar_producto(producto_id, data['nombre'], data['precio'])
    if producto_actualizado:
        return jsonify({'mensaje': 'Producto actualizado', 'producto': producto_actualizado})
    return jsonify({'mensaje': 'Producto no encontrado'}), 404

# DELETE /productos/<id> → Eliminar un producto
@app.route('/productos/<int:producto_id>', methods=['DELETE'])
def delete_producto(producto_id):
    eliminado = eliminar_producto(producto_id)
    if eliminado:
        return jsonify({'mensaje': 'Producto eliminado'})
    return jsonify({'mensaje': 'Producto no encontrado'}), 404

if __name__ == '__main__':
    app.run(debug=True)
