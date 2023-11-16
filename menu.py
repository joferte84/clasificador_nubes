import pandas as pd
import numpy as np
import matplotlib as plt
import seaborn as sns 

from PIL import Image

import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu
from streamlit_extras.add_vertical_space import add_vertical_space

from eda import eda
from ml import ml
from result import result
def menu():

    st.title("Descubriendo el Cielo: Un Viaje a través de las Nubes:sun_behind_cloud:")
    
    add_vertical_space(2)

    st.write("Bienvenidos a **Descubriendo el Cielo**, un proyecto innovador que une la belleza del cielo capturada en fotografías por satélites de la NASA con el poder de la inteligencia artificial. En este viaje, exploraremos juntos la vasta y misteriosa morfología de las nubes, clasificándolas en cuatro categorías fascinantes: Flower, Fish, Graver y Sugar. Estas categorías, identificadas en las imágenes satelitales, representan formas únicas y atractivas que adornan el lienzo del cielo. Utilizando tecnologías avanzadas de aprendizaje automático, incluyendo técnicas como rle_mask para el análisis de máscaras y bounding box para identificar y encuadrar las distintas formaciones nubosas, este proyecto no solo busca ofrecer una nueva perspectiva sobre cómo vemos y comprendemos el cielo, sino también demostrar cómo la IA puede ayudarnos a interpretar y apreciar los complejos patrones naturales que nos rodean:")
    st.write("Sugar :ice_cream:, Gravel :umbrella_on_ground:, Flower :hibiscus: y Fish :fish:")
    
    selected_tab = st.sidebar.radio("Selecciona una nube:", ("Sugar :ice_cream:", "Gravel :umbrella_on_ground:", "Flower :hibiscus:", "Fish :fish:"))

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
        eda()
        
    elif selected == "Machine Learning":
        ml()
        
    elif selected == "Resultados":
        result()

if __name__ == "__menu__":
    menu()
