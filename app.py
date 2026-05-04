import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
st.set_page_config(page_title="copyboost AI",)

st.title("CopyBoost AI")
st.subheader("Generador de descripciones de productos con ia")

st.write("Ingresa tu producto y obtené una descripción lista para vender")

producto = st.text_input("Nombre o descripción del producto")

if st.button("Generar descripcion"):
    if producto:
        try:
            client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

            prompt = F"""
Actua como un experto en marketing digital y copywriting para ecommerce.

Tu tarea es generar una descripcion de producto altamente persuasiva.

Producto: {producto}

Condiciones:
- Máximo 100 palabras
- Tono atractivo, moderno y profesional
- Enfocado en beneficios
- Lenguaje simple
- Incluir llamada a la acción

Formato:
Título  
Descripción
"""

            response = client.chat.completions.create(
                model="gpt-4.1-mini",
                messages=[{"role": "user", "content": prompt}]
            )

            resultado = response.choices[0].message.content

            st.success("Resultado generado:")
            st.write(resultado)

        except Exception as e:
            st.error(f"Error: {e}")

    else:
        st.warning("Por favor ingresá un producto.")

st.markdown("---")

st.header("¿Cómo funciona?")
st.write("""
1. Ingresás el nombre de tu producto  
2. Hacés clic en generar  
3. La IA crea una descripción optimizada para ventas  
""")