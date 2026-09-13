# Sistema de ventas con inventario con el patron ADAPTER

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
        print("\n----- PRODUCTO -----")
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

# PATRÓN ADAPTER

# Interfaz 

class ReglaDescuento:

    def calcular_descuento(self, total):
        raise NotImplementedError

# Sistema externo de descuentos

class SistemaDescuentoExterno:

    def obtener_descuento(self, monto, porcentaje):
        descuento = monto * porcentaje / 100

        print(
            f"Descuento externo aplicado: "
            f"{porcentaje}%"
        )

        return descuento

class AdaptadorDescuento(ReglaDescuento):

    def __init__(self, sistema_externo, porcentaje):
        self.sistema_externo = sistema_externo
        self.porcentaje = porcentaje

    def calcular_descuento(self, total):

        return self.sistema_externo.obtener_descuento(
            total,
            self.porcentaje
        )
    
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

        self.subtotal = (
            self.cantidad *
            self.precio_unitario
        )

        return self.subtotal

class Venta:

    def __init__(
        self,
        id_venta,
        fecha,
        usuario,
        regla_descuento
    ):
        self.id_venta = id_venta
        self.fecha = fecha
        self.usuario = usuario
        self.detalles = []

        self.total = 0
        self.descuento = 0
        self.total_final = 0

        self.regla_descuento = regla_descuento

    def registrar(self):

        print(
            f"\nVenta #{self.id_venta} registrada."
        )

    def agregar_detalle(self, detalle):

        self.detalles.append(detalle)

        print(
            f"Producto '{detalle.producto.nombre}' "
            f"agregado a la venta."
        )

    def calcular_total(self):

        self.total = 0

        for detalle in self.detalles:

            self.total += (
                detalle.calcular_subtotal()
            )

        # Utilizamos el Adapter
        self.descuento = (
            self.regla_descuento
            .calcular_descuento(self.total)
        )

        self.total_final = (
            self.total - self.descuento
        )

        return self.total_final

    def consultar(self):

        print("\n========== VENTA ==========")

        print(f"ID Venta: {self.id_venta}")
        print(f"Fecha: {self.fecha}")
        print(f"Cliente/Usuario: {self.usuario.nombre}")

        print("\n----- DETALLE -----")

        for detalle in self.detalles:

            print(
                f"Producto: {detalle.producto.nombre}"
            )

            print(
                f"Cantidad: {detalle.cantidad}"
            )

            print(
                f"Subtotal: Bs. {detalle.subtotal}"
            )

        print("\n---------------------------")

        print(f"Subtotal: Bs. {self.total}")

        print(
            f"Descuento: Bs. {self.descuento}"
        )

        print(
            f"TOTAL FINAL: Bs. {self.total_final}"
        )

# 1. Crear categoría
categoria = Categoria(
    1,
    "Calzados"
)

categoria.crear()


# 2. Crear producto
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


# 3. Crear usuario
usuario = Usuario(
    1,
    "Juan Pérez",
    "juan",
    "123456",
    "Activo"
)

usuario.crear()

# CREAR EL SISTEMA EXTERNO
sistema_externo = SistemaDescuentoExterno()

# CREAR EL ADAPTER
adapter = AdaptadorDescuento(
    sistema_externo,
    10
)

# CREAR VENTA
venta = Venta(
    1,
    "13/09/2026",
    usuario,
    adapter
)

# CREAR DETALLE
detalle = DetalleVenta(
    1,
    producto,
    2,
    producto.precio_venta
)

venta.agregar_detalle(detalle)

venta.registrar()

total = venta.calcular_total()

venta.consultar()
