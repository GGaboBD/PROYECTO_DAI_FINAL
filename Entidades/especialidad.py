from flask import jsonify, Blueprint, request
from DataBase.db_especialidad import (
    obtener_especialidades,
    obtener_especialidad_por_id,
    insertar_especialidad,
    actualizar_especialidad,
    eliminar_especialidad
)

especialidades_bp = Blueprint('especialidades', __name__)



# ---------------------------------------------------------
# 1. OBTENER TODAS LAS ESPECIALIDADES (GET)
# ---------------------------------------------------------

@especialidades_bp.get("/especialidades")
def mostrar_especialidades():
    especialidades = obtener_especialidades()
    return jsonify(especialidades), 200



# ---------------------------------------------------------
# 2. OBTENER ESPECIALIDAD POR ID (GET)
# ---------------------------------------------------------

@especialidades_bp.get("/especialidades/<int:id>")
def obtener_especialidad(id):
    especialidad = obtener_especialidad_por_id(id)

    if especialidad:
        return jsonify(especialidad), 200
    return jsonify({"error": f"La especialidad con ID {id} no ha sido encontrada"}), 404



# ---------------------------------------------------------
# 3. CREAR NUEVA ESPECIALIDAD (POST)
# ---------------------------------------------------------

@especialidades_bp.post("/especialidades")
def crear_especialidad():
    datos = request.get_json()
    if not datos:
        return jsonify({"error": "Debe enviar información sobre la especialidad"}), 400

    campos_requeridos = ["especialidad_descripcion"]
    if not all(campo in datos for campo in campos_requeridos):
        return jsonify({"error": "El campo especialidad_descripcion es requerido"}), 400

    nueva_especialidad = {
        "especialidad_descripcion": datos["especialidad_descripcion"]
    }
    
    resultado = insertar_especialidad(nueva_especialidad)

    return jsonify(resultado), 201



# ---------------------------------------------------------
# 4. ACTUALIZAR ESPECIALIDAD (PUT)
# ---------------------------------------------------------

@especialidades_bp.put("/especialidades/<int:id>")
def actualizar(id):
    especialidad_existente = obtener_especialidad_por_id(id)
    if not especialidad_existente:
        return jsonify({"error": f"La especialidad con ID {id} no existe"}), 404

    cambios = request.get_json()
    if not cambios:
        return jsonify({"error": "Debe enviar información para actualizar"}), 400

    resultado = actualizar_especialidad(id, cambios)
    return jsonify(resultado), 200



# ---------------------------------------------------------
# 5. ELIMINAR ESPECIALIDAD (DELETE)
# ---------------------------------------------------------

@especialidades_bp.delete("/especialidades/<int:id>")
def eliminar(id):
    especialidad_existente = obtener_especialidad_por_id(id)
    if not especialidad_existente:
        return jsonify({"error": f"La especialidad con ID {id} no existe"}), 404

    resultado = eliminar_especialidad(id)
    return jsonify({"mensaje": f"Especialidad con ID {id} eliminada correctamente", "datos": resultado}), 200



# ---------------------------------------------------------
# 6. MANEJO GLOBAL DE ERRORES
# ---------------------------------------------------------

@especialidades_bp.app_errorhandler(Exception)
def manejar_error(error):
    return jsonify({"error": str(error)}), 500