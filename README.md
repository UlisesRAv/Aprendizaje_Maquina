☯️ El Sensei del Tao - Agente de IA

Bienvenido al proyecto del Agente Taoísta. Este es un sistema de inteligencia artificial que detecta tus emociones (miedo, ansiedad, euforia, etc.) y responde con sabiduría ancestral para devolverte al equilibrio.

📋 Requisitos Previos

Tener Python instalado en tu computadora.

Tener el archivo de imagen club_penguin.gif en la misma carpeta que los scripts (es la cara del Sensei).

🛠️ Paso 1: Instalación

Abre tu terminal (consola) en la carpeta del proyecto e instala las librerías necesarias copiando y pegando este comando:

pip install tensorflow scikit-learn streamlit keras


(Nota: Si usas Mac/Linux, quizás necesites escribir pip3 en lugar de pip).

🧠 Paso 2: Entrenar al Cerebro (Solo una vez)

Antes de usar la web, necesitas que el agente "estudie" los datos y cree su cerebro.

En la terminal, ejecuta:

python entrenar.py


Espera unos segundos. Verás mensajes de que está "Preprocesando datos" y "Entrenando".

Al finalizar, verás que aparecieron 3 archivos nuevos en tu carpeta:

cerebro_taoista.h5 (El modelo neuronal)

tokenizer.pkl (El diccionario de palabras)

encoder.pkl (El traductor de emociones)

¡Listo! El sabio ya aprendió. No necesitas volver a correr este paso a menos que modifiques el archivo datos.py.

⛩️ Paso 3: Ejecutar el Templo (La Web App)

Ahora sí, vamos a abrir la interfaz bonita con el Pingüino Sensei.

En la terminal, ejecuta:

streamlit run app_web.py


Automáticamente se abrirá una pestaña en tu navegador con la aplicación funcionando.

📂 Estructura de Archivos

datos.py: La "biblioteca" del sabio. Contiene todas las frases de entrenamiento y las citas de respuesta.

modelo.py: El "motor". Contiene la lógica de Inteligencia Artificial.

entrenar.py: El "maestro". Script que entrena al modelo y lo guarda para que sea rápido.

app_web.py: La "fachada". El código de la interfaz visual con Streamlit.

club_penguin.gif: La imagen del Sensei.

"El viaje de mil millas comienza con un simple streamlit run." — Laozi (Adaptación moderna)