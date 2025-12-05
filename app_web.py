import streamlit as st
import random
import time
import pickle
import os
import base64
from keras.models import load_model
from datos import citas_db
from modelo import obtener_prediccion

# CONFIGURACIÓN DE LA PÁGINA
st.set_page_config(
    page_title="El Sensei del Tao", 
    page_icon="🐧", 
    layout="wide", 
    initial_sidebar_state="collapsed"
)

def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Intentamos cargar el GIF
try:
    img_base64 = get_img_as_base64("club_penguin.gif")
except:
    st.stop()

# --- ESTILOS CSS MEJORADOS (Zen & Layout) ---
st.markdown(f"""
<style>

@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@700&family=Architects+Daughter&family=Lora:ital@0;1&display=swap');

/* ====== FONDO GENERAL ====== */
.stApp {{
    background: linear-gradient(145deg, #0f0f0f, #1a1a1a);
    color: #E0E0E0;
}}

/* Animación zen */
@keyframes floatZen {{
    0% {{ transform: translateY(0px); }}
    50% {{ transform: translateY(-6px); }}
    100% {{ transform: translateY(0px); }}
}}

/* ====== TÍTULO ====== */
h1 {{
    font-family: 'Cinzel', serif;
    text-align: center;
    color: #9dd8b2;
    margin-bottom: 10px;
    letter-spacing: 2px;
    text-shadow: 0 0 15px #2E8B57;
}}

/* ====== CONTENEDOR DEL PINGÜINO ====== */
.penguin-frame {{
    position: relative;
    width: 100%;
    max-width: 520px;
    margin: auto;

    /* GLASSMORPHISM */
    background: rgba(255,255,255,0.05);
    backdrop-filter: blur(6px);
    border-radius: 20px;

    box-shadow: 0 10px 30px rgba(0,0,0,0.6),
                inset 0 0 30px rgba(255,255,255,0.03);

    padding-bottom: 6px;
    animation: floatZen 4s ease-in-out infinite;
}}

.penguin-image {{
    width: 100%;
    display: block;
    border-radius: 15px;
    mask-image: linear-gradient(to bottom, black 85%, transparent 100%);
    -webkit-mask-image: linear-gradient(to bottom, black 90%, transparent 100%);
}}

/* ====== BURBUJA ====== */
.bubble-text {{
    position: absolute;
    top: 17%;
    right: 8%;

    width: 32%;
    min-height: 23%;

    display: flex;
    align-items: center;
    justify-content: center;
    text-align: center;

    font-family: 'Architects Daughter', cursive;
    font-size: 1.15rem;
    font-weight: 600;
    line-height: 1.1;
    color: #000;

    /* Glow suave */
    text-shadow: 0 0 8px rgba(255,255,255,0.8);

    /* BURBUJA REAL GLASS SUAVE */
    background: rgba(255,255,255,0.35);
    backdrop-filter: blur(3px);
    border-radius: 50%;
    padding: 8px;
    box-shadow: 0 0 10px rgba(0,0,0,0.25);
}}

/* ====== PANEL DE INPUT ====== */
.input-panel {{
    background: rgba(255,255,255,0.05);
    padding: 30px;
    border-radius: 20px;
    border-left: 4px solid #8FBC8F;
    box-shadow: 0 0 25px rgba(0,0,0,0.4);
    backdrop-filter: blur(6px);
}}

.stTextInput > div > div > input {{
    background-color: #2C2C2C;
    color: white;
    border-radius: 10px;
    border: 1px solid #555;
    padding: 12px;
    font-family: 'Lora', serif;
    transition: 0.2s;
}}
.stTextInput > div > div > input:focus {{
    border-color: #8FBC8F;
    box-shadow: 0 0 12px #3CB371;
}}

/* ====== BOTÓN ====== */
.stButton > button {{
    background: linear-gradient(135deg, #2E8B57, #3CB371);
    padding: 12px 20px;
    border-radius: 10px;
    border: none;
    font-family: 'Cinzel', serif;
    color: white;
    transition: 0.3s;
}}
.stButton > button:hover {{
    transform: translateY(-2px) scale(1.03);
    box-shadow: 0 0 20px #3CB371;
}}

/* ====== TEXTO ZEN ====== */
.zen-text {{
    font-family: 'Lora', serif;
    font-style: italic;
    color: #bfbfbf;
    margin-bottom: 20px;
    font-size: 1.2rem;
    text-align: center;
}}

/* ====== RESPONSIVE ====== */
@media (max-width: 768px) {{
    .bubble-text {{
        font-size: 0.8rem;
        width: 38%;
        top: 12%;
        right: 4%;
    }}

    .penguin-frame {{
        max-width: 360px;
    }}
}}

</style>
""", unsafe_allow_html=True)




# CARGA DEL CEREBRO
@st.cache_resource
def cargar_cerebro():
    if not os.path.exists('cerebro_taoista.h5'): return None, None, None
    try:
        modelo = load_model('cerebro_taoista.h5')
        with open('tokenizer.pkl', 'rb') as f: tokenizer = pickle.load(f)
        with open('encoder.pkl', 'rb') as f: encoder = pickle.load(f)
        return modelo, tokenizer, encoder
    except: return None, None, None

modelo_entrenado, tokenizer, encoder = cargar_cerebro()

if modelo_entrenado is None:
    st.error("El Sensei duerme. Ejecuta `entrenar.py` primero.")
    st.stop()

# ESTADO
if "ultimo_mensaje" not in st.session_state:
    st.session_state.ultimo_mensaje = "El vacío no está vacío..." 

# TÍTULO 
st.markdown("<h1>⛩️ El Templo del Sensei ⛩️</h1>", unsafe_allow_html=True)
st.write("") # Espaciador

# LAYOUT DE 2 COLUMNAS
col1, col2 = st.columns([1.2, 1], gap="large")

with col1:
    # HTML del Pingüino con Marco Zen
    html_penguin = f"""
    <div class="penguin-frame">
        <img src="data:image/gif;base64,{img_base64}" class="penguin-image">
        <div class="bubble-text">
            {st.session_state.ultimo_mensaje}
        </div>
    </div>
    """
    st.markdown(html_penguin, unsafe_allow_html=True)

# CONFESIONARIO 
with col2:

    st.markdown("### ¿Qué pesa en tu mente hoy?")
    
    with st.form(key='chat_form', clear_on_submit=True):
        user_input = st.text_input(" ", placeholder="Escribe tu inquietud aquí...", label_visibility="collapsed")
        st.write("") 
        submit_button = st.form_submit_button(label='🍃 Liberar Pensamiento')

    if submit_button and user_input:
        # Lógica de predicción
        with st.spinner("El viento susurra la respuesta..."):
            time.sleep(1.2)
            try:
                resultado, emocion_detectada, probabilidades = obtener_prediccion(
                    user_input, modelo_entrenado, tokenizer, encoder, citas_db
                )

                if isinstance(resultado, list):
                    respuesta = random.choice(resultado)
                else:
                    respuesta = resultado

                st.session_state.ultimo_mensaje = respuesta
                st.session_state.emocion = emocion_detectada
                st.session_state.probabilidades = probabilidades

                st.rerun()

            except Exception as e:
                st.error("El silencio es la única respuesta hoy (Error).")
                st.exception(e) 

    # EMOCIÓN Y PORCENTAJE
    if "emocion" in st.session_state:
        st.markdown("---")
        st.write("### Resultado emocional detectado:")

        emocion = st.session_state.emocion
        probabilidades = st.session_state.probabilidades

        clases = list(encoder.classes_)

        # Probabilidad de la emoción ganadora
        indice = clases.index(emocion)
        prob_emocion = probabilidades[indice] * 100

        st.markdown(f"**Emoción predominante:** `{emocion}`")
        st.markdown(f"**Confianza del modelo:** `{prob_emocion:.2f}%`")

        # Mostrar tabla de todas las emociones
        st.write("### Porcentajes de todas las emociones:")
        for cls, prob in zip(clases, probabilidades):
            st.write(f"- **{cls}** → `{prob*100:.2f}%`")

    st.markdown('</div>', unsafe_allow_html=True)

# Footer sutil
st.markdown("<div style='text-align: center; color: #555; margin-top: 50px; font-size: 0.8rem;'>Sabiduría Taoísta v2.0</div>", unsafe_allow_html=True)