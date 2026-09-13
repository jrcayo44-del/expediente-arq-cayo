# Sistema de ventas con inventario con el patron BUILDER

# 1. CATEGORIA
class Categoria:
    def __init__(self, nombre):
        self.nombre = nombre


# 2. PRODUCTO
class Producto:
    def __init__(self, nombre, precio, categoria):
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria


# 3. USUARIO
class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre


# 4. DETALLE VENTA
class DetalleVenta:
    def __init__(self, producto, cantidad):
        self.producto = producto
        self.cantidad = cantidad

    def subtotal(self):
        return self.producto.precio * self.cantidad


# 5. VENTA
class Venta:
    def __init__(self):
        self.usuario = None
        self.detalles = []

    def total(self):
        return sum(d.subtotal() for d in self.detalles)


# BUILDER
class VentaBuilder:

    def __init__(self):
        self.venta = Venta()

    def con_usuario(self, usuario):
        self.venta.usuario = usuario
        return self

    def agregar_producto(self, producto, cantidad):
        self.venta.detalles.append(
            DetalleVenta(producto, cantidad)
        )
        return self

    def construir(self):
        return self.venta
    

categoria = Categoria("Zapatos")
producto = Producto("Zapato artesanal", 150, categoria)
usuario = Usuario("Juan")

venta = (
    VentaBuilder()
    .con_usuario(usuario)
    .agregar_producto(producto, 2)
    .construir()
)

print("Cliente:", venta.usuario.nombre)
print("Total: Bs.", venta.total())
