# =================================================================
# AGENTE TAOÍSTA - ARCHIVO PRINCIPAL (CORREGIDO)
# =================================================================
import os
import random  # <--- ¡IMPORTANTE! Necesario para elegir citas al azar
from datos import datos, citas_db
from modelo import crear_y_entrenar_modelo, obtener_prediccion

# Silenciar advertencias de TensorFlow
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# 1. INICIALIZACIÓN
# -----------------------------------------------------------------
print("🧠 Entrenando al agente... (esto puede tardar unos segundos)")
modelo_entrenado, tokenizer, encoder = crear_y_entrenar_modelo(datos)

# 2. MODO INTERACTIVO
# -----------------------------------------------------------------
print("\n" + "="*60)
print("🧘 El Agente Taoísta está listo.")
print("   Cuéntale tus penas, tus dudas o tu ira.")
print("   Escribe 'salir' para terminar.")
print("="*60 + "\n")

while True:
    try:
        entrada_usuario = input(">> Tú: ")
    except EOFError:
        break

    # Salida del programa
    if entrada_usuario.lower() in ['salir', 'exit', 'bye', 'adios']:
        print("\n📜 Agente: Que el Tao ilumine tu camino. Adiós.")
        break
    
    if entrada_usuario.strip():
        # Obtenemos la predicción (que ahora puede ser una LISTA de frases)
        resultado = obtener_prediccion(entrada_usuario, modelo_entrenado, tokenizer, encoder, citas_db)
        
        # --- CAMBIO CLAVE AQUÍ ---
        # Si recibimos una lista, elegimos una frase al azar.
        if isinstance(resultado, list):
            cita_final = random.choice(resultado)
        else:
            # Si por alguna razón es solo texto, lo usamos directo
            cita_final = resultado
            
        print(f"\n📜 Agente: {cita_final}\n")
    else:
        print(f"\n📜 Agente: El silencio también es una respuesta.\n")