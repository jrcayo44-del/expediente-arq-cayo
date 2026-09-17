from abc import ABC, abstractmethod

class IProducto(ABC):

    @abstractmethod
    def obtener_descripcion(self):
        pass

    @abstractmethod
    def obtener_precio(self):
        pass

class ProductoBase(IProducto):

    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def obtener_descripcion(self):
        return self.nombre

    def obtener_precio(self):
        return self.precio

class ProductoDecorator(IProducto):

    def __init__(self, producto: IProducto):
        self.producto = producto

    def obtener_descripcion(self):
        return self.producto.obtener_descripcion()

    def obtener_precio(self):
        return self.producto.obtener_precio()


# 4. DECORADOR 1 - GARANTÍA

class ConGarantia(ProductoDecorator):

    def obtener_descripcion(self):
        return self.producto.obtener_descripcion() + " + Garantía extendida"

    def obtener_precio(self):
        return self.producto.obtener_precio() + 50


# 5. DECORADOR 2 - EMPAQUE ESPECIAL

class ConEmpaqueEspecial(ProductoDecorator):

    def obtener_descripcion(self):
        return self.producto.obtener_descripcion() + " + Empaque especial"

    def obtener_precio(self):
        return self.producto.obtener_precio() + 20

producto = ProductoBase("Teclado Gamer", 250)


# COMBINACIÓN 1
# Producto + Garantía

producto1 = ConGarantia(producto)

print("COMBINACIÓN 1")
print("Producto:", producto1.obtener_descripcion())
print("Precio: Bs.", producto1.obtener_precio())

print("\n----------------------------------------\n")

# COMBINACIÓN 2
# Producto + Garantía + Empaque especial

producto2 = ConEmpaqueEspecial(
                ConGarantia(
                    ProductoBase("Mouse Gamer", 150)
                )
            )

print("COMBINACIÓN 2")
print("Producto:", producto2.obtener_descripcion())
print("Precio: Bs.", producto2.obtener_precio())
