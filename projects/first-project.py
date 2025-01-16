import os
import requests

API_URL = "https://api-inference.huggingface.co/models/deepset/roberta-base-squad2"
headers = {"Authorization": "Bearer hl_****"}

def query(payload):
    try:
        response = requests.post(API_URL, headers=headers, json=payload)
        response.raise_for_status()  # Lanza una excepción para códigos de error HTTP
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error al llamar a la API: {e}")
        return None

while True:
    question = input("Escribe tu pregunta (o 'salir' para terminar): ")
    if question.lower() == "salir":
        break
    context = input("Escribe el contexto (o 'salir' para terminar):: ")
    if context.lower() == "salir":
        break
    output = query({"inputs": {"question": question, "context": context}})
    if output and 'answer' in output:
        print(f"Respuesta: {output['answer']}")
    else:
        print("No se encontró una respuesta adecuada.")