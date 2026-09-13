# Sistema de ventas con inventario con el patron ADAPTER

from abc import ABC, abstractmethod

class Categoria:
    def __init__(self, nombre):
        self.nombre = nombre

class Producto:
    def __init__(self, nombre, precio, categoria):
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria

class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre

class DetalleVenta:
    def __init__(self, producto, cantidad):
        self.producto = producto
        self.cantidad = cantidad

    def subtotal(self):
        return self.producto.precio * self.cantidad


# INTERFAZ / CONTRATO
class MetodoPago(ABC):

    @abstractmethod
    def pagar(self, monto):
        pass

class PagoExterno:
    def procesar_pago(self, monto):
        return f"Pago externo realizado: Bs. {monto}"


# ADAPTER
class PagoAdapter(MetodoPago):

    def __init__(self, pago_externo):
        self.pago_externo = pago_externo

    def pagar(self, monto):
        return self.pago_externo.procesar_pago(monto)


class Venta:
    def __init__(self, usuario, metodo_pago: MetodoPago):
        self.usuario = usuario
        self.metodo_pago = metodo_pago
        self.detalles = []

    def agregar_detalle(self, detalle):
        self.detalles.append(detalle)

    def total(self):
        return sum(d.subtotal() for d in self.detalles)

    def realizar_pago(self):
        return self.metodo_pago.pagar(self.total())


categoria = Categoria("Calzados")

producto = Producto(
    "Zapato artesanal",
    150,
    categoria
)

usuario = Usuario("Juan")

pago_externo = PagoExterno()

adapter = PagoAdapter(pago_externo)

venta = Venta(usuario, adapter)

venta.agregar_detalle(
    DetalleVenta(producto, 2)
)

print("Cliente:", venta.usuario.nombre)
print("Total: Bs.", venta.total())
print(venta.realizar_pago())
