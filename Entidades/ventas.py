from flask import jsonify, Blueprint, request
from DataBase.db_ventas import (
    obtener_ventas,
    obtener_venta_por_id,
    insertar_venta,
    actualizar_venta,
    eliminar_venta
)

ventas_bp = Blueprint('ventas', __name__)



# ---------------------------------------------------------
# 1. OBTENER TODAS LAS VENTAS (GET)
# ---------------------------------------------------------

@ventas_bp.get("/ventas")
def mostrar_ventas():
    ventas = obtener_ventas()
    return jsonify(ventas), 200



# ---------------------------------------------------------
# 2. OBTENER VENTA POR ID (GET)
# ---------------------------------------------------------

@ventas_bp.get("/ventas/<int:id>")
def obtener_venta(id):
    venta = obtener_venta_por_id(id)

    if venta:
        return jsonify(venta), 200
    return jsonify({"error": f"La venta con ID {id} no ha sido encontrada"}), 404



# ---------------------------------------------------------
# 3. CREAR NUEVA VENTA (POST)
# ---------------------------------------------------------

@ventas_bp.post("/ventas")
def crear_venta():  # Cambiado a 'crear_venta' para evitar el choque
    datos = request.get_json()
    if not datos:
        return jsonify({"error": "Debe enviar información sobre la venta"}), 400

    campos_requeridos = ["fecha_venta", "monto_venta", "id_sucursal"]
    if not all(campo in datos for campo in campos_requeridos):
        return jsonify({"error": "Los campos fecha_venta, monto_venta e id_sucursal son requeridos"}), 400

    nueva_venta = {
        "fecha_venta": datos["fecha_venta"],
        "monto_venta": datos["monto_venta"],
        "id_sucursal": datos["id_sucursal"]
    }
    
    resultado = insertar_venta(nueva_venta)

    return jsonify(resultado), 201



# ---------------------------------------------------------
# 4. ACTUALIZAR VENTA (PUT)
# ---------------------------------------------------------

@ventas_bp.put("/ventas/<int:id>")
def actualizar(id):
    venta_existente = obtener_venta_por_id(id)
    if not venta_existente:
        return jsonify({"error": f"La venta con ID {id} no existe"}), 404

    cambios = request.get_json()
    if not cambios:
        return jsonify({"error": "Debe enviar información para actualizar"}), 400

    resultado = actualizar_venta(id, cambios)
    return jsonify(resultado), 200



# ---------------------------------------------------------
# 5. ELIMINAR VENTA (DELETE)
# ---------------------------------------------------------

@ventas_bp.delete("/ventas/<int:id>")
def eliminar(id):
    venta_existente = obtener_venta_por_id(id)
    if not venta_existente:
        return jsonify({"error": f"La venta con ID {id} no existe"}), 404

    resultado = eliminar_venta(id)
    return jsonify({"mensaje": f"Venta con ID {id} eliminada correctamente", "datos": resultado}), 200



# ---------------------------------------------------------
# 6. MANEJO GLOBAL DE ERRORES
# ---------------------------------------------------------

@ventas_bp.app_errorhandler(Exception)
def manejar_error(error):
    return jsonify({"error": str(error)}), 500