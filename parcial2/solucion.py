#implementacion del patron OBSERVER
from abc import ABC, abstractmethod

#FIRMA: Junior Moises Cayo Fulguera

# CONTRATO OBSERVER

class ObservadorMembresia(ABC):

    @abstractmethod
    def actualizar(self, socio):
        pass

class NotificadorWhatsApp(ObservadorMembresia):

    def actualizar(self, socio):
        print(f"WhatsApp enviado a {socio}")

class RegistroVencidos(ObservadorMembresia):

    def actualizar(self, socio):
        print(f"{socio} agregado al registro de vencidos")


class PantallaRecepcion(ObservadorMembresia):

    def actualizar(self, socio):
        print(f"Recepción informada del vencimiento de {socio}")


class ModuloSocios:

    def __init__(self):
        self.observadores = []

    def agregar_observador(self, observador):
        self.observadores.append(observador)

    def membresia_vencida(self, socio):
        print(f"\nLa membresía de {socio} venció.")

        for observador in self.observadores:
            observador.actualizar(socio)

print("=================================")
print("       GIMNASIO FUERZA ANDINA")
print("=================================")

#EJEMPLO DE USO
modulo_socios = ModuloSocios()

modulo_socios.agregar_observador(NotificadorWhatsApp())
modulo_socios.agregar_observador(RegistroVencidos())
modulo_socios.agregar_observador(PantallaRecepcion())

modulo_socios.membresia_vencida("Carlos Mendoza")
