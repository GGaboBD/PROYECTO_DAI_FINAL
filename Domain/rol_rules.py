import re


class RolRules:
    @staticmethod
    def validar_creacion(datos):
        if not datos:
            raise ValueError("Debe enviar información sobre el rol")
        if "nombre" not in datos or "descripcion" not in datos:
            raise ValueError("Los campos nombre y descripcion son requeridos")
        if not datos["nombre"].strip():
            raise ValueError("El nombre del rol no puede estar vacío")
        if not datos["descripcion"].strip():
            raise ValueError("La descripción del rol no puede estar vacía")

    @staticmethod
    def validar_identificador(valor, nombre_campo="identificador"):
        if not valor or not str(valor).strip():
            raise ValueError(f"El {nombre_campo} no puede estar vacío")
        if not re.fullmatch(r"[A-Za-z0-9]+", str(valor)):
            raise ValueError(f"El {nombre_campo} solo puede tener letras y números")
