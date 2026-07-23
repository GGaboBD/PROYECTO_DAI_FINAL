from flask import jsonify, Blueprint, request
from DataBase.db_paciente import (
    obtener_pacientes,
    obtener_paciente_por_id,
    insertar_paciente,
    actualizar_paciente,
    eliminar_paciente
)

pacientes_bp = Blueprint('pacientes', __name__)



# ---------------------------------------------------------
# 1. OBTENER TODOS LOS PACIENTES (GET)
# ---------------------------------------------------------

@pacientes_bp.get("/pacientes")
def mostrar_pacientes():
    pacientes = obtener_pacientes()
    return jsonify(pacientes), 200



# ---------------------------------------------------------
# 2. OBTENER PACIANTE POR ID (GET)
# ---------------------------------------------------------

@pacientes_bp.get("/pacientes/<int:id>")
def obtener_paciente(id):
    paciente = obtener_paciente_por_id(id)

    if paciente:
        return jsonify(paciente), 200
    return jsonify({"error": f"El paciente con ID {id} no ha sido encontrado"}), 404



# ---------------------------------------------------------
# 3. CREAR NUEVO PACIENTE (POST)
# ---------------------------------------------------------

@pacientes_bp.post("/pacientes")
def crear_paciente():
    datos = request.get_json()
    if not datos:
        return jsonify({"error": "Debe enviar información sobre el paciente"}), 400

    campos_requeridos = ["nombre_paciente", "dui_paciente", "telefono", "id_sucursal"]
    if not all(campo in datos for campo in campos_requeridos):
        return jsonify({
            "error": "Los campos nombre_paciente, dui_paciente, telefono e id_sucursal son requeridos"
        }), 400

    nuevo_paciente = {
        "nombre_paciente": datos["nombre_paciente"],
        "dui_paciente": datos["dui_paciente"],
        "telefono": datos["telefono"],
        "id_sucursal": datos["id_sucursal"]
    }
    
    resultado = insertar_paciente(nuevo_paciente)

    return jsonify(resultado), 201



# ---------------------------------------------------------
# 4. ACTUALIZAR PACIENTE (PUT)
# ---------------------------------------------------------

@pacientes_bp.put("/pacientes/<int:id>")
def actualizar(id):
    paciente_existente = obtener_paciente_por_id(id)
    if not paciente_existente:
        return jsonify({"error": f"El paciente con ID {id} no existe"}), 404

    cambios = request.get_json()
    if not cambios:
        return jsonify({"error": "Debe enviar información para actualizar"}), 400

    resultado = actualizar_paciente(id, cambios)
    return jsonify(resultado), 200



# ---------------------------------------------------------
# 5. ELIMINAR PACIENTE (DELETE)
# ---------------------------------------------------------

@pacientes_bp.delete("/pacientes/<int:id>")
def eliminar(id):
    paciente_existente = obtener_paciente_por_id(id)
    if not paciente_existente:
        return jsonify({"error": f"El paciente con ID {id} no existe"}), 404

    resultado = eliminar_paciente(id)
    return jsonify({"mensaje": f"Paciente con ID {id} eliminado correctamente", "datos": resultado}), 200



# ---------------------------------------------------------
# 6. MANEJO GLOBAL DE ERRORES
# ---------------------------------------------------------

@pacientes_bp.app_errorhandler(Exception)
def manejar_error(error):
    return jsonify({"error": str(error)}), 500