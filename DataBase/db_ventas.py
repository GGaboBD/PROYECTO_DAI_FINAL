from . import supabase

def obtener_ventas():
    respuesta = (
        supabase
        .table("ventas")
        .select("*")
        .order("id")
        .execute()
    )
    return respuesta.data


def obtener_venta_por_id(venta_id: int):
    respuesta = (
        supabase
        .table("ventas")
        .select("*")
        .eq("id", venta_id)
        .execute()
    )
    
    if respuesta.data:
        return respuesta.data[0]
    
    return None


def insertar_venta(venta: dict):
    respuesta = (
        supabase
        .table("ventas")
        .insert(venta)
        .execute()
    )
    return respuesta.data


def actualizar_venta(venta_id: int, cambios: dict):
    respuesta = (
        supabase
        .table("ventas")
        .update(cambios)
        .eq("id", venta_id)
        .execute()
    )
    return respuesta.data


def eliminar_venta(venta_id: int):

    respuesta = (
        supabase
        .table("ventas")
        .delete()
        .eq("id", venta_id)
        .execute()
    )
    return respuesta.data

