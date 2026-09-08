
| Principio  | Clase y metodo | ¿Porque es una violacion? |
| ------------- | ------------- | ------------- |
| S  | gestorDePedidos.ProcesarPedido()  | El metdodo hace varias cosas, calcular descuentos, guardar en la base de datos y enviar correos  |
| O  | gestorDePedidos.ProcesarPedido() switch(tipoCliente)  | Para agregar un nuevo tipo de cliente hay que modificar el switch  |
| L/I  | IEmpleadoDeFarmacia — métodos que implementa Cajero  | La interfaz obliga al cajero a implementar funciones que no necesita, como ajustar precios o autorizar medicamentos controlados |
| D  | GestorDePedidos.ProcesarPedido() — new BaseDeDatosMySql() y new CorreoSmtp() | Crea directamente BaseDeDatosMySql y CorreoSmtp, quedando acoplado a esas clases |
