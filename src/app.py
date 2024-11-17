from flask import Flask, render_template
import socket
import logging

app = Flask(__name__)

# Configuración del logger
logging.basicConfig(level=logging.INFO)

@app.route("/")
def index():
    try:
        host_name = socket.gethostname()
        host_ip = socket.gethostbyname(host_name)
        app.logger.info(f"Hostname: {host_name}, IP: {host_ip}")
        return render_template('index.html', hostname=host_name, ip=host_ip)
    except socket.error as e:
        app.logger.error(f"Error obteniendo el hostname o IP: {e}")
        return render_template('error.html', error_message="No se pudo obtener el hostname o la IP"), 500
    except Exception as e:
        app.logger.error(f"Error inesperado: {e}")
        return render_template('error.html', error_message="Ocurrió un error inesperado"), 500
    finally:
        app.logger.info("Solicitud procesada.")

if __name__ == "__main__":
    debug_mode = True  # Cambiar a False en producción
    app.run(host='0.0.0.0', port=8080, debug=debug_mode)

