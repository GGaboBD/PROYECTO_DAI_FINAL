from . import supabase


"""
Acceso a datos para el módulo de Servicios.
Responsabilidad: interacción directa con la tabla 'servicios' en Supabase.
"""

def obtener_servicios():
    """Devuelve todos los servicios ordenados por ID."""
    respuesta = (
        supabase
        .table("servicios")
        .select("*")
        .order("id")
        .execute()
    )
    return respuesta.data


def obtener_servicio_por_id(servicio_id: int):
    """
    Busca un servicio por su ID.
    Devuelve los datos si existe, o None si no se encuentra.
    """
    respuesta = (
        supabase
        .table("servicios")
        .select("*")
        .eq("id", servicio_id)
        .execute()
    )
    
    if respuesta.data:
        return respuesta.data[0]
    
    return None


def insertar_servicio(servicio: dict):
    """Inserta un nuevo servicio en Supabase."""
    respuesta = (
        supabase
        .table("servicios")
        .insert(servicio)
        .execute()
    )
    return respuesta.data


def actualizar_servicio(servicio_id: int, cambios: dict):
    """Actualiza los campos de un servicio existente."""
    respuesta = (
        supabase
        .table("servicios")
        .update(cambios)
        .eq("id", servicio_id)
        .execute()
    )
    return respuesta.data


def eliminar_servicio(servicio_id: int):
    """Elimina un servicio por su ID."""
    respuesta = (
        supabase
        .table("servicios")
        .delete()
        .eq("id", servicio_id)
        .execute()
    )
    return respuesta.data
