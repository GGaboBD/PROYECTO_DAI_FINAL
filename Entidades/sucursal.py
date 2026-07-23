from flask import jsonify, Blueprint, request
from DataBase.db_sucursal import (
    obtener_sucursales,
    obtener_sucursal_por_id,
    insertar_sucursal,
    actualizar_sucursal,
    eliminar_sucursal
)

sucursales_bp = Blueprint('sucursales', __name__)



# ---------------------------------------------------------
# 1. OBTENER TODAS LAS SUCURSALES (GET)
# ---------------------------------------------------------

@sucursales_bp.get("/sucursales")
def mostrar_sucursales():
    sucursales = obtener_sucursales()
    return jsonify(sucursales), 200



# ---------------------------------------------------------
# 2. OBTENER SUCURSAL POR ID (GET)
# ---------------------------------------------------------

@sucursales_bp.get("/sucursales/<int:id>")
def obtener_sucursal(id):
    sucursal = obtener_sucursal_por_id(id)

    if sucursal:
        return jsonify(sucursal), 200
    return jsonify({"error": f"La sucursal con ID {id} no ha sido encontrada"}), 404



# ---------------------------------------------------------
# 3. CREAR NUEVA SUCURSAL (POST)
# ---------------------------------------------------------

@sucursales_bp.post("/sucursales")
def crear_sucursal():
    datos = request.get_json()
    if not datos:
        return jsonify({"error": "Debe enviar información sobre la sucursal"}), 400

    campos_requeridos = ["nombre", "direccion", "telefono"]
    if not all(campo in datos for campo in campos_requeridos):
        return jsonify({"error": "Los campos nombre, direccion y telefono son requeridos"}), 400

    nueva_sucursal = {
        "nombre": datos["nombre"],
        "direccion": datos["direccion"],
        "telefono": datos["telefono"]
    }
    
    resultado = insertar_sucursal(nueva_sucursal)

    return jsonify(resultado), 201



# ---------------------------------------------------------
# 4. ACTUALIZAR SUCURSAL (PUT)
# ---------------------------------------------------------

@sucursales_bp.put("/sucursales/<int:id>")
def actualizar(id):
    sucursal_existente = obtener_sucursal_por_id(id)
    if not sucursal_existente:
        return jsonify({"error": f"La sucursal con ID {id} no existe"}), 404

    cambios = request.get_json()
    if not cambios:
        return jsonify({"error": "Debe enviar información para actualizar"}), 400

    resultado = actualizar_sucursal(id, cambios)
    return jsonify(resultado), 200



# ---------------------------------------------------------
# 5. ELIMINAR SUCURSAL (DELETE)
# ---------------------------------------------------------

@sucursales_bp.delete("/sucursales/<int:id>")
def eliminar(id):
    sucursal_existente = obtener_sucursal_por_id(id)
    if not sucursal_existente:
        return jsonify({"error": f"La sucursal con ID {id} no existe"}), 404

    resultado = eliminar_sucursal(id)
    return jsonify({"mensaje": f"Sucursal con ID {id} eliminada correctamente", "datos": resultado}), 200



# ---------------------------------------------------------
# 6. MANEJO GLOBAL DE ERRORES
# ---------------------------------------------------------
@sucursales_bp.app_errorhandler(Exception)
def manejar_error(error):
    return jsonify({"error": str(error)}), 500