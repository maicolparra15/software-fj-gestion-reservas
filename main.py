from cliente import Cliente
from servicio import (
    ReservaSala,
    AlquilerEquipo,
    AsesoriaEspecializada
)
from reserva import Reserva
from configuracion_logs import registrar_evento, registrar_error


def ejecutar_pruebas():

    print("\n===== SISTEMA SOFTWARE FJ =====\n")

    # OPERACIÓN 1
    try:
        cliente1 = Cliente("12345678", "Juan Perez", "juan@gmail.com")
        registrar_evento("Cliente Juan creado correctamente")
        print("Cliente válido registrado.")
    except Exception as e:
        registrar_error(e)

    # OPERACIÓN 2
    try:
        cliente2 = Cliente("ABC123", "Ana", "ana@gmail.com")
    except Exception as e:
        registrar_error(e)
        print("Error controlado:", e)

    # OPERACIÓN 3
    try:
        sala = ReservaSala(20)
        registrar_evento("Servicio ReservaSala creado")
        print("Servicio sala creado.")
    except Exception as e:
        registrar_error(e)

    # OPERACIÓN 4
    try:
        equipo = AlquilerEquipo("VideoBeam")
        registrar_evento("Servicio AlquilerEquipo creado")
        print("Servicio equipo creado.")
    except Exception as e:
        registrar_error(e)

    # OPERACIÓN 5
    try:
        asesoria = AsesoriaEspecializada("Python")
        registrar_evento("Servicio Asesoria creado")
        print("Servicio asesoría creado.")
    except Exception as e:
        registrar_error(e)

    # OPERACIÓN 6
    try:
        reserva1 = Reserva(cliente1, sala, 3)
        reserva1.confirmar()
        registrar_evento("Reserva confirmada")
        print(reserva1.mostrar_informacion())
    except Exception as e:
        registrar_error(e)

    # OPERACIÓN 7
    try:
        reserva2 = Reserva(cliente1, equipo, -2)
    except Exception as e:
        registrar_error(e)
        print("Error controlado:", e)

    # OPERACIÓN 8
    try:
        costo = sala.calcular_costo(-5)
    except Exception as e:
        registrar_error(e)
        print("Error controlado:", e)

    # OPERACIÓN 9
    try:
        reserva1.cancelar()
        registrar_evento("Reserva cancelada")
        print("Reserva cancelada correctamente.")
    except Exception as e:
        registrar_error(e)

    # OPERACIÓN 10
    try:
        reserva1.confirmar()
    except Exception as e:
        registrar_error(e)
        print("Error controlado:", e)

    print("\nSistema ejecutado correctamente.\n")

    # OPERACIÓN 11 - try/except/else/finally
    try:
        nueva_reserva = Reserva(cliente1, asesoria, 2)
    except Exception as e:
        registrar_error(e)
    else:
        print("\nReserva creada usando bloque else.")
        print(nueva_reserva.mostrar_informacion())
    finally:
        print("Finalizó el proceso de creación de la reserva.\n")


if __name__ == "__main__":
    ejecutar_pruebas()