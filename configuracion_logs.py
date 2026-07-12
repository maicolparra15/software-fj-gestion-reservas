import logging
import os

# Crear la carpeta logs si no existe
if not os.path.exists("logs"):
    os.makedirs("logs")

# Configuración del sistema de logs
logging.basicConfig(
    filename="logs/sistema.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8"
)


def registrar_evento(mensaje):
    """Registra eventos importantes del sistema."""
    logging.info(mensaje)


def registrar_error(error):
    """Registra errores detectados durante la ejecución."""
    logging.error(error)