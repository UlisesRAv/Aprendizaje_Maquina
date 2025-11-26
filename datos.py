# =================================================================
# BASE DE CONOCIMIENTO DEL AGENTE TAOISTA
# =================================================================

# 1. DATOS DE ENTRENAMIENTO
# -----------------------------------------------------------------
# Agrega más ejemplos aquí para que el modelo aprenda mejor.
# Cada ejemplo es una tupla: ("frase del usuario", "emocion_correspondiente")
# La "emocion_correspondiente" debe ser una de las claves del diccionario `citas_db`.
# -----------------------------------------------------------------
datos = [
    ("Me siento muy triste y sin esperanza", "tristeza"),
    ("Siento que nada tiene sentido, estoy vacío", "tristeza"),
    ("Tengo mucha ansiedad y miedo por el futuro", "ansiedad"),
    ("Estoy inquieto, no puedo dejar de pensar", "ansiedad"),
    ("Estoy en paz, todo fluye bien", "calma"),
    ("Me siento agradecido con la vida", "calma"),
    ("Tengo mucha ira, estoy enojado con todos", "ira"),
    ("Odio que las cosas no salgan como quiero", "ira")
]


# 2. LAS CITAS (Tu base de datos de sabiduría)
# -----------------------------------------------------------------
# ¡AQUÍ ES DONDE PUEDES AGREGAR MUCHÍSIMAS RESPUESTAS!
#
# Cada clave (ej: "tristeza") representa una categoría de emoción.
# El valor es la cita o respuesta que el agente dará.
#
# Para añadir más, simplemente agrega una nueva línea como:
# "nombre_de_emocion": "La cita que quieres mostrar."
#
# También puedes tener varias citas para una misma emoción. Para eso,
# cambia el valor por una lista de frases. Ejemplo:
# "tristeza": [
#     "“El camino que puede ser nombrado no es el camino eterno.” — Tao Te Ching",
#     "“El que está satisfecho con su parte es rico.” — Laozi"
# ]
# (Si haces esto, necesitarás un pequeño ajuste en `main.py` para elegir una cita al azar de la lista).
# -----------------------------------------------------------------
citas_db = {
    "tristeza": "“El camino que puede ser nombrado no es el camino eterno.” — Tao Te Ching",
    "ansiedad": "“El hombre perfecto usa su mente como un espejo: no agarra nada, no rechaza nada.” — Zhuangzi",
    "calma": "“Si estás deprimido, vives en el pasado. Si estás ansioso, vives en el futuro. Si estás en paz, vives en el presente.” — Laozi",
    "ira": "“El que domina a los otros es fuerte; el que se domina a sí mismo es poderoso.” — Tao Te Ching"
    # Agrega más categorías y citas aquí. Por ejemplo:
    # "confusion": "“Conocer a los demás es inteligencia; conocerse a sí mismo es la verdadera sabiduría.” — Tao Te Ching",
    # "miedo": "“No hay peligro que no puedas vencer si te enfrentas a él con valor.” — Laozi",
}
