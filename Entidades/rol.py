from flask import jsonify, Blueprint, request
from DataBase.db_rol import (
    obtener_roles,
    obtener_rol_por_id,
    insertar_rol,
    actualizar_rol,
    eliminar_rol
)

roles_bp = Blueprint('roles', __name__)



# ---------------------------------------------------------
# 1. OBTENER TODOS LOS ROLES (GET)
# ---------------------------------------------------------

@roles_bp.get("/roles")
def mostrar_roles():
    roles = obtener_roles()
    return jsonify(roles), 200



# ---------------------------------------------------------
# 2. OBTENER ROL POR ID (GET)
# ---------------------------------------------------------

@roles_bp.get("/roles/<int:id>")
def obtener_rol(id):
    rol = obtener_rol_por_id(id)

    if rol:
        return jsonify(rol), 200
    return jsonify({"error": f"El rol con ID {id} no ha sido encontrado"}), 404



# ---------------------------------------------------------
# 3. CREAR NUEVO ROL (POST)
# ---------------------------------------------------------

@roles_bp.post("/roles")
def crear_rol():
    datos = request.get_json()
    if not datos:
        return jsonify({"error": "Debe enviar información sobre el rol"}), 400

    campos_requeridos = ["nombre_rol", "descripcion"]
    if not all(campo in datos for campo in campos_requeridos):
        return jsonify({"error": "Los campos nombre_rol y descripcion son requeridos"}), 400

    nuevo_rol = {
        "nombre_rol": datos["nombre_rol"],
        "descripcion": datos["descripcion"]
    }
    
    resultado = insertar_rol(nuevo_rol)

    return jsonify(resultado), 201



# ---------------------------------------------------------
# 4. ACTUALIZAR ROL (PUT)
# ---------------------------------------------------------

@roles_bp.put("/roles/<int:id>")
def actualizar(id):
    rol_existente = obtener_rol_por_id(id)
    if not rol_existente:
        return jsonify({"error": f"El rol con ID {id} no existe"}), 404

    cambios = request.get_json()
    if not cambios:
        return jsonify({"error": "Debe enviar información para actualizar"}), 400

    resultado = actualizar_rol(id, cambios)
    return jsonify(resultado), 200



# ---------------------------------------------------------
# 5. ELIMINAR ROL (DELETE)
# ---------------------------------------------------------

@roles_bp.delete("/roles/<int:id>")
def eliminar(id):
    rol_existente = obtener_rol_por_id(id)
    if not rol_existente:
        return jsonify({"error": f"El rol con ID {id} no existe"}), 404

    resultado = eliminar_rol(id)
    return jsonify({"mensaje": f"Rol con ID {id} eliminado correctamente", "datos": resultado}), 200



# ---------------------------------------------------------
# 6. MANEJO GLOBAL DE ERRORES
# ---------------------------------------------------------

@roles_bp.app_errorhandler(Exception)
def manejar_error(error):
    return jsonify({"error": str(error)}), 500