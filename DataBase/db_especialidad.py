from . import supabase


"""
Acceso a datos para el módulo de Especialidades.
Responsabilidad: interacción directa con la tabla 'especialidades' en Supabase.
"""

def obtener_especialidades():
    """Devuelve todas las especialidades ordenadas por ID."""
    respuesta = (
        supabase
        .table("especialidades")
        .select("*")
        .order("id")
        .execute()
    )
    return respuesta.data


def obtener_especialidad_por_id(especialidad_id: int):
    """
    Busca una especialidad por su ID.
    Devuelve los datos si existe, o None si no se encuentra.
    """
    respuesta = (
        supabase
        .table("especialidades")
        .select("*")
        .eq("id", especialidad_id)
        .execute()
    )
    
    if respuesta.data:
        return respuesta.data[0]
    
    return None


def insertar_especialidad(especialidad: dict):
    """Inserta una nueva especialidad en Supabase."""
    respuesta = (
        supabase
        .table("especialidades")
        .insert(especialidad)
        .execute()
    )
    return respuesta.data


def actualizar_especialidad(especialidad_id: int, cambios: dict):
    """Actualiza los campos de una especialidad existente."""
    respuesta = (
        supabase
        .table("especialidades")
        .update(cambios)
        .eq("id", especialidad_id)
        .execute()
    )
    return respuesta.data


def eliminar_especialidad(especialidad_id: int):
    """Elimina una especialidad por su ID."""
    respuesta = (
        supabase
        .table("especialidades")
        .delete()
        .eq("id", especialidad_id)
        .execute()
    )
    return respuesta.data
