from . import supabase


"""
Acceso a datos para el módulo de Empleados Administradores.
Responsabilidad: interacción directa con la tabla 'empleados_admin' en Supabase.
"""

def obtener_empleados_admin():
    """Devuelve todos los empleados administradores ordenados por ID."""
    respuesta = (
        supabase
        .table("empleados_admin")
        .select("*")
        .order("id")
        .execute()
    )
    return respuesta.data


def obtener_empleado_admin_por_id(empleado_id: int):
    """
    Busca un empleado administrador por su ID.
    Devuelve los datos si existe, o None si no se encuentra.
    """
    respuesta = (
        supabase
        .table("empleados_admin")
        .select("*")
        .eq("id", empleado_id)
        .execute()
    )
    
    if respuesta.data:
        return respuesta.data[0]
    
    return None


def insertar_empleado_admin(empleado: dict):
    """Inserta un nuevo empleado administrador en Supabase."""
    respuesta = (
        supabase
        .table("empleados_admin")
        .insert(empleado)
        .execute()
    )
    return respuesta.data


def actualizar_empleado_admin(empleado_id: int, cambios: dict):
    """Actualiza los campos de un empleado administrador existente."""
    respuesta = (
        supabase
        .table("empleados_admin")
        .update(cambios)
        .eq("id", empleado_id)
        .execute()
    )
    return respuesta.data


def eliminar_empleado_admin(empleado_id: int):
    """Elimina un empleado administrador por su ID."""
    respuesta = (
        supabase
        .table("empleados_admin")
        .delete()
        .eq("id", empleado_id)
        .execute()
    )
    return respuesta.data
