# Desarrollo de un sistema de gestión de datos con estructuras de datos

El sistema de gestión de datos de una empresa fintech necesita ser optimizado para manejar grandes volúmenes de información de manera eficiente. El objetivo es implementar diferentes estructuras de datos para mejorar la velocidad y la eficiencia en la manipulación de datos. El sistema debe ser capaz de almacenar, recuperar y manipular datos de forma óptima.

## Informacion General

| Campo | Valor |
|-------|-------|
| **Tema** | Fundamentos de estructura de datos |
| **Nivel** | advanced-l2 |
| **Tipo** | practical |
| **Tiempo estimado** | 4-5 horas |

## Fases del Reto

### Fase 0: Configuración del Proyecto

**Objetivo:** Obtener el proyecto base funcional enviando el Código Base a un asistente de IA, que lo analizará, corregirá errores y generará un ZIP listo para usar.

**Tiempo estimado:** 15-30 minutos

**Instrucciones:**

- Asegúrate de tener instalado para ejecutar el proyecto: Un IDE o editor de código.
- Copia todo el contenido del campo **Código Base** de este reto — incluyendo el texto de instrucciones que aparece al inicio.
- Abre un asistente de IA (Claude en claude.ai, ChatGPT o Gemini — se recomienda Claude), pega el contenido copiado en el chat y envíalo.
- El asistente analizará los archivos, corregirá errores y generará un archivo ZIP descargable. Descárgalo y extráelo en la carpeta donde quieras trabajar.
- Verifica que el proyecto arranca sin errores.

**Entregable:** El proyecto compila/arranca sin errores.

<details>
<summary>Pistas de conocimiento</summary>

- Copia el Código Base completo incluyendo el texto de instrucciones al inicio — esas instrucciones le indican al asistente exactamente qué hacer con los archivos.
- Si el asistente no genera el ZIP automáticamente al terminar el análisis, escríbele: "genera el ZIP ahora".
- Si el proyecto tiene errores al arrancar, comparte el mensaje de error con el mismo asistente para que lo corrija.

</details>

### Fase 1: Implementación de estructuras de datos básicas

**Objetivo:** Implementar arrays y listas para almacenar información de clientes.

**Tiempo estimado:** 1 hora

**Instrucciones:**

- Define una estructura de datos para almacenar información básica de los clientes (nombre, edad, ciudad).
- Implementa la funcionalidad para añadir nuevos clientes a la estructura de datos.
- Implementa la funcionalidad para buscar un cliente por nombre.

**Entregable:** Estructuras de datos básicas (array y lista) funcionando para almacenar y buscar información de clientes.

<details>
<summary>Pistas de conocimiento</summary>

- Considera la eficiencia de búsqueda y la facilidad de inserción al elegir la estructura de datos.
- Piensa en cómo manejarías la duplicación de nombres.

</details>

### Fase 2: Implementación de diccionarios y matrices

**Objetivo:** Implementar diccionarios y matrices para almacenar información más compleja de los clientes.

**Tiempo estimado:** 1.5 horas

**Instrucciones:**

- Define una estructura de datos para almacenar información adicional de los clientes (compras realizadas, historial de transacciones).
- Implementa la funcionalidad para añadir y recuperar información de compras y transacciones utilizando diccionarios y matrices.
- Implementa la funcionalidad para calcular el total de compras de un cliente.

**Entregable:** Estructuras de datos avanzadas (diccionario y matriz) funcionando para almacenar y recuperar información compleja de clientes.

<details>
<summary>Pistas de conocimiento</summary>

- Considera la eficiencia en la recuperación de datos al elegir entre diccionarios y matrices.
- Piensa en cómo manejarías los edge cases, como clientes sin compras.

</details>

### Fase 3: Implementación de DataFrames

**Objetivo:** Implementar DataFrames para analizar y manipular grandes volúmenes de datos.

**Tiempo estimado:** 1.5 horas

**Instrucciones:**

- Define una estructura de datos para almacenar y analizar información de múltiples clientes (compras, transacciones, preferencias).
- Implementa la funcionalidad para cargar datos en un DataFrame y realizar análisis básicos (promedio de compras, clientes más activos).
- Implementa la funcionalidad para filtrar y ordenar datos en el DataFrame.

**Entregable:** DataFrame funcionando para almacenar, analizar y manipular grandes volúmenes de datos de clientes.

<details>
<summary>Pistas de conocimiento</summary>

- Considera la eficiencia y la capacidad de análisis al utilizar DataFrames.
- Piensa en cómo manejarías datos faltantes o inconsistentes en el DataFrame.

</details>

## Dimensiones Evaluadas

- **queEs**: ¿Qué es un DataFrame y para qué se utiliza en el análisis de datos?
- **comoSeUsa**: ¿Cómo implementaste la funcionalidad para cargar y analizar datos en el DataFrame?
- **erroresComunes**: ¿Qué edge cases consideraste al implementar las estructuras de datos y cómo los manejaste?

## Criterios de Evaluacion

- Implementación de arrays y listas para almacenar información básica de clientes.
- Implementación de diccionarios y matrices para almacenar información compleja de clientes.
- Implementación de DataFrames para analizar y manipular grandes volúmenes de datos de clientes.
- Manejo de edge cases y datos inconsistentes en las estructuras de datos implementadas.

## Como trabajar con un asistente de IA

- **AGENTS.md** — instrucciones nativas del repo (Cursor, Codex, Copilot, Gemini, Claude Code). Abrí el proyecto y el agente las carga solo.
- **PROMPT_MEJORA.md** — el mismo prompt, para copiar y pegar en un chat (claude.ai, ChatGPT, etc.).

---

*Reto generado automaticamente por Challenge Generator - Pragma*
