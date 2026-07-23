from flask import Flask, jsonify

from Entidades.ventas import ventas_bp 
from Entidades.sucursal import sucursales_bp 
from Entidades.servicio import servicios_bp
from Entidades.rol import roles_bp
from Entidades.personal_administrativo import empleados_admin_bp
from Entidades.paciente import pacientes_bp
from Entidades.expediente import expedientes_bp
from Entidades.especialidad import especialidades_bp
from Entidades.doctor import doctores_bp
from Entidades.cita import citas_bp

app = Flask(__name__)

app.register_blueprint(ventas_bp)
app.register_blueprint(sucursales_bp)
app.register_blueprint(servicios_bp)
app.register_blueprint(roles_bp)
app.register_blueprint(empleados_admin_bp)
app.register_blueprint(pacientes_bp)
app.register_blueprint(expedientes_bp)
app.register_blueprint(especialidades_bp)
app.register_blueprint(doctores_bp)
app.register_blueprint(citas_bp)

@app.get("/")
def inicio():
    return jsonify({
        "mensaje": "Bienvenido a la API del Sistema de Gestión Clínica",
        "version": "1.0",
        "estado": "Activo",
        "modulos_disponibles": [
            "/ventas",
            "/sucursales",
            "/servicios",
            "/roles",
            "/empleados-admin",
            "/pacientes",
            "/expedientes",
            "/especialidades",
            "/doctores",
            "/citas"
        ],
        "metodos_soportados": ["GET (Todos / Por ID)", "POST", "PUT", "DELETE"]
    }), 200

if __name__ == "__main__":
    app.run(debug=True)