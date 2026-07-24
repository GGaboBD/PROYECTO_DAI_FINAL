# Reglas de negocio - Venta
import datetime
import re


class VentaRules:
    @staticmethod
    def validar_creacion(datos):
        if not datos:
            raise ValueError("Debe enviar información sobre la venta")
        if "fecha_venta" not in datos or "monto_venta" not in datos or "id_sucursal" not in datos:
            raise ValueError("Los campos fecha_venta, monto_venta e id_sucursal son requeridos")
        if not datos["fecha_venta"].strip():
            raise ValueError("La fecha de venta no puede estar vacía")
        if datos["monto_venta"] <= 0:
            raise ValueError("El monto de venta debe ser mayor a cero")

        fecha_venta = datetime.strptime(datos["fecha_venta"], "%Y-%m-%d")
        if fecha_venta > datetime.now():
            raise ValueError("La fecha de venta no puede ser futura")

    @staticmethod
    def validar_identificador(valor, nombre_campo="identificador"):
        if not valor or not str(valor).strip():
            raise ValueError(f"El {nombre_campo} no puede estar vacío")
        if not re.fullmatch(r"[A-Za-z0-9]+", str(valor)):
            raise ValueError(f"El {nombre_campo} solo puede tener letras y números")
