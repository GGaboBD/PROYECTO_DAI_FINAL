from flask import jsonify, Blueprint, request
from DataBase.db_doctor import (
    obtener_doctores,
    obtener_doctor_por_id,
    insertar_doctor,
    actualizar_doctor,
    eliminar_doctor
)

doctores_bp = Blueprint('doctores', __name__)



# ---------------------------------------------------------
# 1. OBTENER TODOS LOS DOCTORES (GET)
# ---------------------------------------------------------

@doctores_bp.get("/doctores")
def mostrar_doctores():
    doctores = obtener_doctores()
    return jsonify(doctores), 200



# ---------------------------------------------------------
# 2. OBTENER DOCTOR POR ID (GET)
# ---------------------------------------------------------

@doctores_bp.get("/doctores/<int:id>")
def obtener_doctor(id):
    doctor = obtener_doctor_por_id(id)

    if doctor:
        return jsonify(doctor), 200
    return jsonify({"error": f"El doctor con ID {id} no ha sido encontrado"}), 404



# ---------------------------------------------------------
# 3. CREAR NUEVO DOCTOR (POST)
# ---------------------------------------------------------

@doctores_bp.post("/doctores")
def crear_doctor():
    datos = request.get_json()
    if not datos:
        return jsonify({"error": "Debe enviar información sobre el doctor"}), 400

    campos_requeridos = ["nombre_doctor", "jvpo_doctor", "id_sucursal", "id_especialidad"]
    if not all(campo in datos for campo in campos_requeridos):
        return jsonify({
            "error": "Los campos nombre_doctor, jvpo_doctor, id_sucursal e id_especialidad son requeridos"
        }), 400

    nuevo_doctor = {
        "nombre_doctor": datos["nombre_doctor"],
        "jvpo_doctor": datos["jvpo_doctor"],
        "id_sucursal": datos["id_sucursal"],
        "id_especialidad": datos["id_especialidad"]
    }
    
    resultado = insertar_doctor(nuevo_doctor)

    return jsonify(resultado), 201



# ---------------------------------------------------------
# 4. ACTUALIZAR DOCTOR (PUT)
# ---------------------------------------------------------

@doctores_bp.put("/doctores/<int:id>")
def actualizar(id):
    doctor_existente = obtener_doctor_por_id(id)
    if not doctor_existente:
        return jsonify({"error": f"El doctor con ID {id} no existe"}), 404

    cambios = request.get_json()
    if not cambios:
        return jsonify({"error": "Debe enviar información para actualizar"}), 400

    resultado = actualizar_doctor(id, cambios)
    return jsonify(resultado), 200



# ---------------------------------------------------------
# 5. ELIMINAR DOCTOR (DELETE)
# ---------------------------------------------------------

@doctores_bp.delete("/doctores/<int:id>")
def eliminar(id):
    doctor_existente = obtener_doctor_por_id(id)
    if not doctor_existente:
        return jsonify({"error": f"El doctor con ID {id} no existe"}), 404

    resultado = eliminar_doctor(id)
    return jsonify({"mensaje": f"Doctor con ID {id} eliminado correctamente", "datos": resultado}), 200



# ---------------------------------------------------------
# 6. MANEJO GLOBAL DE ERRORES
# ---------------------------------------------------------

@doctores_bp.app_errorhandler(Exception)
def manejar_error(error):
    return jsonify({"error": str(error)}), 500