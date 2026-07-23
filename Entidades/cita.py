from flask import jsonify, Blueprint, request
from DataBase.db_citas import (
    obtener_citas,
    obtener_cita_por_id,
    insertar_cita,
    actualizar_cita,
    eliminar_cita
)

citas_bp = Blueprint('citas', __name__)



# ---------------------------------------------------------
# 1. OBTENER TODAS LAS CITAS (GET)
# ---------------------------------------------------------

@citas_bp.get("/citas")
def mostrar_citas():
    citas = obtener_citas()
    return jsonify(citas), 200



# ---------------------------------------------------------
# 2. OBTENER CITA POR ID (GET)
# ---------------------------------------------------------

@citas_bp.get("/citas/<int:id>")
def obtener_cita(id):
    cita = obtener_cita_por_id(id)

    if cita:
        return jsonify(cita), 200
    return jsonify({"error": f"La cita con ID {id} no ha sido encontrada"}), 404



# ---------------------------------------------------------
# 3. CREAR NUEVA CITA (POST)
# ---------------------------------------------------------

@citas_bp.post("/citas")
def crear_cita():
    datos = request.get_json()
    if not datos:
        return jsonify({"error": "Debe enviar información sobre la cita"}), 400

    campos_requeridos = ["id_sucursal", "horario_cita", "id_doctor", "id_expediente"]
    if not all(campo in datos for campo in campos_requeridos):
        return jsonify({
            "error": "Los campos id_sucursal, horario_cita, id_doctor e id_expediente son requeridos"
        }), 400

    nueva_cita = {
        "id_sucursal": datos["id_sucursal"],
        "horario_cita": datos["horario_cita"],
        "id_doctor": datos["id_doctor"],
        "id_expediente": datos["id_expediente"]
    }
    
    resultado = insertar_cita(nueva_cita)

    return jsonify(resultado), 201



# ---------------------------------------------------------
# 4. ACTUALIZAR CITA (PUT)
# ---------------------------------------------------------

@citas_bp.put("/citas/<int:id>")
def actualizar(id):
    cita_existente = obtener_cita_por_id(id)
    if not cita_existente:
        return jsonify({"error": f"La cita con ID {id} no existe"}), 404

    cambios = request.get_json()
    if not cambios:
        return jsonify({"error": "Debe enviar información para actualizar"}), 400

    resultado = actualizar_cita(id, cambios)
    return jsonify(resultado), 200



# ---------------------------------------------------------
# 5. ELIMINAR CITA (DELETE)
# ---------------------------------------------------------

@citas_bp.delete("/citas/<int:id>")
def eliminar(id):
    cita_existente = obtener_cita_por_id(id)
    if not cita_existente:
        return jsonify({"error": f"La cita con ID {id} no existe"}), 404

    resultado = eliminar_cita(id)
    return jsonify({"mensaje": f"Cita con ID {id} eliminada correctamente", "datos": resultado}), 200



# ---------------------------------------------------------
# 6. MANEJO GLOBAL DE ERRORES
# ---------------------------------------------------------

@citas_bp.app_errorhandler(Exception)
def manejar_error(error):
    return jsonify({"error": str(error)}), 500