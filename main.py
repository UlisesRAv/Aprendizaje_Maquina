# =================================================================
# AGENTE TAOÍSTA - ARCHIVO PRINCIPAL
# =================================================================
# Este es el único archivo que necesitas ejecutar para iniciar el programa.

# 1. IMPORTACIONES
# -----------------------------------------------------------------
# Importamos las variables y funciones de nuestros módulos.
# `datos` y `citas_db` vienen de datos.py
# `crear_y_entrenar_modelo` y `obtener_prediccion` vienen de modelo.py
import os
from datos import datos, citas_db
from modelo import crear_y_entrenar_modelo, obtener_prediccion

# Silenciar advertencias de TensorFlow que pueden ser muy ruidosas
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# 2. INICIALIZACIÓN Y ENTRENAMIENTO
# -----------------------------------------------------------------
# Al iniciar, creamos y entrenamos el modelo con los datos de `datos.py`.
# Este proceso solo ocurre una vez, al arrancar el script.
modelo_entrenado, tokenizer, encoder = crear_y_entrenar_modelo(datos)

# 3. MODO INTERACTIVO
# -----------------------------------------------------------------
# Un bucle infinito para que puedas conversar con el agente.
# El programa se quedará aquí esperando tus mensajes.
print("🧘 El agente taoísta está listo. Escribe cómo te sientes o 'salir' para terminar.")
print("-" * 70)

while True:
    # Pedimos al usuario que escriba algo.
    entrada_usuario = input(">> Tú: ")
    
    # Si el usuario escribe "salir", rompemos el bucle y el programa termina.
    if entrada_usuario.lower() == 'salir':
        print("\n📜 Agente: Que encuentres tu propio camino. Adiós.")
        break
    
    # Si no, pasamos el texto al modelo para que nos dé una respuesta.
    if entrada_usuario:
        # Obtenemos la cita usando nuestro modelo entrenado y los datos.
        cita_obtenida = obtener_prediccion(entrada_usuario, modelo_entrenado, tokenizer, encoder, citas_db)
        
        # Imprimimos la respuesta del agente.
        print(f"\n📜 Agente: {cita_obtenida}\n")
    else:
        print(f"\n📜 Agente: El silencio también es una respuesta.\n")
