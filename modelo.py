import numpy as np
import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense
from keras_preprocessing.text import Tokenizer
from sklearn.preprocessing import LabelBinarizer

def crear_y_entrenar_modelo(datos):
    """
    Esta función se encarga de todo el proceso de la red neuronal:
    1. Preprocesa los datos de texto.
    2. Construye la arquitectura del modelo.
    3. Entrena el modelo con los datos.
    4. Devuelve el modelo entrenado y los preprocesadores (tokenizer y encoder).
    """
    
    # 1. PREPROCESAMIENTO
    print("Preprocesando datos...")
    # Separamos frases y etiquetas del conjunto de datos
    frases = [d[0] for d in datos]
    etiquetas = [d[1] for d in datos]

    # El Tokenizer convierte las palabras en números para que la red los entienda.
    tokenizer = Tokenizer(num_words=100) 
    tokenizer.fit_on_texts(frases)
    X_train = tokenizer.texts_to_matrix(frases, mode='binary') # Usamos "Bag of Words"

    # El LabelBinarizer convierte las etiquetas de texto (ej: "tristeza") a un formato numérico
    # que el modelo pueda usar como objetivo (ej: [0, 0, 1, 0]).
    encoder = LabelBinarizer()
    y_train = encoder.fit_transform(etiquetas)

    # 2. CREACIÓN DEL MODELO NEURONAL
    print("Construyendo la red neuronal...")
    model = Sequential()

    # Capa oculta 1: representación emocional suave (-1 a 1)
    model.add(Dense(16, input_shape=(X_train.shape[1],), activation='tanh'))

    # Capa oculta 2: refinamiento y separación más clara
    model.add(Dense(8, activation='relu'))

    # Capa de salida: probabilidad por emoción
    model.add(Dense(y_train.shape[1], activation='softmax'))

    # Compilación
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])


    # 3. ENTRENAMIENTO
    print("🧠 Entrenando al agente taoísta...")
    # epochs=200 es el número de veces que la red "revisa" los datos para aprender.
    # verbose=0 para no imprimir el progreso de cada epoch y mantener limpia la salida.
    model.fit(X_train, y_train, epochs=200, verbose=0)
    print("✅ Entrenamiento completado.\n")
    
    # 🔍 Evaluación del modelo
    loss, acc = model.evaluate(X_train, y_train, verbose=0)
    print(f"📈 Accuracy del entrenamiento: {acc:.2f}")
    print(f"📉 Loss: {loss:.4f}\n")

    # Devolvemos todo lo necesario para hacer predicciones
    return model, tokenizer, encoder

def obtener_prediccion(texto_usuario, model, tokenizer, encoder, citas_db):
    """
    Usa el modelo entrenado para predecir la emoción en el texto del usuario
    y devuelve la cita correspondiente.
    """
    # Convertimos el texto del usuario al mismo formato numérico que los datos de entrenamiento.
    vector_texto = tokenizer.texts_to_matrix([texto_usuario], mode='binary')
    
    # La red neuronal predice las probabilidades de cada emoción.
    prediccion = model.predict(vector_texto, verbose=0)
    
    # Buscamos el índice de la emoción con la probabilidad más alta (ej: 0.8 de "tristeza").
    indice_ganador = np.argmax(prediccion)
    
    # Con el índice, obtenemos el nombre de la etiqueta (ej: "tristeza").
    etiqueta_ganadora = encoder.classes_[indice_ganador]
    
    # Usamos la etiqueta para buscar la cita correspondiente en nuestra base de datos.
    return citas_db[etiqueta_ganadora]
