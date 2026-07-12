"""
Clase abstracta base del sistema Software FJ.

Define la estructura común que deben implementar las entidades
principales del sistema.
"""

from abc import ABC, abstractmethod


class Entidad(ABC):
    """Clase abstracta general para las entidades del sistema."""

    @abstractmethod
    def mostrar_informacion(self):
        """
        Retorna la información principal de la entidad.

        Todas las clases que hereden de Entidad deben implementar
        este método.
        """
        pass