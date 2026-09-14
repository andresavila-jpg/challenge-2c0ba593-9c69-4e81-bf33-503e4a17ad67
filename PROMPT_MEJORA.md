# Prompt para Mejorar el Codigo Base

Copia y pega el siguiente contenido completo en un asistente de IA (Claude, ChatGPT, etc.)
para obtener un ZIP con el proyecto arrancable. Si el adjunto es una carcasa (docs/placeholders),
el asistente debe materializar la estructura del stack del briefing, sin resolver las fases del reto.

---

```
## Briefing del reto (autoridad)
Este bloque manda sobre los archivos adjuntos. El stack y el rol salen de AQUÍ, no de un topic genérico ni de markdown placeholder.

### Perfil
Chapter Ciencia de Datos, Especialidad Ingeniero de Datos, Seniority Advanced

### Brecha de conocimiento
Manipula diferentes estructuras de datos para la solucion de los retos técnicos (Array, Matriz, Diccionario, DataFrame, Listas)

### Misión / candidato
Candidato con nivel advanced, trabajando en proyectos de ingeniería de datos

### Reto
- Tema: Fundamentos de estructura de datos
- Seniority: advanced-l2
- Tipo: practical
- Título: Desarrollo de un sistema de gestión de datos con estructuras de datos
- Tiempo estimado: 4-5 horas

### Fases (trabajo del HUMANO — PROHIBIDO completarlas)
No implementes estos entregables. Dejalos como hueco pedagógico. El asistente solo materializa el proyecto arrancable para que el participante pueda trabajar.
- Fase 1: Implementación de estructuras de datos básicas — objetivo: Implementar arrays y listas para almacenar información de clientes. — entregable (NO resolver): Estructuras de datos básicas (array y lista) funcionando para almacenar y buscar información de clientes.
- Fase 2: Implementación de diccionarios y matrices — objetivo: Implementar diccionarios y matrices para almacenar información más compleja de los clientes. — entregable (NO resolver): Estructuras de datos avanzadas (diccionario y matriz) funcionando para almacenar y recuperar información compleja de clientes.
- Fase 3: Implementación de DataFrames — objetivo: Implementar DataFrames para analizar y manipular grandes volúmenes de datos. — entregable (NO resolver): DataFrame funcionando para almacenar, analizar y manipular grandes volúmenes de datos de clientes.

Eres un asistente experto en análisis, corrección y generación de archivos de cualquier tipo:
código fuente, documentación, hojas de cálculo, documentos Word, configuraciones, entre otros.
Voy a enviarte una cadena de texto que contiene uno o más archivos. Cada archivo está delimitado por un marcador con el siguiente formato:
// === ARCHIVO: ruta/del/archivo.extension ===
o también puede aparecer como:
## === ARCHIVO: ruta/del/archivo.extension ===
Lo que sigue al marcador puede ser:

El contenido real del archivo (código, texto, YAML, etc.)
Una descripción en lenguaje natural de lo que debe contener el archivo


TU TAREA
PASO 1 — Detección y extracción
Identifica todos los archivos presentes en la cadena. Para cada archivo extrae:

Su ruta completa (ej: src/main/java/com/pragma/Service.java)
Su contenido o descripción

PASO 2 — Clasificación por tipo
Clasifica cada archivo en una de estas categorías:
A) Código fuente (Java, Python, TypeScript, JavaScript, Kotlin, etc.)
B) Configuración / documentación (YAML, properties, Markdown, JSON, txt, etc.)
C) Excel (.xlsx, .xls, .csv)
D) Word (.docx, .doc)
E) Otro tipo de archivo binario o especial
PASO 3 — Clasificación de errores en código fuente

Objetivo prioritario: que el proyecto compile. No corrijas flujo de negocio ni lógica funcional.

Antes de modificar cualquier archivo de código fuente, clasifica cada problema encontrado en una de estas dos categorías:
🔴 ERROR DE COMPILACIÓN — corregir siempre
Son errores que impiden que el proyecto arranque, sin valor pedagógico:

Import faltante o incorrecto
Clase, método o variable referenciada que no existe en ningún archivo del proyecto
Error de sintaxis
Anotación con atributos inválidos
Dependencia ausente en pom.xml, package.json, etc.
Archivo referenciado que no existe y debe ser creado con implementación mínima

→ CORREGIR estos errores.
🟡 PROBLEMA FUNCIONAL O DE CALIDAD — preservar siempre
Son problemas que no impiden compilar. Pueden ser intencionales para el aprendizaje:

Clave secreta hardcodeada ("secret", "password123")
API deprecada que funciona pero tiene reemplazo moderno
Lógica de negocio incorrecta o incompleta
Código redundante o de baja legibilidad
Falta de validaciones en flujo de negocio
Patrones de diseño incorrectos pero funcionales
Concurrencia no segura
Configuración funcional pero no óptima

→ PRESERVAR tal cual. No corregir, no mejorar, no comentar.
PASO 4 — Procesamiento según tipo de archivo
Tipo A — Código fuente
Aplica únicamente las correcciones clasificadas como 🔴 ERROR DE COMPILACIÓN.
No alteres ningún elemento clasificado como 🟡 PROBLEMA FUNCIONAL O DE CALIDAD.
Si falta un archivo referenciado, créalo con la implementación mínima necesaria para compilar.
Tipo B — Configuración / documentación
Extrae el contenido tal cual, sin modificaciones salvo errores evidentes de sintaxis
(ej: YAML mal indentado).
Tipo C — Excel (.xlsx)
Si viene con contenido real, genera el archivo respetando ese contenido.
Si viene con descripción en lenguaje natural, genera un archivo Excel funcional con:

Fila de encabezados en negrita con color de fondo distintivo
Columnas con ancho ajustado al contenido
Tipos de dato correctos por columna
Validaciones si la descripción lo indica
Hojas nombradas descriptivamente si hay más de una
Filas de ejemplo si no hay datos reales

Tipo D — Word (.docx)
Si viene con contenido real, genera el archivo respetando ese contenido.
Si viene con descripción en lenguaje natural, genera un documento Word funcional con:

Estilos de título (Título 1, Título 2) para jerarquía de secciones
Fuente legible (Calibri o equivalente), tamaño 11-12pt para cuerpo
Márgenes estándar
Tabla de contenido si tiene múltiples secciones
Tablas con encabezados en negrita si aplica

Tipo E — Otro
Genera el archivo con el contenido o estructura más apropiada según la descripción.
PASO 5 — Exportación en ZIP
Empaqueta todos los archivos en un único archivo ZIP descargable respetando exactamente
la estructura de rutas indicada por los marcadores.
El ZIP debe incluir:

Archivos de código con únicamente los errores de compilación corregidos
Archivos de configuración y documentación sin cambios
Archivos nuevos creados para resolver dependencias de compilación faltantes
Archivos Excel y Word generados desde descripción

IMPORTANTE: El ZIP debe estar listo para descargar al finalizar. No preguntes si el usuario
quiere generarlo. Simplemente genera el archivo y proporciona el enlace de descarga; No debes desplegar en el chat el resumen de lo que arreglaste al Zip, solo entregalo.

REGLAS IMPORTANTES

No omitas ningún archivo aunque no tenga errores ni modificaciones
Respeta los nombres y rutas exactas indicadas por los marcadores
Si un archivo no tiene marcador claro, infiere el nombre desde su contenido
Si la cadena contiene solo documentación o descripciones sin código, genera los archivos
correspondientes sin aplicar análisis de compilación
No agregues texto después del enlace de descarga del ZIP
No preguntes si el usuario quiere el ZIP: simplemente generalo siempre
Si detectas que falta un archivo de configuración necesario para compilar
(pom.xml, package.json, requirements.txt, build.gradle, etc.), créalo e inclúyelo
inferiendo su contenido desde los imports y frameworks detectados en el código
Nunca corrijas problemas 🟡 aunque parezcan obvios o fáciles de mejorar.
El participante que recibirá este proyecto los debe encontrar y resolver él mismo.


INPUT
Aquí está la cadena con los archivos:

import pandas as pd
from typing import List, Dict

# === ARCHIVO: data/clients_basic.csv ===
name,age,city
Alice,30,New York
Bob,25,Los Angeles
Charlie,35,Chicago

# === ARCHIVO: data/clients_complex.csv ===
name,purchases,transactions
Alice,[100, 200],[500, 600]
Bob,[150],[]
Charlie,[250, 300],[700]

# === ARCHIVO: src/data_structures.py ===
class Client:
    def __init__(self, name: str, age: int, city: str):
        self.name = name
        self.age = age
        self.city = city

class ClientArray:
    def __init__(self):
        self.clients = []

    def add_client(self, client: Client):
        self.clients.append(client)

    def find_client_by_name(self, name: str) -> Client:
        for client in self.clients:
            if client.name == name:
                return client
        raise ValueError('Client not found')

class ClientList:
    def __init__(self):
        self.clients = []

    def add_client(self, client: Client):
        self.clients.append(client)

    def find_client_by_name(self, name: str) -> Client:
        for client in self.clients:
            if client.name == name:
                return client
        raise ValueError('Client not found')

# === ARCHIVO: src/advanced_data_structures.py ===
class ClientDict:
    def __init__(self):
        self.clients = {}

    def add_client(self, client: Client):
        self.clients[client.name] = client

    def find_client_by_name(self, name: str) -> Client:
        if name in self.clients:
            return self.clients[name]
        raise ValueError('Client not found')

    def add_purchase(self, name: str, purchase: int):
        if name in self.clients:
            self.clients[name].purchases.append(purchase)
        else:
            raise ValueError('Client not found')

    def get_total_purchases(self, name: str) -> int:
        if name in self.clients:
            return sum(self.clients[name].purchases)
        raise ValueError('Client not found')

class ClientMatrix:
    def __init__(self):
        self.clients = {}

    def add_client(self, client: Client):
        self.clients[client.name] = client

    def find_client_by_name(self, name: str) -> Client:
        if name in self.clients:
            return self.clients[name]
        raise ValueError('Client not found')

    def add_transaction(self, name: str, transaction: int):
        if name in self.clients:
            self.clients[name].transactions.append(transaction)
        else:
            raise ValueError('Client not found')

    def get_total_transactions(self, name: str) -> int:
        if name in self.clients:
            return sum(self.clients[name].transactions)
        raise ValueError('Client not found')

# === ARCHIVO: src/dataframes.py ===
def load_dataframe(file_path: str) -> pd.DataFrame:
    return pd.read_csv(file_path)

def calculate_average_purchases(df: pd.DataFrame) -> float:
    return df['purchases'].mean()

def filter_dataframe(df: pd.DataFrame, column: str, value) -> pd.DataFrame:
    return df[df[column] == value]

def sort_dataframe(df: pd.DataFrame, column: str) -> pd.DataFrame:
    return df.sort_values(by=column)

# === ARCHIVO: tests/test_data_structures.py ===
import unittest
from src.data_structures import Client, ClientArray, ClientList

class TestDataStructures(unittest.TestCase):
    def test_client_array(self):
        array = ClientArray()
        client = Client('Alice', 30, 'New York')
        array.add_client(client)
        self.assertEqual(array.find_client_by_name('Alice').name, 'Alice')

    def test_client_list(self):
        list = ClientList()
        client = Client('Bob', 25, 'Los Angeles')
        list.add_client(client)
        self.assertEqual(list.find_client_by_name('Bob').name, 'Bob')

if __name__ == '__main__':
    unittest.main()

# === ARCHIVO: tests/test_advanced_data_structures.py ===
import unittest
from src.advanced_data_structures import ClientDict, ClientMatrix

class TestAdvancedDataStructures(unittest.TestCase):
    def test_client_dict(self):
        dict = ClientDict()
        client = Client('Charlie', 35, 'Chicago')
        dict.add_client(client)
        dict.add_purchase('Charlie', 250)
        self.assertEqual(dict.get_total_purchases('Charlie'), 250)

    def test_client_matrix(self):
        matrix = ClientMatrix()
        client = Client('Alice', 30, 'New York')
        matrix.add_client(client)
        matrix.add_transaction('Alice', 500)
        self.assertEqual(matrix.get_total_transactions('Alice'), 500)

if __name__ == '__main__':
    unittest.main()

# === ARCHIVO: tests/test_dataframes.py ===
import unittest
from src.dataframes import load_dataframe, calculate_average_purchases, filter_dataframe, sort_dataframe
import pandas as pd

class TestDataFrames(unittest.TestCase):
    def test_load_dataframe(self):
        df = load_dataframe('data/clients_complex.csv')
        self.assertIsInstance(df, pd.DataFrame)

    def test_calculate_average_purchases(self):
        df = load_dataframe('data/clients_complex.csv')
        average = calculate_average_purchases(df)
        self.assertAlmostEqual(average, 200.0)

    def test_filter_dataframe(self):
        df = load_dataframe('data/clients_complex.csv')
        filtered = filter_dataframe(df, 'name', 'Alice')
        self.assertEqual(filtered.shape[0], 1)

    def test_sort_dataframe(self):
        df = load_dataframe('data/clients_complex.csv')
        sorted_df = sort_dataframe(df, 'name')
        self.assertEqual(sorted_df.iloc[0].name, 'Alice')

if __name__ == '__main__':
    unittest.main()
```
