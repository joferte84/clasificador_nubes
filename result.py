import streamlit as st
from PIL import Image
from streamlit_lottie import st_lottie

lottie_url = "https://lottie.host/e6640a08-055a-4ee6-b26e-f2679bab0c65/m4WtzxGtgI.json"
def result():
    
    st.title("Resultados")
    st.lottie(lottie_url, width=650, height=300)
    st.write("La pestaña `Resultados` es donde el rigor científico se fusiona con la visualización creativa. En este espacio, presentamos una serie de gráficas que capturan la esencia del rendimiento de nuestro modelo de Machine Learning. Cada visualización está diseñada para ofrecerte una visión clara y detallada de cómo nuestro clasificador de nubes procesa y evalúa los datos. Aquí, encontrarás desde la precisión y la eficiencia hasta la efectividad global del modelo, representadas en formatos que hacen que la interpretación de los resultados sea tan accesible como fascinante. Prepárate para explorar la interacción entre los fenómenos naturales y la capacidad analítica de la inteligencia artificial, todo presentado a través de una lente que realza tanto la funcionalidad técnica como la belleza visual de nuestro trabajo.")
    
    tab1, tab2, tab3 = st.tabs(["Curva de Aprendizaje", "Métricas", "Matriz de Confusión"])
    
    with tab1:
        st.write("Estas gráficas muestran la pérdida y la precisión del modelo a lo largo de las épocas de entrenamiento para los conjuntos de entrenamiento y validación.")
        st.image(Image.open("Pictures/output.png"), caption="Imagen de ejemplo", width=700)
        st.write("Conclusiones:")
        st.write("La pérdida de entrenamiento disminuye de manera constante, lo que indica que el modelo está aprendiendo y mejorando con cada época.")
        st.write("La pérdida de validación disminuye inicialmente y después fluctua.")
        st.write("La precisión de entrenamiento mejora con el tiempo. Sin embarlo, la precisión de validación parece estancarse.")

    with tab2:
        st.write("En la pestaña `Métricas`, examinamos la precisión, el recall y la puntuación F1 de nuestro modelo para cada clase. Estos indicadores nos ayudan a entender mejor cómo se desempeña el modelo con cada tipo de nube, destacando áreas donde el rendimiento es fuerte y otras donde necesitamos mejorar, especialmente en clases con menor representación en los datos.")
        st.image(Image.open("Pictures/newplot.png"), caption="Imagen de ejemplo", width=700)
        st.write("Conclusiones:")
        st.write("La clase `Gravel` tiene el recall más alto, lo que significa que el modelo es bastante bueno detectando esta clase cuando está presente.")
        st.write("La clase `Flower` tiene la puntuación F1 más baja, lo que indica que tanto la precisión como el recall son bajos para esta clase; esto puede deberse al desbalanceo de datos mencionado anteriormente.")
        st.write("La clase `Sugar` tiene una buena puntuación F1, lo que sugiere que el modelo es equilibrado en términos de precisión y recall para esta clase.")

    with tab3:
        st.write("Esta gráfica es una matriz de confusión que muestra el número de predicciones correctas e incorrectas del modelo para cada clase. Los números en la diagonal representan las predicciones correctas para cada clase (verdaderos positivos). Las otras celdas muestran el número de veces que una clase fue confundida con otra (falsos positivos y falsos negativos)")
        st.image(Image.open("Pictures/graf.png"), caption="Imagen de ejemplo", width=600)
        st.write("Conclusiones:")
        st.write("Las categorías `Gravel` y `Sugar` son las más fácilmente identificadas por el modelo, con la mayoría de sus predicciones siendo correctas.")
        st.write("La categoría `Fish` tiende a confundirse considerablemente con `Sugar`, indicando que el modelo tiene dificultades para distinguir entre estas dos clases.")
        st.write("`Flower` es a menudo mal clasificada como `Sugar`, lo que sugiere que el modelo puede estar sobreajustado hacia la categoría `Sugar`.")
        
if __name__ == "__result__":
    result()
