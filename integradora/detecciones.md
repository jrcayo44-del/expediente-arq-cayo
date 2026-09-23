# Violacion1
-Me di cuenta de que el método ProcesarPedido está haciendo demasiado por sí solo: calcula precios, guarda en base de datos, imprime el vale y envía un correo.
# Violacion2
- El switch para calcular el precio según el tipo de menú me hizo ver que el sistema no está preparado para crecer.
# Violacion3
- Lo que más me llamó la atención fue el uso de new BaseDeDatosComedor() y new CorreoUniversitario() directamente dentro de la clase principal. Esto crea una dependencia rígida hacia implementaciones concretas.
