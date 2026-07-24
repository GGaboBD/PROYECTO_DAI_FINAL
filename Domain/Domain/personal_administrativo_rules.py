import re


class PersonalAdministrativoRules:
    @staticmethod
    def validar_creacion(datos):
        if not datos:
            raise ValueError("Debe enviar información sobre el empleado")
        if "nombre" not in datos or "id_rol" not in datos or "id_sucursal" not in datos:
            raise ValueError("Los campos nombre, id_rol e id_sucursal son requeridos")
        if not datos["nombre"].strip():
            raise ValueError("El nombre no puede estar vacío")
        PersonalAdministrativoRules.validar_texto(datos["nombre"], "nombre")
        if not datos["id_rol"]:
            raise ValueError("El id_rol no puede estar vacío")
        if not datos["id_sucursal"]:
            raise ValueError("El id_sucursal no puede estar vacío")

    @staticmethod
    def validar_texto(valor, nombre_campo):
        if not valor or not str(valor).strip():
            raise ValueError(f"El {nombre_campo} no puede estar vacío")
        if not re.fullmatch(r"[A-Za-zÁÉÍÓÚáéíóúÑñ ]+", str(valor)):
            raise ValueError(f"El {nombre_campo} no puede contener símbolos ni números")
