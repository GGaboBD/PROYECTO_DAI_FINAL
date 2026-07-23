from . import supabase

"""
Acceso a datos para el módulo de Pacientes.
Responsabilidad: interacción directa con la tabla 'pacientes' en Supabase.
"""

def obtener_pacientes():
    """Devuelve todos los pacientes ordenados por ID."""
    respuesta = (
        supabase
        .table("pacientes")
        .select("*")
        .order("id")
        .execute()
    )
    return respuesta.data


def obtener_paciente_por_id(paciente_id: int):
    """
    Busca un paciente por su ID.
    Devuelve los datos si existe, o None si no se encuentra.
    """
    respuesta = (
        supabase
        .table("pacientes")
        .select("*")
        .eq("id", paciente_id)
        .execute()
    )
    
    if respuesta.data:
        return respuesta.data[0]
    
    return None


def insertar_paciente(paciente: dict):
    """Inserta un nuevo paciente en Supabase."""
    respuesta = (
        supabase
        .table("pacientes")
        .insert(paciente)
        .execute()
    )
    return respuesta.data


def actualizar_paciente(paciente_id: int, cambios: dict):
    """Actualiza los campos de un paciente existente."""
    respuesta = (
        supabase
        .table("pacientes")
        .update(cambios)
        .eq("id", paciente_id)
        .execute()
    )
    return respuesta.data


def eliminar_paciente(paciente_id: int):
    """Elimina un paciente por su ID."""
    respuesta = (
        supabase
        .table("pacientes")
        .delete()
        .eq("id", paciente_id)
        .execute()
    )
    return respuesta.data
