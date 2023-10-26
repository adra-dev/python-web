import reflex as rx
from link_bio.components.link_button import link_button
from link_bio.components.title import title
from link_bio.styles.styles import Size as Size
import link_bio.constants as const



def links() -> rx.Component:
    return rx.vstack(
        title("Repositorios"),
        link_button(
            "GitHub", 
            "Portafolio de codigo",
            "icons/github.svg", 
            const.GITHUB_URL
        ),
        link_button(
            "Linkedin", 
            "Perfil de linkedin",
            "icons/linkedin.svg", 
            const.LINKEDIN_URL
        ),
        link_button(
            "CV.pdf", 
            "CV para descargar en pdf",
            "icons/download.svg", 
            "https://github.com/adra-dev"
        ),
        link_button(
            "Kaggle", 
            "Repositorios de Kaggle",
            "icons/github.svg",
            "https://github.com/adra-dev"
        ),

        title("Repositorios"),
        link_button(
            "GitHub", 
            "Portafolio de codigo",
            "icons/github.svg", 
            const.GITHUB_URL
        ),
        link_button(
            "Linkedin", 
            "Perfil de linkedin",
            "icons/github.svg", 
            const.LINKEDIN_URL
        ),
        link_button(
            "CV.pdf", 
            "CV para descargar en pdf",
            "icons/github.svg", 
            "https://github.com/adra-dev"
        ),
        link_button(
            "Kaggle", 
            "Repositorios de Kaggle",
            "icons/github.svg",
            "https://github.com/adra-dev"
        ),

        title("Contacto"),
        link_button(
            "MyPublicInbox",
            "Respuesta rápida y con preferencia",
            "icons/github.svg",
            const.MYPUBLICINBOX_URL
        ),
        link_button(
            "Email",
            const.EMAIL,
            "icons/email.svg",
            f"mailto:{const.EMAIL}"
        ),
        width="100%",
        spacing=Size.MEDIUM.value,
    )