import os
import random 
from datos import datos, citas_db
from modelo import crear_y_entrenar_modelo, obtener_prediccion

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# INICIALIZACIÓN

print("Entrenando al taoista...")
modelo_entrenado, tokenizer, encoder = crear_y_entrenar_modelo(datos)

# MODO INTERACTIVO
# -----------------------------------------------------------------
print("\n" + "="*60)
print("   El Agente Taoísta está listo.")
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
        print("\n Agente: Que el Tao ilumine tu camino. Adiós.")
        break
    
    if entrada_usuario.strip():
        # Obtenemos la predicción
        resultado = obtener_prediccion(entrada_usuario, modelo_entrenado, tokenizer, encoder, citas_db)

        if isinstance(resultado, list):
            cita_final = random.choice(resultado)
        else:

            cita_final = resultado
            
        print(f"\n Agente: {cita_final}\n")
    else:
        print(f"\n Agente: El silencio también es una respuesta.\n")