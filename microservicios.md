¿Qué diferencias hay entre REST y microservicios?

REST es una forma de comunicar partes de una aplicación usando HTTP.

Una API REST puede vivir dentro de una sola aplicación grande (monolítica).

Los microservicios son aplicaciones pequeñas e independientes, cada una con su propia API.

¿Qué desafíos tendríamos al pasar de REST a microservicios?

Hay que separar bien las funcionalidades en diferentes servicios (productos, usuarios, pagos, etc.).

Cada servicio debe hablar con los demás, lo que añade complejidad en la comunicación.

Necesitamos herramientas para desplegar y encontrar servicios (orquestación y descubrimiento).

Hay que manejar errores y seguridad entre servicios.

¿Qué ventajas tienen los microservicios frente a una API REST monolítica?

Puedes escalar solo el servicio que más lo necesite.

Actualizar un servicio no afecta al resto.

Cada servicio puede usar la tecnología o base de datos que mejor convenga.

Si un servicio falla, los demás pueden seguir funcionando.
