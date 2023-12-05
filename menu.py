import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import seaborn as sns 

from PIL import Image

import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu
from streamlit_extras.add_vertical_space import add_vertical_space

from eda import eda
from ml import ml
from result import result

textos_es = {
    'titulo': "¡Bienvenido a nuestra clasificación de nubes en Streamlit!:sun_behind_cloud:",
    'intro': "Bienvenidos a **Descubriendo el Cielo**, un proyecto innovador que une la belleza del cielo capturada en fotografías por satélites de la NASA con el poder de la inteligencia artificial. En este viaje, exploraremos juntos la vasta y misteriosa morfología de las nubes, clasificándolas en cuatro categorías fascinantes: Flower, Fish, Graver y Sugar. Estas categorías, identificadas en las imágenes satelitales, representan formas únicas y atractivas que adornan el lienzo del cielo. Utilizando tecnologías avanzadas de aprendizaje automático, incluyendo técnicas como rle_mask para el análisis de máscaras y bounding box para identificar y encuadrar las distintas formaciones nubosas, este proyecto no solo busca ofrecer una nueva perspectiva sobre cómo vemos y comprendemos el cielo, sino también demostrar cómo la IA puede ayudarnos a interpretar y apreciar los complejos patrones naturales que nos rodean:",
    'selecciona_nube': "Selecciona una nube:",
    'nubes': ("Sugar :ice_cream:", "Gravel :umbrella_on_ground:", "Flower :hibiscus:", "Fish :fish:")
}

textos_en = {
    'titulo': "Welcome to our Cloud Classification in Streamlit!:sun_behind_cloud:",
    'intro': "Welcome to **Discovering the Sky**, an innovative project that combines the beauty of the sky captured in photographs by NASA satellites with the power of artificial intelligence. In this journey, we will explore together the vast and mysterious morphology of clouds, classifying them into four fascinating categories: Flower, Fish, Graver, and Sugar. These categories, identified in satellite images, represent unique and captivating shapes that adorn the canvas of the sky. Utilizing advanced machine learning technologies, including techniques like rle_mask for mask analysis and bounding box for identifying and framing different cloud formations, this project not only aims to offer a new perspective on how we see and understand the sky but also demonstrates how AI can help us interpret and appreciate the complex natural patterns that surround us.",
    'selecciona_nube': "Select a cloud:",
    'nubes': ("Sugar :ice_cream:", "Gravel :umbrella_on_ground:", "Flower :hibiscus:", "Fish :fish:")
}

def obtener_textos(idioma):
    return textos_es if idioma == 'es' else textos_en

def menu(idioma='es'):
    
    if 'idioma' not in st.session_state:
        st.session_state['idioma'] = 'es'

    textos = obtener_textos(st.session_state['idioma'])
    
    st.title(textos['titulo'])
    add_vertical_space(2)
    st.write(textos['intro'])
    
    st.write("Sugar :ice_cream:, Gravel :umbrella_on_ground:, Flower :hibiscus: y Fish :fish:")
    
    selected_tab = st.sidebar.radio(textos['selecciona_nube'], textos['nubes'])

    if selected_tab == "Sugar :ice_cream:":
        st.sidebar.image(Image.open("Pictures/Sugar.jpg"), width=300)
        
    elif selected_tab == "Gravel :umbrella_on_ground:":
        st.sidebar.image(Image.open("Pictures/Gravel.jpg"), width=300)
        
    elif selected_tab == "Flower :hibiscus:":
        st.sidebar.image(Image.open("Pictures/Flower.jpg"), width=290)
        
    elif selected_tab == "Fish :fish:":
        st.sidebar.image(Image.open("Pictures/Fish.jpg"), width=300)   
        
    add_vertical_space(2)
    
    selected = option_menu(
    menu_title=None,
    options=["EDA","Machine Learning", "Resultados"],
    icons=["clipboard-data", "boxes", "card-checklist"],
    default_index=0,
    orientation="horizontal")
    
    if selected == "EDA":
        eda(idioma=st.session_state['idioma'])
        
    elif selected == "Machine Learning":
        ml(idioma=st.session_state['idioma'])
        
    if selected == "Resultados":
        result(idioma=st.session_state['idioma'])

if __name__ == "__menu__":
    menu()
