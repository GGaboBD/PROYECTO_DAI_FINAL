from . import supabase


"""
Acceso a datos para el módulo de Citas.
Responsabilidad: interacción directa con la tabla 'citas' en Supabase.
"""

def obtener_citas():
    """Devuelve todas las citas ordenadas por ID."""
    respuesta = (
        supabase
        .table("citas")
        .select("*")
        .order("id")
        .execute()
    )
    return respuesta.data


def obtener_cita_por_id(cita_id: int):
    """
    Busca una cita por su ID.
    Devuelve los datos si existe, o None si no se encuentra.
    """
    respuesta = (
        supabase
        .table("citas")
        .select("*")
        .eq("id", cita_id)
        .execute()
    )
    
    if respuesta.data:
        return respuesta.data[0]
    
    return None


def insertar_cita(cita: dict):
    """Inserta una nueva cita en Supabase."""
    respuesta = (
        supabase
        .table("citas")
        .insert(cita)
        .execute()
    )
    return respuesta.data


def actualizar_cita(cita_id: int, cambios: dict):
    """Actualiza los campos de una cita existente."""
    respuesta = (
        supabase
        .table("citas")
        .update(cambios)
        .eq("id", cita_id)
        .execute()
    )
    return respuesta.data


def eliminar_cita(cita_id: int):
    """Elimina una cita por su ID."""
    respuesta = (
        supabase
        .table("citas")
        .delete()
        .eq("id", cita_id)
        .execute()
    )
    return respuesta.data