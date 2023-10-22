import reflex as rx
from link_bio.components.link_button import link_button
from link_bio.components.title import title
from link_bio.styles.styles import Size as Size



def links() -> rx.Component:
    return rx.vstack(
        title("Repositorios"),
        link_button(
            "GitHub", 
            "Portafolio de codigo", 
            "https://github.com/adra-dev"
        ),
        link_button(
            "Linkedin", 
            "Perfil de linkedin", 
            "https://github.com/adra-dev"
        ),
        link_button(
            "CV.pdf", 
            "CV para descargar en pdf", 
            "https://github.com/adra-dev"
        ),
        link_button(
            "Kaggle", 
            "Repositorios de Kaggle",
            "https://github.com/adra-dev"
        ),
        title("Repositorios"),
        link_button(
            "GitHub", 
            "Portafolio de codigo", 
            "https://github.com/adra-dev"
        ),
        link_button(
            "Linkedin", 
            "Perfil de linkedin", 
            "https://github.com/adra-dev"
        ),
        link_button(
            "CV.pdf", 
            "CV para descargar en pdf", 
            "https://github.com/adra-dev"
        ),
        link_button(
            "Kaggle", 
            "Repositorios de Kaggle",
            "https://github.com/adra-dev"
        ),
        width="100%",
        spacing=Size.MEDIUM.value
    )