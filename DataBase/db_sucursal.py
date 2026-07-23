from . import supabase

"""
Acceso a datos para el módulo de Sucursales.
Responsabilidad: interacción directa con la tabla 'sucursales' en Supabase.
"""

def obtener_sucursales():
    """Devuelve todas las sucursales ordenadas por ID."""
    respuesta = (
        supabase
        .table("sucursales")
        .select("*")
        .order("id")
        .execute()
    )
    return respuesta.data


def obtener_sucursal_por_id(sucursal_id: int):
    """
    Busca una sucursal por su ID.
    Devuelve los datos si existe, o None si no se encuentra.
    """
    respuesta = (
        supabase
        .table("sucursales")
        .select("*")
        .eq("id", sucursal_id)
        .execute()
    )
    
    if respuesta.data:
        return respuesta.data[0]
    
    return None


def insertar_sucursal(sucursal: dict):
    """Inserta una nueva sucursal en Supabase."""
    respuesta = (
        supabase
        .table("sucursales")
        .insert(sucursal)
        .execute()
    )
    return respuesta.data


def actualizar_sucursal(sucursal_id: int, cambios: dict):
    """Actualiza los campos de una sucursal existente."""
    respuesta = (
        supabase
        .table("sucursales")
        .update(cambios)
        .eq("id", sucursal_id)
        .execute()
    )
    return respuesta.data


def eliminar_sucursal(sucursal_id: int):
    """Elimina una sucursal por su ID."""
    respuesta = (
        supabase
        .table("sucursales")
        .delete()
        .eq("id", sucursal_id)
        .execute()
    )
    return respuesta.data
