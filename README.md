# API REST de Productos

## Características que la hacen una API REST:

- Utiliza el protocolo HTTP y sigue el modelo cliente-servidor.
- Comunicación stateless: Cada petición contiene toda la información necesaria.
- Recursos accesibles a través de URLs claras (por ejemplo, `/productos`).
- Operaciones basadas en métodos estándar HTTP (GET, POST, PUT, DELETE).
- Respuestas en formato JSON.

## Diferencias con la arquitectura de 3 capas anterior:

- Antes, las rutas eran  `/agregar` o `/listar`, ahora son endpoints REST (`/productos`).
- Las operaciones CRUD (crear, leer, actualizar, eliminar) se implemento bien.
- Mayor estandarización y claridad en las rutas para trabajar mejor con clientes frontend o aplicaciones móviles.
