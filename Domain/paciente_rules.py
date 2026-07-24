# Reglas de negocio - Paciente
import re


class PacienteRules:
    @staticmethod
    def validar_creacion(datos):
        if not datos:
            raise ValueError("Debe enviar información sobre el paciente")
        if "nombre_paciente" not in datos or "dui_paciente" not in datos or "telefono" not in datos or "id_sucursal" not in datos:
            raise ValueError("Los campos nombre_paciente, dui_paciente, telefono e id_sucursal son requeridos")
        if not datos["nombre_paciente"].strip():
            raise ValueError("El nombre del paciente no puede estar vacío")
        if not datos["dui_paciente"].strip():
            raise ValueError("El DUI del paciente no puede estar vacío")
        if not datos["telefono"].strip():
            raise ValueError("El teléfono no puede estar vacío")

    @staticmethod
    def validar_identificador(valor, nombre_campo="identificador"):
        if not valor or not str(valor).strip():
            raise ValueError(f"El {nombre_campo} no puede estar vacío")
        if not re.fullmatch(r"[A-Za-z0-9]+", str(valor)):
            raise ValueError(f"El {nombre_campo} solo puede tener letras y números")
