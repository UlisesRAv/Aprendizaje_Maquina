import numpy as np
import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras_preprocessing.text import Tokenizer
from sklearn.preprocessing import LabelBinarizer
import unicodedata


# ================= NORMALIZACIÓN DE TEXTO =======================
def normalizar(texto):
    texto = texto.lower()
    texto = ''.join(
        c for c in unicodedata.normalize('NFD', texto)
        if unicodedata.category(c) != 'Mn'
    )
    return texto

def crear_y_entrenar_modelo(datos):
    """
    Entrena la red neuronal con los datos proporcionados.
    Ajustado para manejar un vocabulario más amplio.
    """
    
    # 1. PREPROCESAMIENTO
    print("Preprocesando datos...")
    frases = [normalizar(d[0]) for d in datos]
    etiquetas = [d[1] for d in datos]

    # --- AUMENTAR EL VOCABULARIO ---
    tokenizer = Tokenizer(num_words=2600, lower=True) 
    tokenizer.fit_on_texts(frases)
    
    # Convertimos las frases a vectores TF-IDF para capturar la importancia de cada palabra
    X_train = tokenizer.texts_to_matrix(frases, mode='tfidf')

    encoder = LabelBinarizer()
    y_train = encoder.fit_transform(etiquetas)

    # 2. CREACIÓN DEL MODELO
    print(f"Construyendo red neuronal (Vocabulario: {X_train.shape[1]} palabras, Categorías: {y_train.shape[1]})...")
    model = Sequential()

    model.add(Dense(32, input_shape=(X_train.shape[1],), activation='tanh'))
    
    # Dropout ayuda a que el modelo no "memorice" demasiado y generalice mejor
    model.add(Dropout(0.3)) 

    # Capa Oculta 2
    model.add(Dense(16, activation='relu'))

    # Capa de salida (softmax para probabilidad de múltiples clases)
    model.add(Dense(y_train.shape[1], activation='softmax'))

    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

    # 3. ENTRENAMIENTO
    print("Entrenando al agente taoísta con sabiduría expandida...")
    # Aumentamos epochs a 250 para asegurar que aprenda bien las diferencias sutiles
    model.fit(X_train, y_train, epochs=250, verbose=0)
    print("Entrenamiento completado.\n")
    
    loss, acc = model.evaluate(X_train, y_train, verbose=0)
    print(f"📈 Precisión (Accuracy): {acc*100:.2f}%")

    return model, tokenizer, encoder

def obtener_prediccion(texto_usuario, model, tokenizer, encoder, citas_db):
    """
    Predice la emoción y devuelve la cita correspondiente.
    """
    # Normalizar texto
    texto_usuario = normalizar(texto_usuario)

    # Convertir texto a vector numérico usando el tokenizer entrenado
    vector_texto = tokenizer.texts_to_matrix([texto_usuario], mode='tfidf')

    # Predicción (vector con probabilidades para TODAS las emociones)
    prediccion = model.predict(vector_texto, verbose=0)[0]

    # Índice de la emoción con mayor probabilidad
    indice_ganador = np.argmax(prediccion)

    # Nombre de la emoción predicha
    etiqueta_ganadora = encoder.classes_[indice_ganador]

    # Obtener cita correspondiente
    try:
        cita = citas_db[etiqueta_ganadora]
    except KeyError:
        cita = "El Tao es misterioso... no sé qué decirte sobre eso, pero respira."

    # Devolver: cita, emoción, probabilidades
    return cita, etiqueta_ganadora, prediccion