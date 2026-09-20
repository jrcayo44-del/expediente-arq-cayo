# C4 del caso sistema de tienda con inventario

# Nivel 1 - Contexto (el sistema y su mundo) <br>
¿quién usa el sistema y con qué otros sistemas habla?
- Principalmente lo usan el vendedor, para registrar las ventas y cobrar a los clientes; el administrador, para gestionar productos, usuarios y reportes; y el encargado de inventario, para controlar las existencias, entradas, salidas y niveles de stock.<br>
- El sistema se comunica con una pasarela de pagos para procesar pagos electrónicos, con un sistema del proveedor para apoyar la reposición de productos, y con un servicio de notificaciones para enviar avisos por WhatsApp.
```mermaid
flowchart TB
    vendedor["👤 Vendedor<br>(registra ventas, consultar productos y verificar stock)"]
    administrador["🧑‍💼 Administrador<br>(Gestionar usuarios, proveedores, productos,inventario y reportes)"]
    encargado["👤 Encargado_de_inventario<br>(controlar entradas y salidas de productos)"]
    sistema["🏪 SISTEMA DE TIENDA CON INVENTARIO<br>Registra Usuario,registra proveedor,
registra compra,registra venta,controla stock,genera reportes"]
    notificacion["🔔 Servicio de notificaciones por WhatsApp<br>(externo)"]
    pasarela["💳 Pasarela de pagos<br>(externa)"]
    proveedor["🚚 sistema del proveedor<br>(externa)"]
    vendedor -->|"registra ventas"| sistema
    encargado -->|"controla entradas/salidas"| sistema
    administrador -->|"Gestionar reportes y stock"| sistema
    sistema -->|"envía comprobantes y avisos"| notificacion
    sistema -->|"cobra en línea"| pasarela
    proveedor -->|"realiza reposición de productos"| sistema
```

# Nivel 2 — Contenedores (el zoom adentro del sistema) <br>
¿de qué piezas ejecutables/almacenes está hecho el sistema?
- Las piezas ejecutables son la Aplicación Web, que interactúa con el sistema; la Lógica de Negocio; el Servicio de Avisos, que genera notificaciones y una base de datos MySQL.

```mermaid
flowchart TB
    vendedor["👤 Vendedor"]
    administrador["🧑‍💼 Administrador"]
    encargado["👤 Encargado de inventario"]
    subgraph sistema["🏪 SISTEMA DE TIENDA CON INVENTARIO"]
        webapp["🌐 Aplicación web<br>Python / Django<br>Pantallas de venta, stock y reportes"]
        api["⚙️ Lógica de negocio<br>Python<br>Ventas, descuentos, inventario, pagos<br>Factory:Elige el descuento y método de pago"]
        bd[("🗄️ Base de datos<br>MySQL<br>Productos, ventas, movimientos, usuarios, proveedores")]
        avisos["🛎️ Servicio de avisos<br>Python<br>Observer: publica stock-bajo<br>a los suscriptores"]
    end
    correo["🔔 Servicio de notificaciones (externo)"]
    pasarela["💳 Pasarela de pagos (externo)"]
    proveedor["🚚 sistema del proveedor (externo)"]
    vendedor --> webapp
    administrador --> webapp
    encargado --> webapp
    webapp --> api
    api --> |"cobra por el método de pago elegido"| pasarela
    api --> bd
    proveedor --> |"realiza la reposición"| api
    api -->|"publica evento stock-bajo"| avisos
    avisos --> correo
```
