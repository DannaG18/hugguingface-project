from transformers import pipeline

sentiment_model = pipeline("sentiment-analysis", model="nlptown/bert-base-multilingual-uncased-sentiment")

text = [
    "Este producto es excelente y me encanta.",
    "El servicio fue terrible y no lo recomiendo.",
    "Es una experiencia promedio, no está mal."
]

results = sentiment_model(text)

for idx, result in enumerate(results):
    print(f"Texto: {text[idx]}")
    print(f"Sentimiento: {result['label']} (Confianza: {result['score']:.2f})\n")
