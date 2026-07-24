"""
Ejecuta este script UNA VEZ para crear clinica.db a partir del schema SQL.

Uso:
    python crear_db.py

Requisitos:
    - Debe estar en la misma carpeta que 'schema_clinica_sqlite.sql'
    - Se creará (o recreará) el archivo 'clinica.db' en esta misma carpeta
"""
import sqlite3
import os

CARPETA = os.path.dirname(os.path.abspath(__file__))
SCHEMA_PATH = os.path.join(CARPETA, "schema_clinica_sqlite.sql")
DB_PATH = os.path.join(CARPETA, "clinica.db")

if not os.path.exists(SCHEMA_PATH):
    print(f"ERROR: no encuentro el archivo {SCHEMA_PATH}")
    print("Asegúrate de que 'schema_clinica_sqlite.sql' esté en esta misma carpeta.")
    exit(1)

with open(SCHEMA_PATH, "r", encoding="utf-8") as f:
    schema_sql = f.read()

conn = sqlite3.connect(DB_PATH)
conn.executescript(schema_sql)
conn.commit()
conn.close()

print(f"Listo. Base de datos creada en: {DB_PATH}")
