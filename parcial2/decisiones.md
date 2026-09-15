- Situacion 1 patrón Observer <br>
Estoy usando el patron Observer en la primera situación porque, cuando una membresía vence, varios módulos necesitan ser notificados automáticamente, como WhatsApp, vencidos, recepción y promociones. Observer me permite agregar nuevos interesados sin modificar constantemente el módulo de socios, ya que este solo emite el aviso y los observadores reaccionan. <br>
No estoy usando patrones como Strategy o Factory, porque no necesito cambiar un algoritmo ni crear distintos tipos de objetos, sino notificar a varios componentes cuando ocurre un mismo evento.<br>
- Situacion 2 patron Strategy <br>
En esta situacion estoy usando el patrón Strategy porque existen diferentes formas de calcular la tarifa según la franja: mañana, noche o fin de semana, cada cálculo puede estar separado en una estrategia diferente, evitando tener muchas condicionales (if/else) y permitiendome cambiar las reglas fácilmente cada temporada.<br>
No estoy usando Observer porque no es nesesario notificar a varios módulos, ni Factory porque el problema no es crear objetos, sino cambiar dinámicamente la forma de calcular el precio.<br>
- Situacion 3 patron Adapter <br>
Y en esta situacion estoy usando el patrón Adapter porque el SDK de la pasarela de pago utiliza una interfaz distinta a la de mi sistema de gimnasio,los métodos en inglés, montos en centavos y datos que el dominio no debería manejar directamente. El Adapter me permite traducir esa comunicación y mantener el sistema independiente del proveedor externo. <br>
Tambien no estoy usando Strategy porque no estoy cambiando un algoritmo de pago, ni tampoco Observer porque no necesito notificar eventos, sino necesito adaptar una interfaz externa a la interfaz de mi sistema de gimnasio.
