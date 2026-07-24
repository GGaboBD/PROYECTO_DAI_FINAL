import re


class ServicioRules:
    @staticmethod
    def validar_creacion(datos):
        if not datos:
            raise ValueError("Debe enviar información sobre el servicio")

        if "nombre" not in datos or "precio" not in datos:
            raise ValueError("Los campos nombre y precio son requeridos")

        if not datos["nombre"].strip():
            raise ValueError("El nombre del servicio no puede estar vacío")
        ServicioRules.validar_texto(datos["nombre"], "nombre")

        if not isinstance(datos["precio"], (int, float)) or datos["precio"] <= 0:
            raise ValueError("El precio del servicio debe ser mayor a cero")

    @staticmethod
    def validar_texto(valor, nombre_campo):
        if not valor or not str(valor).strip():
            raise ValueError(f"El {nombre_campo} no puede estar vacío")
        if not re.fullmatch(r"[A-Za-zÁÉÍÓÚáéíóúÑñ0-9 ]+", str(valor)):
            raise ValueError(f"El {nombre_campo} no puede contener símbolos")
