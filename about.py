import streamlit as st
from streamlit_extras.add_vertical_space import add_vertical_space
from PIL import Image

def about(idioma='es'):
    column_sizes = [3, 3]
    col1, col2 = st.columns(column_sizes)

    with col1:
        st.image("Pictures/Jorge.jpg", width=230)
        add_vertical_space(3)  
        st.image("Pictures/Guille.png", width=230)
    
    with col2:
        st.header("Jorge Fernández")    
        st.markdown("[![Foo](https://img.icons8.com/material-outlined/48/000000/github.png)](https://github.com/joferte84)")
        st.markdown("[![Foo](https://content.linkedin.com/content/dam/me/business/en-us/amp/brand-site/v2/bg/LI-Bug.svg.original.svg)](https://www.linkedin.com/in/joferte/)")
        add_vertical_space(14)  
        st.header("Guillermo Santano")
        st.markdown("[![Foo](https://img.icons8.com/material-outlined/48/000000/github.png)](https://github.com/GuillermoSantano)")
        st.markdown("[![Foo](https://content.linkedin.com/content/dam/me/business/en-us/amp/brand-site/v2/bg/LI-Bug.svg.original.svg)](https://www.linkedin.com/in/gms17/)")

    pdf_file_1 = "Pictures/Jorge_Fernández_Tejedor_-_Junior_Data_Scientist.pdf"
    pdf_file_2 = "Pictures/Guillermo Moreno Santano CV.pdf"

    with st.sidebar:
        
        st.markdown("### \n" * 6)
        
        with open(pdf_file_1, "rb") as file:
            st.download_button(
                label="Curriculum Jorge",
                data=file,
                file_name="Jorge_Fernández_Tejedor_-_Junior_Data_Scientist.pdf",
                mime="application/octet-stream")

        st.markdown("### \n" * 3)
        
        with open(pdf_file_2, "rb") as file:
            st.download_button(
                label="Curriculum Guillermo",
                data=file,
                file_name="Guillermo Moreno Santano CV.pdf",
                mime="application/octet-stream")


if __name__ == "__about__":
    about()

    about()
