from . import supabase


"""
Acceso a datos para el módulo de Roles.
Responsabilidad: interacción directa con la tabla 'roles' en Supabase.
"""

def obtener_roles():
    """Devuelve todos los roles ordenados por ID."""
    respuesta = (
        supabase
        .table("roles")
        .select("*")
        .order("id")
        .execute()
    )
    return respuesta.data


def obtener_rol_por_id(rol_id: int):
    """
    Busca un rol por su ID.
    Devuelve los datos si existe, o None si no se encuentra.
    """
    respuesta = (
        supabase
        .table("roles")
        .select("*")
        .eq("id", rol_id)
        .execute()
    )
    
    if respuesta.data:
        return respuesta.data[0]
    
    return None


def insertar_rol(rol: dict):
    """Inserta un nuevo rol en Supabase."""
    respuesta = (
        supabase
        .table("roles")
        .insert(rol)
        .execute()
    )
    return respuesta.data


def actualizar_rol(rol_id: int, cambios: dict):
    """Actualiza los campos de un rol existente."""
    respuesta = (
        supabase
        .table("roles")
        .update(cambios)
        .eq("id", rol_id)
        .execute()
    )
    return respuesta.data


def eliminar_rol(rol_id: int):
    """Elimina un rol por su ID."""
    respuesta = (
        supabase
        .table("roles")
        .delete()
        .eq("id", rol_id)
        .execute()
    )
    return respuesta.data
