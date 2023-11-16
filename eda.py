import streamlit as st
import plotly.express as px
import pandas as pd
from streamlit_lottie import st_lottie

lottie_url = "https://lottie.host/cd8399a4-af0c-41a1-9fff-246602b31bcf/63kQhSDING.json"
def eda():
    
    df = pd.read_csv(filepath_or_buffer = "Datos.csv")
    df_sun = pd.read_csv(filepath_or_buffer = "csv_sunburst.csv")
    st.title("Exploratory Data Analysis")
    
    st.lottie(lottie_url, width=650, height=300)
    
    st.markdown("En la pestaña de EDA `Análisis Exploratorio de Datos`, nos centramos en la exploración y comprensión de nuestro conjunto limitado de imágenes: 4394 para entrenamiento y 1073 para pruebas. Esta sección te ofrece visualizaciones interactivas y análisis detallados que reflejan las diversas formas de las nubes, así como el desbalanceo de datos entre las categorías que estamos clasificando. Aunque la clase Flower tenía aproximadamente la mitad de los datos en comparación con Sugar, optamos por no utilizar técnicas como SMOTE, submuestreo o penalización de clases, debido a la complejidad de las imágenes y el mínimo impacto de estas técnicas en el rendimiento. En lugar de alterar nuestro conjunto de datos, decidimos mantener su autenticidad. En esta sección, te invitamos a explorar estos desafíos y a apreciar la riqueza de los datos naturales, enfocándonos en el análisis exploratorio y la comprensión de las formaciones nubosas.")

    clouds_options = list(df_sun["label"].value_counts().index)
    clouds = st.sidebar.multiselect(label = "Clouds :sun_behind_cloud:", options = clouds_options,
                                  default = clouds_options[:10])
    
    dfg = df_sun[df_sun["label"].isin(clouds)]
    
    col1, col2 = st.columns([1, 1])

    # Pie Chart
    fig = px.sunburst(dfg, path=["set","label"], values="Unnamed: 0", color="set")
    fig.update_traces(textinfo="label+percent parent")
    
    fig_bar = px.bar(dfg, x="Unnamed: 0", y="label", color="set",)
    fig_bar.update_layout(legend = dict( orientation="h", yanchor="top", y=0.02, xanchor="right", x=0.8, itemwidth=40), xaxis_showticklabels=False, xaxis_title=None, yaxis_title=None)
    fig_bar.update_traces(width = 0.65)

    col1.plotly_chart(figure_or_data = fig_bar, use_container_width = True)
    col2.plotly_chart(figure_or_data = fig, use_container_width = True)
    
    with st.expander(label = "DataFrame", expanded = False):
        st.dataframe(df)
        
    if __name__ == "__eda__":
        eda()











































