from abc import ABC, abstractmethod
from excepciones import ServicioInvalidoError


class Servicio(ABC):

    def __init__(self, nombre, tarifa_base):
        self.nombre = nombre
        self.tarifa_base = tarifa_base

    @abstractmethod
    def calcular_costo(self, cantidad):
        pass

    @abstractmethod
    def descripcion(self):
        pass


class ReservaSala(Servicio):

    def __init__(self, capacidad, tarifa_base=50000):
        super().__init__("Reserva de Sala", tarifa_base)
        self.capacidad = capacidad

    def calcular_costo(self, horas):
        if horas <= 0:
            raise ServicioInvalidoError(
                "La cantidad de horas debe ser mayor que cero."
            )
        return self.tarifa_base * horas

    def descripcion(self):
        return f"Sala para {self.capacidad} personas."


class AlquilerEquipo(Servicio):

    def __init__(self, tipo_equipo, tarifa_base=30000):
        super().__init__("Alquiler de Equipo", tarifa_base)
        self.tipo_equipo = tipo_equipo

    def calcular_costo(self, dias):
        if dias <= 0:
            raise ServicioInvalidoError(
                "La cantidad de días debe ser mayor que cero."
            )
        return self.tarifa_base * dias

    def descripcion(self):
        return f"Alquiler de equipo tipo {self.tipo_equipo}."


class AsesoriaEspecializada(Servicio):

    def __init__(self, especialidad, tarifa_base=120000):
        super().__init__("Asesoría Especializada", tarifa_base)
        self.especialidad = especialidad

    def calcular_costo(self, horas):
        if horas <= 0:
            raise ServicioInvalidoError(
                "La cantidad de horas debe ser mayor que cero."
            )
        return self.tarifa_base * horas

    def descripcion(self):
        return f"Asesoría especializada en {self.especialidad}."