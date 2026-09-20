from abc import ABC, abstractmethod

# CONTRATO OBSERVER

class ObservadorStock(ABC):

    @abstractmethod
    def actualizar(self, producto):
        pass

class AlertaAdministrador(ObservadorStock):

    def actualizar(self, producto):
        print(
            f"Administrador: stock bajo de {producto.nombre}. "
            f"Quedan {producto.stock} unidades."
        )


class AlertaEncargadoInventario(ObservadorStock):

    def actualizar(self, producto):
        print(
            f"Encargado de inventario: debe reponer "
            f"{producto.nombre}."
        )

# PRODUCTO 

class Producto:

    def __init__(self, nombre, precio, stock, stock_minimo=5):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
        self.stock_minimo = stock_minimo
        self.observadores = []

    def agregar_observador(self, observador):
        self.observadores.append(observador)

    def notificar(self):
        for observador in self.observadores:
            observador.actualizar(self)

    def descontar_stock(self, cantidad):

        if cantidad > self.stock:
            print("❌ Stock insuficiente")
            return False

        self.stock -= cantidad

        print(
            f"Stock actualizado de {self.nombre}: "
            f"{self.stock} unidades"
        )

        # OBSERVER
        if self.stock <= self.stock_minimo:
            self.notificar()

        return True

# CONTRATO FACTORY - MÉTODOS DE PAGO

class MetodoPago(ABC):

    @abstractmethod
    def pagar(self, monto):
        pass

class PagoEfectivo(MetodoPago):

    def pagar(self, monto):
        print(f"Pago en efectivo realizado: Bs. {monto}")


class PagoTarjeta(MetodoPago):

    def pagar(self, monto):
        print(f"Pago con tarjeta realizado: Bs. {monto}")


class PagoQR(MetodoPago):

    def pagar(self, monto):
        print(f"Pago mediante QR realizado: Bs. {monto}")


# FACTORY

class PagoFactory:

    @staticmethod
    def crear_pago(tipo):

        if tipo == "efectivo":
            return PagoEfectivo()

        elif tipo == "tarjeta":
            return PagoTarjeta()

        elif tipo == "qr":
            return PagoQR()

        else:
            raise ValueError("Método de pago no válido")

# VENTA

class Venta:

    def realizar_venta(self, producto, cantidad, tipo_pago):

        print("\n===== SISTEMA DE TIENDA CON INVENTARIO =====")

        total = producto.precio * cantidad

        # Actualiza inventario
        venta_correcta = producto.descontar_stock(cantidad)

        if not venta_correcta:
            return

        # método de pago
        metodo_pago = PagoFactory.crear_pago(tipo_pago)

        metodo_pago.pagar(total)

        print(f"Producto: {producto.nombre}")
        print(f"Cantidad: {cantidad}")
        print(f"Total: Bs. {total}")
        print("Venta realizada correctamente")

# EJEMPLO DE USO

producto = Producto(
    nombre="Teclado Gamer",
    precio=200,
    stock=7,
    stock_minimo=5
)

# Observadores
administrador = AlertaAdministrador()
encargado = AlertaEncargadoInventario()

producto.agregar_observador(administrador)
producto.agregar_observador(encargado)

# Venta
venta = Venta()

venta.realizar_venta(
    producto=producto,
    cantidad=3,
    tipo_pago="qr"
)
