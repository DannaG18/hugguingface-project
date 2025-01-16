import requests

class MultiModelApp:
    def __init__(self, models, token):
        self.models = models
        self.headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }
        self.current_model_index = None

    def query(self, payload, files=None):
        try:
            api_url = self.models[self.current_model_index]
            
            if files:
                headers = {"Authorization": self.headers["Authorization"]}
                response = requests.post(api_url, headers=headers, files=files)
            else:
                response = requests.post(api_url, headers=self.headers, json=payload)
            
            response.raise_for_status()
            
            if self.current_model_index == 1:
                return response.content
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error al llamar a la API del modelo {api_url}: {e}")
            if hasattr(e.response, 'text'):
                print(f"Detalles del error: {e.response.text}")
            return None

    def switch_model(self, index):
        if 0 <= index < len(self.models):
            self.current_model_index = index
            print(f"Modelo cambiado a: {self.models[self.current_model_index]}")
        else:
            print("Índice de modelo no válido.")

if __name__ == "__main__":
    models = [
        "https://api-inference.huggingface.co/models/deepset/roberta-base-squad2",
        "https://api-inference.huggingface.co/models/black-forest-labs/FLUX.1-dev",
        "https://api-inference.huggingface.co/models/meta-llama/Llama-3.2-11B-Vision-Instruct"

    ]
    token = "hf_****"
    app = MultiModelApp(models, token)

    print("Bienvenido a la aplicación multifuncional usando IA!\n")
    print("Los modelos disponibles son:")
    print("1. Respuestas a preguntas.")
    print("2. Generación de imágenes a partir de texto.")
    print("3. Generación de texto a partir de imágenes.")

    while app.current_model_index is None:
        try:
            selection = int(input("\nSelecciona el modelo con el que quieres empezar (1-3): ")) - 1
            app.switch_model(selection)
        except ValueError:
            print("Por favor, ingresa un número válido.")

    print("\nPuedes cambiar de modelo escribiendo 'cambiar' cuando se solicite el contexto.\n")

    while True:
        print("\nModelo actual: ", end="")
        if app.current_model_index == 0:
            print("Respuestas a preguntas")
            question = input("Escribe tu pregunta (o 'salir' para terminar): ")
            if question.lower() == "salir":
                break

            context = input("Escribe el contexto (o 'cambiar' para cambiar el modelo): ")
            if context.lower() == "salir":
                break
            elif context.lower() == "cambiar":
                while True:
                    try:
                        new_model = int(input("Selecciona el modelo con el que quieres continuar (1-3): ")) - 1
                        app.switch_model(new_model)
                        break
                    except ValueError:
                        print("Por favor, ingresa un número válido.")
                continue

            output = app.query({"inputs": {"question": question, "context": context}})
            if output and 'answer' in output:
                print(f"Respuesta: {output['answer']}")
            else:
                print("No se encontró una respuesta adecuada.")

        elif app.current_model_index == 1:
            print("Generación de imágenes")
            prompt = input("Describe la imagen que quieres generar (o 'salir' para terminar): ")
            if prompt.lower() == "salir":
                break
            elif prompt.lower() == "cambiar":
                while True:
                    try:
                        new_model = int(input("Selecciona el modelo con el que quieres continuar (1-3): ")) - 1
                        app.switch_model(new_model)
                        break
                    except ValueError:
                        print("Por favor, ingresa un número válido.")
                continue

            payload = {
                "inputs": prompt,
                "parameters": {
                    "num_inference_steps": 30,
                    "guidance_scale": 7.5,
                    "width": 512,
                    "height": 512
                }
            }
            
            output = app.query(payload)
            
            if output and isinstance(output, bytes):
                try:
                    image_filename = "generated_image.png"
                    with open(image_filename, "wb") as image_file:
                        image_file.write(output)
                    print(f"Imagen generada correctamente. Guardada como {image_filename}")
                    print("Abre la imagen en tu visor de imágenes para verla.")
                except Exception as e:
                    print(f"Error al guardar la imagen: {e}")
            else:
                print("No se pudo generar la imagen.")

        elif app.current_model_index == 2:
            print("Generación de descripciones de imágenes (Llama Vision Instruct)")
            image_path = input("Proporciona la ruta al archivo de imagen (o 'salir' para terminar): ")
            if image_path.lower() == "salir":
                break
            elif image_path.lower() == "cambiar":
                while True:
                    try:
                        new_model = int(input("Selecciona el modelo con el que quieres continuar (1-3): ")) - 1
                        app.switch_model(new_model)
                        break
                    except ValueError:
                        print("Por favor, ingresa un número válido.")
                continue

            try:
           
                with open(image_path, 'rb') as image_file:
                    files = {
                        "file": ("image.jpg", image_file, "image/jpeg")  # Ensure the correct MIME type
                    }
                    output = app.query(None, files=files)
                
                if output and 'text' in output:
                    print(f"Descripción de la imagen: {output['text']}")
                else:
                    print("No se pudo generar la descripción de la imagen.")
            
            except Exception as e:
                print(f"Error al procesar el archivo de imagen: {e}")
