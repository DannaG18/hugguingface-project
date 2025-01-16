# Hugging Face Project

Este proyecto implementa modelos de aprendizaje automático de Hugging Face. Incluye pipelines avanzados para tareas como generación de imágenes, procesamiento de texto y modelos combinados.

## Tabla de Contenidos

- [Descripción](#descripción)
- [Características Principales](#características-principales)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Modelos Usados](#modelos-usados)
- [Requisitos](#requisitos)
- [Instalación](#instalación)
- [Ejecución](#ejecución)
- [Contribuciones](#contribuciones)

---

## Descripción

Este proyecto utiliza múltiples pipelines de Hugging Face para la manipulación y generación de contenido visual y textual. Su propósito es facilitar tareas como imagen-a-imagen (img2img), control de contenido y otras operaciones avanzadas.

## Características Principales

- Soporte para múltiples pipelines avanzados, incluyendo:

  - Generación de respuestas.
  - Texto a imagen.
  - Imagen a texto.
  - Control de modelos.

- Utiliza modelos preentrenados de Hugging Face.

  

## Estructura del Proyecto

```
.
├── .venv/                 # Entorno virtual configurado.
├── media                # Carpeta contenido multimedia.
|   ├── generated_image.png # Imagen generada con modelo texto a imagen.
	├── Lavanda Wallpaper.jpg # Imagen de ejemplo para modelo imagen a texto.
├── models/                # Archivos relacionados con los modelos preentrenados.
	├── first_project.py # Modelo de respuestas.
	├── model_execution.py # Prueba básica de modelo de sentimientos.
	├── second_project.py # Implementacion de múltiples modelos
└── README.md # Documentación del proyecto.
```

## Modelos Usados

Los modelos utilizados provienen de la biblioteca `diffusers` y están optimizados para tareas específicas:

1. **nlptown/bert-base-multilingual-uncased-sentiment**:
   - Modelo: https://huggingface.co/nlptown/bert-base-multilingual-uncased-sentiment.
   - Tareas: Detecta el grado de confianza de el sujeto respecto a algo.

2. **deepset/roberta-base-squad2**:
   - Model: https://huggingface.co/deepset/roberta-base-squad2.
   - Tareas: Genera respuestas a partir de preguntas.

3. **black-forest-labs/FLUX.1-dev**:
   - Model: https://huggingface.co/black-forest-labs/FLUX.1-dev.
   - Tareas: Genera imágenes a partir de descripciones.

4. **meta-llama/Llama-3.2-11B-Vision-Instruct**:
   - Model: https://huggingface.co/meta-llama/Llama-3.2-11B-Vision-Instruct.
   - Tareas: A partir de imágenes genera texto.

## Requisitos

- Python 3.10 o superior.
- Bibliotecas principales:
  - `torch`
  - `transformers`
- GPU recomendada para mejorar el rendimiento.

## Instalación

1. Clona el repositorio:

   ```bash
   git clone <repositorio-url>
   cd <nombre-del-proyecto>
   ```

2. Crea un entorno virtual:

   ```bash
   python -m venv .venv
   source .venv/bin/activate # Para Linux/Mac
   .venv\Scripts\activate   # Para Windows
   ```

## Ejecución

1. Descarga las bibliotecas principales.

2. Haz la ejecución del modelo de sentimientos.

   ```bash
   python projects/model-execution.py
   ```

3. Ejecuta el proyecto 1:

   ```bash
   python projects/first-project.py
   ```

4. Ejecuta el proyecto 2:

   ```bash
   python projects/second-project.py
   ```

## Contribuciones

Las contribuciones son bienvenidas. Si tienes alguna idea o encuentras un problema, por favor abre un issue o envía un pull request.