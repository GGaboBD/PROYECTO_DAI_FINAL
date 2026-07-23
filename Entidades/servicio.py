from flask import jsonify, Blueprint, request
from DataBase.db_servicio import (
    obtener_servicios,
    obtener_servicio_por_id,
    insertar_servicio,
    actualizar_servicio,
    eliminar_servicio
)

servicios_bp = Blueprint('servicios', __name__)



# ---------------------------------------------------------
# 1. OBTENER TODOS LOS SERVICIOS (GET)
# ---------------------------------------------------------

@servicios_bp.get("/servicios")
def mostrar_servicios():
    servicios = obtener_servicios()
    return jsonify(servicios), 200



# ---------------------------------------------------------
# 2. OBTENER SERVICIO POR ID (GET)
# ---------------------------------------------------------

@servicios_bp.get("/servicios/<int:id>")
def obtener_servicio(id):
    servicio = obtener_servicio_por_id(id)

    if servicio:
        return jsonify(servicio), 200
    return jsonify({"error": f"El servicio con ID {id} no ha sido encontrado"}), 404



# ---------------------------------------------------------
# 3. CREAR NUEVO SERVICIO (POST)
# ---------------------------------------------------------

@servicios_bp.post("/servicios")
def crear_servicio():
    datos = request.get_json()
    if not datos:
        return jsonify({"error": "Debe enviar información sobre el servicio"}), 400

    campos_requeridos = ["descripcion_servicio", "costo_servicio"]
    if not all(campo in datos for campo in campos_requeridos):
        return jsonify({"error": "Los campos descripcion_servicio y costo_servicio son requeridos"}), 400

    nuevo_servicio = {
        "descripcion_servicio": datos["descripcion_servicio"],
        "costo_servicio": datos["costo_servicio"]
    }
    
    resultado = insertar_servicio(nuevo_servicio)

    return jsonify(resultado), 201



# ---------------------------------------------------------
# 4. ACTUALIZAR SERVICIO (PUT)
# ---------------------------------------------------------

@servicios_bp.put("/servicios/<int:id>")
def actualizar(id):
    servicio_existente = obtener_servicio_por_id(id)
    if not servicio_existente:
        return jsonify({"error": f"El servicio con ID {id} no existe"}), 404

    cambios = request.get_json()
    if not cambios:
        return jsonify({"error": "Debe enviar información para actualizar"}), 400

    resultado = actualizar_servicio(id, cambios)
    return jsonify(resultado), 200



# ---------------------------------------------------------
# 5. ELIMINAR SERVICIO (DELETE)
# ---------------------------------------------------------

@servicios_bp.delete("/servicios/<int:id>")
def eliminar(id):
    servicio_existente = obtener_servicio_por_id(id)
    if not servicio_existente:
        return jsonify({"error": f"El servicio con ID {id} no existe"}), 404

    resultado = eliminar_servicio(id)
    return jsonify({"mensaje": f"Servicio con ID {id} eliminado correctamente", "datos": resultado}), 200



# ---------------------------------------------------------
# 6. MANEJO GLOBAL DE ERRORES
# ---------------------------------------------------------

@servicios_bp.app_errorhandler(Exception)
def manejar_error(error):
    return jsonify({"error": str(error)}), 500