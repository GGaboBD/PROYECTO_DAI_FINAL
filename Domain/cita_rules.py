# Reglas de negocio - Cita
import re
from datetime import datetime, timedelta


class CitaRules:
    @staticmethod
    def validar_creacion(datos):
        if not datos:
            raise ValueError("Debe enviar información sobre la cita")
        if "id_paciente" not in datos or "fecha_hora" not in datos or "motivo" not in datos:
            raise ValueError("Los campos id_paciente, fecha_hora y motivo son requeridos")
        if not datos["id_paciente"]:
            raise ValueError("El id_paciente no puede estar vacío")
        if not datos["fecha_hora"]:
            raise ValueError("La fecha_hora no puede estar vacía")
        if not datos["motivo"].strip():
            raise ValueError("El motivo no puede estar vacío")
        CitaRules.validar_texto(datos["motivo"], "motivo")

    @staticmethod
    def validar_estado(estado):
        estados_validos = {"programada", "confirmada", "cancelada", "completada"}
        if estado not in estados_validos:
            raise ValueError("El estado de la cita no es válido")

    @staticmethod
    def validar_texto(valor, nombre_campo):
        if not valor or not str(valor).strip():
            raise ValueError(f"El {nombre_campo} no puede estar vacío")
        if not re.fullmatch(r"[A-Za-zÁÉÍÓÚáéíóúÑñ0-9 ]+", str(valor)):
            raise ValueError(f"El {nombre_campo} no puede contener símbolos")

    @staticmethod
    def verificar_disponibilidad(nueva_cita_fecha, citas_existentes, duracion_minutos=30):
        nueva_fecha = datetime.strptime(nueva_cita_fecha, "%Y-%m-%d %H:%M")
        fin_nueva_cita = nueva_fecha + timedelta(minutes=duracion_minutos)

        for cita_existente in citas_existentes:
            fecha_existente = datetime.strptime(cita_existente, "%Y-%m-%d %H:%M")
            fin_existente = fecha_existente + timedelta(minutes=duracion_minutos)

            if nueva_fecha < fin_existente and fin_nueva_cita > fecha_existente:
                raise ValueError("Error: Ya existe una cita programada en este horario.")

        return True

    @staticmethod
    def validar_fecha_futura(fecha_cita):
        fecha = datetime.strptime(fecha_cita, "%Y-%m-%d %H:%M")
        if fecha < datetime.now():
            raise ValueError("No se puede programar una cita en una fecha u hora pasada.")
