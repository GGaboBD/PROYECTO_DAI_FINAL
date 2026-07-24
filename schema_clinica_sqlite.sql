-- ============================================================
-- ESQUEMA: Sistema de Gestión Clínica
-- Base de datos: SQLite
-- Ejecutar en DBeaver (SQL Editor) conectado al archivo .db
-- o con: sqlite3 clinica.db < schema_clinica_sqlite.sql
-- ============================================================

PRAGMA foreign_keys = ON;

-- 1. ROLES
CREATE TABLE IF NOT EXISTS roles (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    descripcion TEXT
);

-- 2. ESPECIALIDADES
CREATE TABLE IF NOT EXISTS especialidades (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    descripcion TEXT
);

-- 3. SUCURSALES
CREATE TABLE IF NOT EXISTS sucursales (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    direccion TEXT,
    telefono TEXT
);

-- 4. SERVICIOS
CREATE TABLE IF NOT EXISTS servicios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    descripcion TEXT,
    precio REAL NOT NULL DEFAULT 0,
    sucursal_id INTEGER,
    FOREIGN KEY (sucursal_id) REFERENCES sucursales(id)
);

-- 5. EMPLEADOS ADMINISTRATIVOS
CREATE TABLE IF NOT EXISTS empleados_admin (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    apellido TEXT NOT NULL,
    telefono TEXT,
    email TEXT,
    rol_id INTEGER,
    sucursal_id INTEGER,
    FOREIGN KEY (rol_id) REFERENCES roles(id),
    FOREIGN KEY (sucursal_id) REFERENCES sucursales(id)
);

-- 6. DOCTORES
CREATE TABLE IF NOT EXISTS doctores (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    apellido TEXT NOT NULL,
    telefono TEXT,
    email TEXT,
    especialidad_id INTEGER,
    sucursal_id INTEGER,
    FOREIGN KEY (especialidad_id) REFERENCES especialidades(id),
    FOREIGN KEY (sucursal_id) REFERENCES sucursales(id)
);

-- 7. PACIENTES
CREATE TABLE IF NOT EXISTS pacientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    apellido TEXT NOT NULL,
    fecha_nacimiento TEXT,
    telefono TEXT,
    email TEXT,
    direccion TEXT
);

-- 8. EXPEDIENTES
CREATE TABLE IF NOT EXISTS expedientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    paciente_id INTEGER,
    doctor_id INTEGER,
    diagnostico TEXT,
    tratamiento TEXT,
    fecha TEXT DEFAULT (DATE('now')),
    FOREIGN KEY (paciente_id) REFERENCES pacientes(id),
    FOREIGN KEY (doctor_id) REFERENCES doctores(id)
);

-- 9. CITAS
CREATE TABLE IF NOT EXISTS citas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    paciente_id INTEGER,
    doctor_id INTEGER,
    sucursal_id INTEGER,
    servicio_id INTEGER,
    fecha TEXT NOT NULL,
    hora TEXT NOT NULL,
    estado TEXT DEFAULT 'pendiente',
    FOREIGN KEY (paciente_id) REFERENCES pacientes(id),
    FOREIGN KEY (doctor_id) REFERENCES doctores(id),
    FOREIGN KEY (sucursal_id) REFERENCES sucursales(id),
    FOREIGN KEY (servicio_id) REFERENCES servicios(id)
);

-- 10. VENTAS
CREATE TABLE IF NOT EXISTS ventas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    paciente_id INTEGER,
    servicio_id INTEGER,
    sucursal_id INTEGER,
    monto REAL NOT NULL,
    fecha TEXT DEFAULT (DATE('now')),
    FOREIGN KEY (paciente_id) REFERENCES pacientes(id),
    FOREIGN KEY (servicio_id) REFERENCES servicios(id),
    FOREIGN KEY (sucursal_id) REFERENCES sucursales(id)
);

-- ============================================================
-- FIN DEL SCRIPT
-- ============================================================
