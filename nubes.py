import streamlit as st
from menu import menu
from about import about

# Define los diccionarios de texto aquí o en un módulo separado que importas.
textos_es = {
    'titulo_pagina': "Detección de nubes",
    'menu_principal': "Principal",
    'menu_conocenos': "Conócenos",
    'label_menu': "Menú :bookmark_tabs:",
}

textos_en = {
    'titulo_pagina': "Cloud Detection",
    'menu_principal': "Main",
    'menu_conocenos': "About Us",
    'label_menu': "Menu :bookmark_tabs:",
}

def main():
    # Establece el título de la página y el icono solo una vez, aquí al inicio del script.
    st.set_page_config(page_title="Cloud Detection", page_icon=":sun_behind_cloud")

    # Si 'idioma' no está en state, se establece a 'es' por defecto
    if 'idioma' not in st.session_state:
        st.session_state['idioma'] = 'es'

    # Selector de idioma en el sidebar, solo un elemento de UI para la selección de idioma.
    idioma_seleccionado = st.sidebar.selectbox("Elige idioma/Choose Language", ['Español', 'English'])
    if idioma_seleccionado == 'Español':
        st.session_state['idioma'] = 'es'
    else:
        st.session_state['idioma'] = 'en'

    # Selecciona el diccionario de texto apropiado basado en el idioma seleccionado.
    textos = textos_es if st.session_state['idioma'] == 'es' else textos_en

    # Menú de navegación
    opciones = [textos['menu_principal'], textos['menu_conocenos']]
    opcion = st.sidebar.selectbox(label=textos['label_menu'], options=opciones)

    # Lógica de navegación
    if opcion == textos['menu_principal']:
        menu(st.session_state['idioma'])
    elif opcion == textos['menu_conocenos']:
        about(st.session_state['idioma'])

if __name__ == "__main__":
    main()
