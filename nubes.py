import streamlit as st
from menu import menu
from about import about
from streamlit_lottie import st_lottie

def main():
    
    st.set_page_config(page_title="Detección de nubes", page_icon=":sun_behind_cloud",)
    
    opciones = ["Principal", "Conócenos"]
    
    opcion = st.sidebar.selectbox(label = "Menu :bookmark_tabs:", options = opciones)
    
    if opcion == "Principal":  
        menu()

    elif opcion == "Conócenos":
        about()

if __name__ == "__main__":
        main()
