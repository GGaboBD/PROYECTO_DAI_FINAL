# Reglas de negocio - Sucursal
import re


class SucursalRules:
    @staticmethod
    def validar_creacion(datos):
        if not datos:
            raise ValueError("Debe enviar información sobre la sucursal")
        if "nombre" not in datos or "direccion" not in datos or "telefono" not in datos:
            raise ValueError("Los campos nombre, direccion y telefono son requeridos")
        if not datos["nombre"].strip():
            raise ValueError("El nombre de la sucursal no puede estar vacío")
        SucursalRules.validar_texto(datos["nombre"], "nombre")
        if not datos["direccion"].strip():
            raise ValueError("La dirección no puede estar vacía")
        if not datos["telefono"].strip():
            raise ValueError("El teléfono no puede estar vacío")

        try:
            from rutas.sucursal import sucursales
        except Exception:
            sucursales = []

        nombres = [s["nombre"].lower() for s in sucursales]
        if datos["nombre"].lower() in nombres:
            raise ValueError("Ya existe una sucursal con ese nombre")

    @staticmethod
    def validar_texto(valor, nombre_campo):
        if not valor or not str(valor).strip():
            raise ValueError(f"El {nombre_campo} no puede estar vacío")
        if not re.fullmatch(r"[A-Za-zÁÉÍÓÚáéíóúÑñ0-9 ]+", str(valor)):
            raise ValueError(f"El {nombre_campo} no puede contener símbolos")
