[&#10066; Volver al índice](README.md)

# Riesgos identificados

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

[&leftarrow; Ir al anterior](4-alphas-prioritarios.md)

[Ir al siguiente &rightarrow;](6-material-adicional.md)
