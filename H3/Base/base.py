# Sistema de ventas con inventario

class Categoria:

    def __init__(self, id_categoria, nombre):
        self.id_categoria = id_categoria
        self.nombre = nombre

    def crear(self):
        print(f"Categoría '{self.nombre}' creada.")

class Producto:

    def __init__(
        self,
        id_producto,
        nombre,
        precio_compra,
        precio_venta,
        stock,
        categoria
    ):
        self.id_producto = id_producto
        self.nombre = nombre
        self.precio_compra = precio_compra
        self.precio_venta = precio_venta
        self.stock = stock
        self.categoria = categoria

    def crear(self):
        print(f"Producto '{self.nombre}' creado.")

    def mostrar_informacion(self):
        print("----- PRODUCTO -----")
        print(f"ID: {self.id_producto}")
        print(f"Nombre: {self.nombre}")
        print(f"Precio compra: Bs. {self.precio_compra}")
        print(f"Precio venta: Bs. {self.precio_venta}")
        print(f"Stock: {self.stock}")
        print(f"Categoría: {self.categoria.nombre}")

class Usuario:

    def __init__(
        self,
        id_usuario,
        nombre,
        usuario,
        contrasena,
        estado
    ):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.usuario = usuario
        self.contrasena = contrasena
        self.estado = estado

    def crear(self):
        print(f"Usuario '{self.usuario}' creado.")

class DetalleVenta:

    def __init__(
        self,
        id_detalle_venta,
        producto,
        cantidad,
        precio_unitario
    ):
        self.id_detalle_venta = id_detalle_venta
        self.producto = producto
        self.cantidad = cantidad
        self.precio_unitario = precio_unitario
        self.subtotal = 0

    def calcular_subtotal(self):
        self.subtotal = self.cantidad * self.precio_unitario
        return self.subtotal

class Venta:

    def __init__(self, id_venta, fecha, usuario):
        self.id_venta = id_venta
        self.fecha = fecha
        self.usuario = usuario
        self.detalles = []
        self.total = 0

    def registrar(self):
        print(f"Venta #{self.id_venta} registrada.")

    def agregar_detalle(self, detalle):
        self.detalles.append(detalle)
        print(f"Producto '{detalle.producto.nombre}' agregado a la venta.")

    def calcular_total(self):
        self.total = 0

        for detalle in self.detalles:
            self.total += detalle.calcular_subtotal()

        return self.total

    def consultar(self):
        print("----- VENTA -----")
        print(f"ID Venta: {self.id_venta}")
        print(f"Fecha: {self.fecha}")
        print(f"Usuario: {self.usuario.nombre}")

        print("\nProductos:")

        for detalle in self.detalles:
            print(
                f"- {detalle.producto.nombre} | "
                f"Cantidad: {detalle.cantidad} | "
                f"Subtotal: Bs. {detalle.subtotal}"
            )

        print(f"\nTOTAL: Bs. {self.total}")

# Crear categoría
categoria = Categoria(
    1,
    "Calzados"
)
categoria.crear()


# Crear producto
producto = Producto(
    1,
    "Zapato Artesanal",
    80.00,
    150.00,
    20,
    categoria
)
producto.crear()
producto.mostrar_informacion()


# Crear usuario
usuario = Usuario(
    1,
    "Juan Garcia",
    "Juan",
    "123456",
    "Activo"
)
usuario.crear()


# Crear venta
venta = Venta(
    1,
    "09/07/2026",
    usuario
)

# Crear detalle de venta
detalle = DetalleVenta(
    1,
    producto,
    2,
    producto.precio_venta
)

# Agregar detalle a la venta
venta.agregar_detalle(detalle)


# Registrar venta
venta.registrar()


# Calcular total
total = venta.calcular_total()

print(f"\nTotal calculado: Bs. {total}")

# Consultar venta
venta.consultar()
