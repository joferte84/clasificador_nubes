import streamlit as st
from PIL import Image
import tensorflow as tf
import numpy as np
import os
from streamlit_lottie import st_lottie
import plotly.express as px

lottie_url = "https://lottie.host/a2918a43-1ece-404f-9fc5-28a34def4574/9frnYzLVqE.json"

# Cargar el modelo pre-entrenado
def load_model():
    model = tf.keras.models.load_model('mi_modelo.h5')
    return model

category_names = {
    0: "Fish",
    1: "Flower",
    2: "Gravel",
    3: "Sugar"}

carpeta_imagenes = 'classified_correctly'

lista_archivos = os.listdir(carpeta_imagenes)

lista_imagenes = [os.path.join(carpeta_imagenes, nombre_archivo) for nombre_archivo in lista_archivos if nombre_archivo.endswith('.jpg') or nombre_archivo.endswith('.png')]

def ml():
    st.title("Machine Learning")
    st.lottie(lottie_url, width=650, height=300)
    st.markdown("La pestaña de `Machine Learning` es el corazón de nuestro proyecto. Aquí presentamos nuestro modelo de IA más exitoso: una Red Neuronal Convolucional `CNN`, meticulosamente diseñada para identificar y clasificar nubes en las cuatro categorías: Flower, Fish, Graver y Sugar. Experimenta la magia de la inteligencia artificial con un carrusel de imágenes donde nuestro modelo RNN demuestra su capacidad para analizar y clasificar cada nube en tiempo real. Este espacio  te permite apreciar la complejidad y la estética intrínsecas de las nubes a través de la tecnología avanzada.")
    st.markdown("En nuestra implementación de una Red Neuronal Convolucional `CNN`, incorporamos técnicas avanzadas como ReduceLROnPlateau, EarlyStopping y ModelCheckpoint para optimizar el rendimiento. Curiosamente, de estas, solo ModelCheckpoint se activó, lo que indica cómo nuestra CNN logró un equilibrio efectivo en el entrenamiento sin necesidad de reducir la tasa de aprendizaje o detenerse prematuramente debido a la falta de mejoras.")
    
    # Cargar el modelo entrenado
    model = tf.keras.models.load_model('mi_modelo.h5')

    # Función para preprocesar la imagen cargada
    def preprocess_image(image):
        img = np.array(image)
        img = tf.image.resize(img, (224, 224))
        img = img / 255.0 
        img = np.expand_dims(img, axis=0)
        return img

    imagen_seleccionada = st.selectbox('Selecciona una imagen', lista_imagenes)
    
    if imagen_seleccionada:
        image = Image.open(imagen_seleccionada)
        
        processed_image = preprocess_image(image)  
        prediction = model.predict(processed_image)
        predicted_class = np.argmax(prediction)
        predicted_label = category_names[predicted_class]
        
        fig = px.bar(
            x=list(category_names.values()), 
            y=prediction[0], 
            labels={'x': 'Categoría', 'y': 'Confianza'})
                    
        col1, col2= st.columns(2)
        
        with col1:
            st.image(image, caption='Imagen seleccionada', use_column_width=True)
            
        with col2:
            st.plotly_chart(fig, use_container_width=True)
        
    st.markdown(f"<h1 style='text-align: center;'>{predicted_label}</h1>", unsafe_allow_html=True)
   
if __name__ == "__ml__":
    ml()