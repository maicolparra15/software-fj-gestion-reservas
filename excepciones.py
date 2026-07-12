"""
Excepciones personalizadas del sistema Software FJ.

Estas clases permiten identificar y controlar errores específicos
relacionados con clientes, servicios, reservas y cálculos.
"""


class ErrorSoftwareFJ(Exception):
    """Excepción base para todos los errores del sistema."""

    pass


class DatoInvalidoError(ErrorSoftwareFJ):
    """Se genera cuando un dato ingresado no es válido."""

    pass


class ClienteInvalidoError(ErrorSoftwareFJ):
    """Se genera cuando los datos de un cliente son incorrectos."""

    pass


class ServicioInvalidoError(ErrorSoftwareFJ):
    """Se genera cuando un servicio contiene datos incorrectos."""

    pass


class ServicioNoDisponibleError(ErrorSoftwareFJ):
    """Se genera cuando un servicio no se encuentra disponible."""

    pass


class ReservaInvalidaError(ErrorSoftwareFJ):
    """Se genera cuando una reserva no cumple los requisitos."""

    pass


class DuracionInvalidaError(ErrorSoftwareFJ):
    """Se genera cuando la duración indicada no es válida."""

    pass


class OperacionNoPermitidaError(ErrorSoftwareFJ):
    """Se genera cuando una operación no puede realizarse."""

    pass


class EstadoReservaError(ErrorSoftwareFJ):
    """Se genera cuando el estado de la reserva impide una operación."""

    pass


class CalculoCostoError(ErrorSoftwareFJ):
    """Se genera cuando ocurre un error al calcular un costo."""

    pass