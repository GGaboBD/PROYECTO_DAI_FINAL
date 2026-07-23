from flask import jsonify, Blueprint, request
from DataBase.db_expediente import (
    obtener_expedientes,
    obtener_expediente_por_id,
    insertar_expediente,
    actualizar_expediente,
    eliminar_expediente
)

expedientes_bp = Blueprint('expedientes', __name__)



# ---------------------------------------------------------
# 1. OBTENER TODOS LOS EXPEDIENTES (GET)
# ---------------------------------------------------------

@expedientes_bp.get("/expedientes")
def mostrar_expedientes():
    expedientes = obtener_expedientes()
    return jsonify(expedientes), 200



# ---------------------------------------------------------
# 2. OBTENER EXPEDIENTE POR ID (GET)
# ---------------------------------------------------------

@expedientes_bp.get("/expedientes/<int:id>")
def obtener_expediente(id):
    expediente = obtener_expediente_por_id(id)

    if expediente:
        return jsonify(expediente), 200
    return jsonify({"error": f"El expediente con ID {id} no ha sido encontrado"}), 404



# ---------------------------------------------------------
# 3. CREAR NUEVO EXPEDIENTE (POST)
# ---------------------------------------------------------

@expedientes_bp.post("/expedientes")
def crear_expediente():
    datos = request.get_json()
    if not datos:
        return jsonify({"error": "Debe enviar información sobre el expediente"}), 400

    campos_requeridos = [
        "id_paciente",
        "fecha_apertura",
        "alergias_medicamentos",
        "enfermedades_existentes",
        "notas_medicas"
    ]
    if not all(campo in datos for campo in campos_requeridos):
        return jsonify({
            "error": "Los campos id_paciente, fecha_apertura, alergias_medicamentos, enfermedades_existentes y notas_medicas son requeridos"
        }), 400

    nuevo_expediente = {
        "id_paciente": datos["id_paciente"],
        "fecha_apertura": datos["fecha_apertura"],
        "alergias_medicamentos": datos["alergias_medicamentos"],
        "enfermedades_existentes": datos["enfermedades_existentes"],
        "notas_medicas": datos["notas_medicas"]
    }
    
    resultado = insertar_expediente(nuevo_expediente)

    return jsonify(resultado), 201



# ---------------------------------------------------------
# 4. ACTUALIZAR EXPEDIENTE (PUT)
# ---------------------------------------------------------

@expedientes_bp.put("/expedientes/<int:id>")
def actualizar(id):
    expediente_existente = obtener_expediente_por_id(id)
    if not expediente_existente:
        return jsonify({"error": f"El expediente con ID {id} no existe"}), 404

    cambios = request.get_json()
    if not cambios:
        return jsonify({"error": "Debe enviar información para actualizar"}), 400

    resultado = actualizar_expediente(id, cambios)
    return jsonify(resultado), 200



# ---------------------------------------------------------
# 5. ELIMINAR EXPEDIENTE (DELETE)
# ---------------------------------------------------------

@expedientes_bp.delete("/expedientes/<int:id>")
def eliminar(id):
    expediente_existente = obtener_expediente_por_id(id)
    if not expediente_existente:
        return jsonify({"error": f"El expediente con ID {id} no existe"}), 404

    resultado = eliminar_expediente(id)
    return jsonify({"mensaje": f"Expediente con ID {id} eliminado correctamente", "datos": resultado}), 200



# ---------------------------------------------------------
# 6. MANEJO GLOBAL DE ERRORES
# ---------------------------------------------------------

@expedientes_bp.app_errorhandler(Exception)
def manejar_error(error):
    return jsonify({"error": str(error)}), 500