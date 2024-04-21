[&#10066; Volver al índice](README.md)

# Riesgos identificados

## 1. Dependencias de terceros

En el proyecto hay un riesgo claro, que también estuvo presente el semestre pasado. Se trata de la dependencia de APIs externas para el funcionamiento crítico de la aplicación.

El riesgo principalmente se basa en el poco control que tenemos sobre el funcionamiento de las APIs debido a que estamos usando la versión gratuita de éstas. Estando limitados a una cuota de peticiones diarias y una cuota general. Además de estar sujetos a cambios en las políticas de uso de las APIs (lo más probable por parte de OpenAI) que restrinjan aún más el uso de las mismas.

En el caso de la API de **OpenAI**:

- **Descripción del riesgo**: Dependencia de la API de OpenAI para el funcionamiento crítico de la aplicación.
- **Objetivo afectado**: Filtrar la descripción del taller para la búsqueda de talleristas.
- **Impacto**: Alto, ya que afecta la principal funcionalidad de la aplicación que es la búsqueda de talleristas.
- **Probabilidad de ocurrencia**: No predecible.
- **Medidas de mitigación**: En caso de falla, no filtrar la descripción del taller y forzar la búsqueda (mitigando parte del problema, pero muy probablemente empeorando los resultados).
- **Estado del riesgo**: No activo.

Lo mismo aplica para la API de **Google Custom Search**, solo que en lugar de afectar el filtrado del prompt, afecta el retorno de resultados de la búsqueda. Y la medida de mitigación sería hacer web scraping directamente (que es lo que se hace en la vista de búsqueda de insumos).

El incorrecto funcionamiento de las APIs mencionadas afectan a la misma funcionalidad, que es la vista de búsqueda de talleristas.

## 2. Tecnología obsoleta

Aunque "obsoleta" no sea la palabra indicada para este caso, si va ligado al problema que tuvimos el semestre anterior, ya que el uso de **streamlit** fue limitante al momento de intentar realizar algunas de las historias de usuario que se habían propuesto.

En particular, queríamos hacer la simulación de un carrito de compras para que los organizadores pudieran estimar el costo que tendrían los insumos que necesitarían para la realización de un taller. El problema era que streamlit forzaba una reinicio estático de la página cada vez que se modificaba un input, lo que hacía imposible realizar un carrito de compras ya que se necesita ver cómo se va modificando el precio en tiempo real (dinámicamente) a medida que se escogen o eliminan productos.

- **Descripción del riesgo**: Tecnología que limita el desarrollo de historias de usuario.
- **Objetivo afectado**: Realización de un carrito de compras.
- **Impacto**: Bajo, ya que si bien es una funcionalidad, no fue un requerimiento explícito del cliente.
- **Probabilidad de ocurrencia**: Inevitable. (Se forzaba el uso de la librería)
- **Medidas de mitigación**: Este semestre nos deshicimos de streamlit ya que ya no es una librería que sí o sí tengamos que utilizar.
- **Estado del riesgo**: Mitigado.

## 3. Requisitos poco claros

Si bien este no es el caso en este semestre, sí ocurrió en el semestre anterior, ya que al principio no se entendía bien qué era lo que quería el cliente. También lo podríamos relacionar a otro riesgo (cambio en los requisitos), ya que al principio se hablaba de un "question answering system" lo que se podía interpretar como un chatbot que guiara al usuario mientras éste buscaba talleristas, cosa que no se aclaró hasta la corrección del hito de las historias de usuario del semestre anterior (lapso de tiempo en el que no podíamos avanzar en el proyecto).

- **Descripción del riesgo**: Requisitos poco claros.
- **Objetivo afectado**: Inicio del desarollo del proyecto.
- **Impacto**: Medio, ya que no sabíamos cómo avanzar ya que básicamente no sabíamos qué era lo que se pedía.
- **Probabilidad de ocurrencia**: Bajo.
- **Medidas de mitigación**: Esperar evaluación.
- **Estado del riesgo**: No activo.

## 4. Falta de comunicación con usuarios finales

Por último, si bien tenemos a los _stakeholders_ como uno de los Alphas más prioritarios, ese sería el caso si fuera un cliente real. La realidad es que solo estamos modelando un caso de juguete, lo que provoca que no exista comunicación real con la parte más importante importante de los _stakeholders_ que nosotros consideramos que serían los usuarios finales de la aplicación.

- **Descripción del riesgo**: Falta de comunicación con usuarios finales.
- **Objetivo afectado**: Diseño de la aplicación.
- **Impacto**: Medio, ya que aunque nuestro criterio personal no sea una mala base, nunca sabremos si realmente estamos cumpliendo con las expectativas de nuestros usuarios finales.
- **Probabilidad de ocurrencia**: Alto.
- **Medidas de mitigación**: Criterio personal, consultas con los demás stakeholders.
- **Estado del riesgo**: Activo.

[&leftarrow; Ir al anterior](4-alphas-prioritarios.md)

[Ir al siguiente &rightarrow;](6-material-adicional.md)
