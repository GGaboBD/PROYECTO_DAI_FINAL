from flask import jsonify, Blueprint, request
from DataBase.db_personal_administrativo import (
    obtener_empleados_admin,
    obtener_empleado_admin_por_id,
    insertar_empleado_admin,
    actualizar_empleado_admin,
    eliminar_empleado_admin
)

empleados_admin_bp = Blueprint('empleados_admin', __name__)



# ---------------------------------------------------------
# 1. OBTENER TODOS LOS EMPLEADOS ADMIN (GET)
# ---------------------------------------------------------

@empleados_admin_bp.get("/empleados-admin")
def mostrar_empleados_admin():
    empleados = obtener_empleados_admin()
    return jsonify(empleados), 200



# ---------------------------------------------------------
# 2. OBTENER EMPLEADO ADMIN POR ID (GET)
# ---------------------------------------------------------

@empleados_admin_bp.get("/empleados-admin/<int:id>")
def obtener_empleado_admin(id):
    empleado = obtener_empleado_admin_por_id(id)

    if empleado:
        return jsonify(empleado), 200
    return jsonify({"error": f"El empleado administrador con ID {id} no ha sido encontrado"}), 404



# ---------------------------------------------------------
# 3. CREAR NUEVO EMPLEADO ADMIN (POST)
# ---------------------------------------------------------

@empleados_admin_bp.post("/empleados-admin")
def crear_empleado_admin():
    datos = request.get_json()
    if not datos:
        return jsonify({"error": "Debe enviar información sobre el empleado administrador"}), 400

    campos_requeridos = ["nombre", "id_rol", "id_sucursal"]
    if not all(campo in datos for campo in campos_requeridos):
        return jsonify({"error": "Los campos nombre, id_rol e id_sucursal son requeridos"}), 400

    nuevo_empleado = {
        "nombre": datos["nombre"],
        "id_rol": datos["id_rol"],
        "id_sucursal": datos["id_sucursal"]
    }
    
    resultado = insertar_empleado_admin(nuevo_empleado)

    return jsonify(resultado), 201



# ---------------------------------------------------------
# 4. ACTUALIZAR EMPLEADO ADMIN (PUT)
# ---------------------------------------------------------

@empleados_admin_bp.put("/empleados-admin/<int:id>")
def actualizar(id):
    empleado_existente = obtener_empleado_admin_por_id(id)
    if not empleado_existente:
        return jsonify({"error": f"El empleado administrador con ID {id} no existe"}), 404

    cambios = request.get_json()
    if not cambios:
        return jsonify({"error": "Debe enviar información para actualizar"}), 400

    resultado = actualizar_empleado_admin(id, cambios)
    return jsonify(resultado), 200



# ---------------------------------------------------------
# 5. ELIMINAR EMPLEADO ADMIN (DELETE)
# ---------------------------------------------------------

@empleados_admin_bp.delete("/empleados-admin/<int:id>")
def eliminar(id):
    empleado_existente = obtener_empleado_admin_por_id(id)
    if not empleado_existente:
        return jsonify({"error": f"El empleado administrador con ID {id} no existe"}), 404

    resultado = eliminar_empleado_admin(id)
    return jsonify({"mensaje": f"Empleado administrador con ID {id} eliminado correctamente", "datos": resultado}), 200



# ---------------------------------------------------------
# 6. MANEJO GLOBAL DE ERRORES
# ---------------------------------------------------------

@empleados_admin_bp.app_errorhandler(Exception)
def manejar_error(error):
    return jsonify({"error": str(error)}), 500