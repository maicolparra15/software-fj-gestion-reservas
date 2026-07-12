from entidad import Entidad
from excepciones import ClienteInvalidoError


class Cliente(Entidad):

    def __init__(self, documento, nombre, correo):
        self.documento = documento
        self.nombre = nombre
        self.correo = correo

    @property
    def documento(self):
        return self.__documento

    @documento.setter
    def documento(self, valor):
        if not str(valor).isdigit():
            raise ClienteInvalidoError(
                "El documento debe contener únicamente números."
            )
        self.__documento = valor

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):
        if not valor or len(valor.strip()) < 3:
            raise ClienteInvalidoError(
                "El nombre debe tener mínimo 3 caracteres."
            )
        self.__nombre = valor

    @property
    def correo(self):
        return self.__correo

    @correo.setter
    def correo(self, valor):
        if "@" not in valor or "." not in valor:
            raise ClienteInvalidoError(
                "Correo electrónico inválido."
            )
        self.__correo = valor

    def mostrar_informacion(self):
        return (
            f"Cliente: {self.nombre} - "
            f"Documento: {self.documento} - "
            f"Correo: {self.correo}"
        )