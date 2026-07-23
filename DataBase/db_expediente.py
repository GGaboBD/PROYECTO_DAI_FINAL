from . import supabase


"""
Acceso a datos para el módulo de Expedientes.
Responsabilidad: interacción directa con la tabla 'expedientes' en Supabase.
"""

def obtener_expedientes():
    """Devuelve todos los expedientes ordenados por ID."""
    respuesta = (
        supabase
        .table("expedientes")
        .select("*")
        .order("id")
        .execute()
    )
    return respuesta.data


def obtener_expediente_por_id(expediente_id: int):
    """
    Busca un expediente por su ID.
    Devuelve los datos si existe, o None si no se encuentra.
    """
    respuesta = (
        supabase
        .table("expedientes")
        .select("*")
        .eq("id", expediente_id)
        .execute()
    )
    
    if respuesta.data:
        return respuesta.data[0]
    
    return None


def insertar_expediente(expediente: dict):
    """Inserta un nuevo expediente en Supabase."""
    respuesta = (
        supabase
        .table("expedientes")
        .insert(expediente)
        .execute()
    )
    return respuesta.data


def actualizar_expediente(expediente_id: int, cambios: dict):
    """Actualiza los campos de un expediente existente."""
    respuesta = (
        supabase
        .table("expedientes")
        .update(cambios)
        .eq("id", expediente_id)
        .execute()
    )
    return respuesta.data


def eliminar_expediente(expediente_id: int):
    """Elimina un expediente por su ID."""
    respuesta = (
        supabase
        .table("expedientes")
        .delete()
        .eq("id", expediente_id)
        .execute()
    )
    return respuesta.data
