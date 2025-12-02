import pickle
from datos import datos
from modelo import crear_y_entrenar_modelo

print("Iniciando proceso de entrenamiento...")

# 1. Entrenamos el modelo con todos los datos
modelo, tokenizer, encoder = crear_y_entrenar_modelo(datos)

print("\n Guardando el conocimiento del sabio en el disco...")

# 2. Guardamos el MODELO (la red neuronal)
# Keras tiene su propio formato optimizado (.h5 o .keras)
modelo.save('cerebro_taoista.h5')
print("   -> Modelo guardado como 'cerebro_taoista.h5'")

# 3. Guardamos el TOKENIZER (el diccionario de palabras)
# Usamos pickle para guardar objetos de Python
with open('tokenizer.pkl', 'wb') as handle:
    pickle.dump(tokenizer, handle, protocol=pickle.HIGHEST_PROTOCOL)
print("   -> Tokenizer guardado como 'tokenizer.pkl'")

# 4. Guardamos el ENCODER (las etiquetas de emociones)
with open('encoder.pkl', 'wb') as handle:
    pickle.dump(encoder, handle, protocol=pickle.HIGHEST_PROTOCOL)
print("   -> Encoder guardado como 'encoder.pkl'")

print("\n ¡Listo! Ya puedes ejecutar la app web.")