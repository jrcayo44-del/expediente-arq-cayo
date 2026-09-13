# Sistema de ventas con inventario con el patron BUILDER

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

class Venta:
    def __init__(self):
        self.usuario = None
        self.detalles = []

    def total(self):
        return sum(d.subtotal() for d in self.detalles)


# INTERFAZ / CONTRATO 
class IVentaBuilder(ABC):

    @abstractmethod
    def agregar_usuario(self, usuario):
        pass

    @abstractmethod
    def agregar_producto(self, producto, cantidad):
        pass

    @abstractmethod
    def construir(self):
        pass


# BUILDER 
class VentaBuilder(IVentaBuilder):

    def __init__(self):
        self.venta = Venta()

    def agregar_usuario(self, usuario):
        self.venta.usuario = usuario
        return self

    def agregar_producto(self, producto, cantidad):
        detalle = DetalleVenta(producto, cantidad)
        self.venta.detalles.append(detalle)
        return self

    def construir(self):
        return self.venta


categoria = Categoria("Calzados")

producto = Producto(
    "Zapato artesanal",
    150,
    categoria
)

usuario = Usuario("Juan")

venta = (
    VentaBuilder()
    .agregar_usuario(usuario)
    .agregar_producto(producto, 2)
    .construir()
)

print("Cliente:", venta.usuario.nombre)
print("Producto:", producto.nombre)
print("Total: Bs.", venta.total())
