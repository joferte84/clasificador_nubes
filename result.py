import streamlit as st
from PIL import Image
from streamlit_lottie import st_lottie

lottie_url = "https://lottie.host/e6640a08-055a-4ee6-b26e-f2679bab0c65/m4WtzxGtgI.json"

textos_es = {
    'titulo': "Resultados",
    'intro': "La pestaña `Resultados` es donde el rigor científico se fusiona con la visualización creativa. En este espacio, presentamos una serie de gráficas que capturan la esencia del rendimiento de nuestro modelo de Machine Learning. Cada visualización está diseñada para ofrecerte una visión clara y detallada de cómo nuestro clasificador de nubes procesa y evalúa los datos. Aquí, encontrarás desde la precisión y la eficiencia hasta la efectividad global del modelo, representadas en formatos que hacen que la interpretación de los resultados sea tan accesible como fascinante. Prepárate para explorar la interacción entre los fenómenos naturales y la capacidad analítica de la inteligencia artificial, todo presentado a través de una lente que realza tanto la funcionalidad técnica como la belleza visual de nuestro trabajo.",
    'tab1_titulo': "Curva de Aprendizaje",
    'tab1_contenido': "Estas gráficas muestran la pérdida y la precisión del modelo a lo largo de las épocas de entrenamiento para los conjuntos de entrenamiento y validación. La pérdida de entrenamiento disminuye de manera constante, lo que indica que el modelo está aprendiendo y mejorando con cada época. La pérdida de validación disminuye inicialmente y después fluctúa. La precisión de entrenamiento mejora con el tiempo, mientras que la precisión de validación parece estancarse.",
    'tab2_titulo': "Métricas",
    'tab2_contenido': "En la pestaña `Métricas`, examinamos la precisión, el recall y la puntuación F1 de nuestro modelo para cada clase. Estos indicadores nos ayudan a entender mejor cómo se desempeña el modelo con cada tipo de nube, destacando áreas donde el rendimiento es fuerte y otras donde necesitamos mejorar, especialmente en clases con menor representación en los datos. La clase `Gravel` tiene el recall más alto, lo que significa que el modelo es bastante bueno detectando esta clase cuando está presente. La clase `Flower` tiene la puntuación F1 más baja, lo que indica que tanto la precisión como el recall son bajos para esta clase; esto puede deberse al desbalanceo de datos mencionado anteriormente. La clase `Sugar` tiene una buena puntuación F1, lo que sugiere que el modelo es equilibrado en términos de precisión y recall para esta clase.",
    'tab3_titulo': "Matriz de Relación",
    'tab3_contenido': "Esta gráfica es una matriz de confusión que muestra el número de predicciones correctas e incorrectas del modelo para cada clase. Los números en la diagonal representan las predicciones correctas para cada clase (verdaderos positivos). Las otras celdas muestran el número de veces que una clase fue confundida con otra (falsos positivos y falsos negativos). Las categorías `Gravel` y `Sugar` son las más fácilmente identificadas por el modelo, con la mayoría de sus predicciones siendo correctas. La categoría `Fish` tiende a confundirse considerablemente con `Sugar`, indicando que el modelo tiene dificultades para distinguir entre estas dos clases. `Flower` es a menudo mal clasificada como `Sugar`, lo que sugiere que el modelo puede estar sobreajustado hacia la categoría `Sugar`."
}

textos_en = {
    'titulo': "Results",
    'intro': "The `Results` tab is where scientific rigor merges with creative visualization. In this space, we present a series of graphs that capture the essence of our Machine Learning model's performance. Each visualization is designed to give you a clear and detailed view of how our cloud classifier processes and evaluates data. Here, you'll find everything from accuracy and efficiency to the overall effectiveness of the model, represented in formats that make interpreting the results as accessible as they are fascinating. Get ready to explore the interaction between natural phenomena and the analytical capacity of artificial intelligence, all presented through a lens that enhances both the technical functionality and visual beauty of our work.",
    'tab1_titulo': "Learning Curve",
    'tab1_contenido': "These graphs show the model's loss and accuracy over the training epochs for both the training and validation sets. The training loss decreases steadily, indicating that the model is learning and improving with each epoch. The validation loss initially decreases and then fluctuates. Training accuracy improves over time, while validation accuracy seems to plateau.",
    'tab2_titulo': "Metrics",
    'tab2_contenido': "In the `Metrics` tab, we examine the accuracy, recall, and F1 score of our model for each class. These indicators help us better understand how the model performs with each type of cloud, highlighting areas where performance is strong and others where we need to improve, especially in classes with less representation in the data. The `Gravel` class has the highest recall, meaning the model is quite good at detecting this class when present. The `Flower` class has the lowest F1 score, indicating both precision and recall are low for this class; this may be due to the data imbalance mentioned earlier. The `Sugar` class has a good F1 score, suggesting the model is balanced in terms of precision and recall for this class.",
    'tab3_titulo': "Relation Matrix",
    'tab3_contenido': "This graph is a confusion matrix showing the number of correct and incorrect predictions by the model for each class. The numbers on the diagonal represent correct predictions for each class (true positives). The other cells show how many times a class was confused with another (false positives and false negatives). The `Gravel` and `Sugar` categories are the most easily identified by the model, with most of their predictions being correct. The `Fish` category tends to be considerably confused with `Sugar`, indicating that the model struggles to distinguish between these two classes. `Flower` is often misclassified as `Sugar`, suggesting the model may be overfitted towards the `Sugar` category."
}

textos_es['conclusiones'] = "Conclusiones:"
textos_en['conclusions'] = "Conclusions:"


textos_es['tab1_conclusiones'] = [
    "La pérdida de entrenamiento disminuye de manera constante, lo que indica que el modelo está aprendiendo y mejorando con cada época.",
    "La pérdida de validación disminuye inicialmente y después fluctúa.",
    "La precisión de entrenamiento mejora con el tiempo, mientras que la precisión de validación parece estancarse."
]

textos_es['tab2_conclusiones'] = [
    "La clase `Gravel` tiene el recall más alto, lo que significa que el modelo es bastante bueno detectando esta clase cuando está presente.",
    "La clase `Flower` tiene la puntuación F1 más baja, lo que indica que tanto la precisión como el recall son bajos para esta clase; esto puede deberse al desbalanceo de datos mencionado anteriormente.",
    "La clase `Sugar` tiene una buena puntuación F1, lo que sugiere que el modelo es equilibrado en términos de precisión y recall para esta clase."
]

textos_es['tab3_conclusiones'] = [
    "Las categorías `Gravel` y `Sugar` son las más fácilmente identificadas por el modelo, con la mayoría de sus predicciones siendo correctas.",
    "La categoría `Fish` tiende a confundirse considerablemente con `Sugar`, indicando que el modelo tiene dificultades para distinguir entre estas dos clases.",
    "`Flower` es a menudo mal clasificada como `Sugar`, lo que sugiere que el modelo puede estar sobreajustado hacia la categoría `Sugar`."
]

textos_en['tab1_conclusiones'] = [
    "Training loss decreases steadily, indicating that the model is learning and improving with each epoch.",
    "Validation loss initially decreases and then fluctuates.",
    "Training accuracy improves over time, while validation accuracy seems to plateau."
]

textos_en['tab2_conclusiones'] = [
    "The `Gravel` class has the highest recall, meaning the model is quite good at detecting this class when present.",
    "The `Flower` class has the lowest F1 score, indicating both precision and recall are low for this class; this may be due to the data imbalance mentioned earlier.",
    "The `Sugar` class has a good F1 score, suggesting the model is balanced in terms of precision and recall for this class."
]

textos_en['tab3_conclusiones'] = [
    "The `Gravel` and `Sugar` categories are the most easily identified by the model, with most of their predictions being correct.",
    "The `Fish` category tends to be considerably confused with `Sugar`, indicating the model struggles to distinguish between these two classes.",
    "`Flower` is often misclassified as `Sugar`, suggesting the model may be overfitted towards the `Sugar` category."
]


def result(idioma='es'):
    textos = textos_es if idioma == 'es' else textos_en

    st.title(textos['titulo'])
    st.lottie(lottie_url, width=650, height=300)
    st.write(textos['intro'])
    
    tab1, tab2, tab3 = st.tabs([textos['tab1_titulo'], textos['tab2_titulo'], textos['tab3_titulo']])
    

    with tab1:
        st.write(textos['tab1_contenido'])
        st.image(Image.open("Pictures/output.png"), caption="Imagen de ejemplo", width=700)
        st.write(textos[idioma == 'es' and 'conclusiones' or 'conclusions'])  
        for conclusion in textos['tab1_conclusiones']:
            st.write(conclusion)

    with tab2:
        st.write(textos['tab2_contenido'])
        st.image(Image.open("Pictures/newplot.png"), caption="Imagen de ejemplo", width=700)
        st.write(textos[idioma == 'es' and 'conclusiones' or 'conclusions'])  
        for conclusion in textos['tab2_conclusiones']:
            st.write(conclusion)

    with tab3:
        st.write(textos['tab3_contenido'])
        st.image(Image.open("Pictures/graf.png"), caption="Imagen de ejemplo", width=700)
        st.write(textos[idioma == 'es' and 'conclusiones' or 'conclusions'])  
        for conclusion in textos['tab3_conclusiones']:
            st.write(conclusion)
        
        
if __name__ == "__result__":
    result()
