# Loadtests

Este directorio contiene las pruebas de carga para la aplicación. Las pruebas de carga se utilizan para probar la aplicación bajo una carga pesada para ver cómo se comporta.

- `response-time-150-users.webp` es una captura de pantalla de la aplicación bajo una carga de 150 usuarios. La respuesta de la aplicación es de 90 milisegundos casi al final cuando los usuarios están en su punto máximo. No falla y está dentro del rango razonable de respuesta.
- `response-time-300-users.webp` es una captura de pantalla de la aplicación bajo una carga de 300 usuarios. Funciona correctamente durante 13 segundos, luego comienza a fallar. El tiempo de respuesta de la aplicación se encuentra dentro del rango esperado, sin embargo, no todas las respuestas son satisfactorias (algunas fallan con error 500).
