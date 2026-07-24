import sqlite3

#Constante con mi "base de datos"
DATABASE = "Clinicas_Dentales.db"

def obtener_conexion():
    conexion = sqlite3.connect(DATABASE)
    conexion.row_factory = sqlite3.Row #Las lineas generadas de una cosulta se tratan objetos row sqlite
    return conexion

def convertir_fila_a_diccionario(fila):
    return {
        "id": fila["id"],
        "titulo": fila["titulo"],
        "autor": fila-["autor"],
        "disponible": bool(fila["disponible"])
    }
