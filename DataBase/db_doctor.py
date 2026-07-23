from . import supabase


"""
Acceso a datos para el módulo de Doctores.
Responsabilidad: interacción directa con la tabla 'doctores' en Supabase.
"""

def obtener_doctores():
    """Devuelve todos los doctores ordenados por ID."""
    respuesta = (
        supabase
        .table("doctores")
        .select("*")
        .order("id")
        .execute()
    )
    return respuesta.data


def obtener_doctor_por_id(doctor_id: int):
    """
    Busca un doctor por su ID.
    Devuelve los datos si existe, o None si no se encuentra.
    """
    respuesta = (
        supabase
        .table("doctores")
        .select("*")
        .eq("id", doctor_id)
        .execute()
    )
    
    if respuesta.data:
        return respuesta.data[0]
    
    return None


def insertar_doctor(doctor: dict):
    """Inserta un nuevo doctor en Supabase."""
    respuesta = (
        supabase
        .table("doctores")
        .insert(doctor)
        .execute()
    )
    return respuesta.data


def actualizar_doctor(doctor_id: int, cambios: dict):
    """Actualiza los campos de un doctor existente."""
    respuesta = (
        supabase
        .table("doctores")
        .update(cambios)
        .eq("id", doctor_id)
        .execute()
    )
    return respuesta.data


def eliminar_doctor(doctor_id: int):
    """Elimina un doctor por su ID."""
    respuesta = (
        supabase
        .table("doctores")
        .delete()
        .eq("id", doctor_id)
        .execute()
    )
    return respuesta.data
