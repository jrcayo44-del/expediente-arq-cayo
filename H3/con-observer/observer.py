rom abc import ABC, abstractmethod

class Observador(ABC):

    @abstractmethod
    def actualizar(self, producto, cantidad):
        pass

# OBSERVADOR 1: INVENTARIO

class Inventario(Observador):

    def __init__(self):
        self.stock = {
            "Martillo": 10,
            "Taladro": 5,
            "Destornillador": 20
        }

    def actualizar(self, producto, cantidad):
        if producto in self.stock:
            self.stock[producto] -= cantidad

            print(
                f"Inventario actualizado: "
                f"{producto} ahora tiene {self.stock[producto]} unidades."
            )

# OBSERVADOR 2: CLIENTE

class Cliente(Observador):

    def __init__(self, nombre):
        self.nombre = nombre

    def actualizar(self, producto, cantidad):
        print(
            f"Notificación para {self.nombre}: "
            f"Compraste {cantidad} unidad(es) de {producto}."
        )

class Venta:

    def __init__(self):
        self.observadores = []

    def suscribir(self, observador):
        self.observadores.append(observador)

    def notificar(self, producto, cantidad):
        for observador in self.observadores:
            observador.actualizar(producto, cantidad)

    def registrar_venta(self, producto, cantidad):
        print(
            f"\nVenta registrada: "
            f"{cantidad} unidad(es) de {producto}"
        )

        # Avisamos a todos los observadores
        self.notificar(producto, cantidad)


inventario = Inventario()
cliente = Cliente("Juan")

venta = Venta()

# Suscribir observadores
venta.suscribir(inventario)
venta.suscribir(cliente)

# Registrar una venta
venta.registrar_venta("Taladro", 2)
