import numpy as np
import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras_preprocessing.text import Tokenizer
from sklearn.preprocessing import LabelBinarizer

def crear_y_entrenar_modelo(datos):
    """
    Entrena la red neuronal con los datos proporcionados.
    Ajustado para manejar un vocabulario más amplio.
    """
    
    # 1. PREPROCESAMIENTO
    print("Preprocesando datos...")
    frases = [d[0] for d in datos]
    etiquetas = [d[1] for d in datos]

    # --- AJUSTE CLAVE: AUMENTAR EL VOCABULARIO ---
    # Antes tenías 100. Ahora lo subimos a 2000 para que entienda
    # palabras específicas como "agobio", "vacío", "chingada", etc.
    tokenizer = Tokenizer(num_words=2600, lower=True) 
    tokenizer.fit_on_texts(frases)
    
    # Matrix binaria (Bag of Words)
    X_train = tokenizer.texts_to_matrix(frases, mode='binary')

    encoder = LabelBinarizer()
    y_train = encoder.fit_transform(etiquetas)

    # 2. CREACIÓN DEL MODELO
    print(f"Construyendo red neuronal (Vocabulario: {X_train.shape[1]} palabras, Categorías: {y_train.shape[1]})...")
    model = Sequential()

    # Capa de entrada + Oculta 1
    # Aumentamos un poco las neuronas (de 16 a 32) para manejar la complejidad de las 25 emociones
    model.add(Dense(32, input_shape=(X_train.shape[1],), activation='relu'))
    
    # Dropout ayuda a que el modelo no "memorice" demasiado y generalice mejor
    model.add(Dropout(0.3)) 

    # Capa Oculta 2
    model.add(Dense(16, activation='relu'))

    # Capa de salida (softmax para probabilidad de múltiples clases)
    model.add(Dense(y_train.shape[1], activation='softmax'))

    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

    # 3. ENTRENAMIENTO
    print("🧠 Entrenando al agente taoísta con sabiduría expandida...")
    # Aumentamos epochs a 250 para asegurar que aprenda bien las diferencias sutiles
    model.fit(X_train, y_train, epochs=250, verbose=0)
    print("✅ Entrenamiento completado.\n")
    
    loss, acc = model.evaluate(X_train, y_train, verbose=0)
    print(f"📈 Precisión (Accuracy): {acc*100:.2f}%")

    return model, tokenizer, encoder

def obtener_prediccion(texto_usuario, model, tokenizer, encoder, citas_db):
    """
    Predice la emoción y devuelve la cita correspondiente.
    """
    # Convertir texto nuevo a números usando el MISMO tokenizer entrenado
    vector_texto = tokenizer.texts_to_matrix([texto_usuario], mode='binary')
    
    prediccion = model.predict(vector_texto, verbose=0)
    
    # Obtenemos el índice de la emoción más probable
    indice_ganador = np.argmax(prediccion)
    
    # Obtenemos la etiqueta de texto (ej: "euforia")
    etiqueta_ganadora = encoder.classes_[indice_ganador]
    
    # Confianza de la predicción (opcional, útil para depurar)
    confianza = prediccion[0][indice_ganador]
    
    # Si la confianza es muy baja (el modelo está adivinando), podríamos manejarlo
    # Pero por ahora, confiamos en el Tao.
    
    # Recuperamos la cita (o lista de citas) de la base de datos
    try:
        return citas_db[etiqueta_ganadora]
    except KeyError:
        return ["El Tao es misterioso... no sé qué decirte sobre eso, pero respira."]