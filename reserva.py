from excepciones import (
    ReservaInvalidaError,
    EstadoReservaError
)


class Reserva:

    def __init__(self, cliente, servicio, duracion):
        if duracion <= 0:
            raise ReservaInvalidaError(
                "La duración de la reserva debe ser mayor que cero."
            )

        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.estado = "Pendiente"

    def confirmar(self):
        if self.estado != "Pendiente":
            raise EstadoReservaError(
                "Solo las reservas pendientes pueden confirmarse."
            )

        self.estado = "Confirmada"

    def cancelar(self):
        if self.estado == "Cancelada":
            raise EstadoReservaError(
                "La reserva ya se encuentra cancelada."
            )

        self.estado = "Cancelada"

    def calcular_total(self):
        return self.servicio.calcular_costo(self.duracion)

    def mostrar_informacion(self):
        return (
            f"Cliente: {self.cliente.nombre}\n"
            f"Servicio: {self.servicio.nombre}\n"
            f"Duración: {self.duracion}\n"
            f"Estado: {self.estado}\n"
            f"Valor total: ${self.calcular_total():,.0f}"
        )