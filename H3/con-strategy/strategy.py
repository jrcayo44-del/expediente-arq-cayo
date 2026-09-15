from abc import ABC, abstractmethod

class EstrategiaPago(ABC):

    @abstractmethod
    def pagar(self, monto):
        pass

# ESTRATEGIA 1

class PagoEfectivo(EstrategiaPago):

    def pagar(self, monto):
        print(f"Pago en efectivo: Bs. {monto}")

# ESTRATEGIA 2

class PagoTarjeta(EstrategiaPago):

    def pagar(self, monto):
        print(f"Pago con tarjeta: Bs. {monto}")

# ESTRATEGIA 3

class PagoQR(EstrategiaPago):

    def pagar(self, monto):
        print(f"Pago mediante QR: Bs. {monto}")


class Venta:

    def __init__(self, estrategia_pago):
        self.estrategia_pago = estrategia_pago

    def cambiar_estrategia(self, estrategia_pago):
        self.estrategia_pago = estrategia_pago

    def realizar_pago(self, monto):
        self.estrategia_pago.pagar(monto)


venta = Venta(PagoEfectivo())
venta.realizar_pago(100)

venta.cambiar_estrategia(PagoTarjeta())
venta.realizar_pago(250)

venta.cambiar_estrategia(PagoQR())
venta.realizar_pago(80)
