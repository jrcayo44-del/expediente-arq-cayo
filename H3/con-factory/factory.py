# Sistema de ventas con inventario con el patron FACTORY

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
    def __init__(self, usuario):
        self.usuario = usuario
        self.detalles = []

    def agregar_detalle(self, detalle):
        self.detalles.append(detalle)

    def total(self):
        return sum(d.subtotal() for d in self.detalles)


# INTERFAZ / CONTRATO
class IProductoFactory(ABC):

    @abstractmethod
    def crear_producto(self, tipo):
        pass


# FACTORY 
class ProductoFactory(IProductoFactory):

    def crear_producto(self, tipo):

        if tipo == "zapato":
            categoria = Categoria("Calzados")
            return Producto("Zapato artesanal", 150, categoria)

        elif tipo == "sandalia":
            categoria = Categoria("Calzados")
            return Producto("Sandalia artesanal", 100, categoria)

        else:
            raise ValueError("Tipo de producto no válido")


usuario = Usuario("Juan")

factory = ProductoFactory()

producto = factory.crear_producto("zapato")

detalle = DetalleVenta(producto, 2)

venta = Venta(usuario)
venta.agregar_detalle(detalle)

print("Cliente:", venta.usuario.nombre)
print("Producto:", producto.nombre)
print("Categoría:", producto.categoria.nombre)
print("Total: Bs.", venta.total())
