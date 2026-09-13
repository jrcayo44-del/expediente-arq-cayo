# Sistema de ventas con inventario con el patron SINGLETON

from abc import ABC, abstractmethod

# INTERFAZ / CONTRATO
class IConfiguracion(ABC):

    @abstractmethod
    def establecer(self, clave, valor):
        pass

    @abstractmethod
    def obtener(self, clave):
        pass


# SINGLETON
class GestorConfiguracion(IConfiguracion):

    _instancia = None

    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
            cls._instancia.datos = {}

        return cls._instancia

    def establecer(self, clave, valor):
        self.datos[clave] = valor

    def obtener(self, clave):
        return self.datos.get(clave)


config1 = GestorConfiguracion()
config2 = GestorConfiguracion()

config1.establecer("moneda", "Bs.")
config1.establecer("iva", 13)

print(config2.obtener("moneda"))
print(config2.obtener("iva"))

print(config1 is config2)
