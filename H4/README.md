# C4 del caso sistema de tienda con inventario

# Nivel 1 (el sistema y su mundo)
``` sirena
flowchart TB
    vendedor["Vendedor<br>(registra ventas)"]
    admin["Administrador<br>(ajusta stock y precios)"]
    cliente["Cliente<br>(recibe avisos de su compra)"]
    proveedor["Provedor<br>(Suministrar productos)"]
    encargado_de_inventario["encargado_de_inventari<br>(entradas y salidas de los productos)"]
    sistema[" SISTEMA PARA LA TIENDA DE ROPA <br>Registra proveedor, registra usuario, registra ventas, registra compra, controla stock"]
    vendedor -->|"registra ventas"| sistema
    admin -->|"gestiona catálogo y stock"| sistema
    proveedor -->|"suministrar producto"| sistema
    encargado_de_inventario -->|"entradas y salidas de los productos"| sistema
    sistema -->|"envía comprobantes y avisos"| correo
