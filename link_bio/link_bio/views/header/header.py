import reflex as rx
from link_bio.components.link_icon import link_icon
from link_bio.components.info_text import info_text
from link_bio.styles.styles import Size as Size

def header() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.avatar(name="Adrian Rodriguez", size="xl"),
            rx.vstack(
                rx.heading(
                    "ADRIAN RODRIGUEZ", 
                    size="lg"
                ),
                rx.text(
                    "@adradev",
                    margin_top="0px !important"
                ),
                rx.hstack(
                    link_icon("https://github.com/adra-dev/python-web"),
                    link_icon("https://github.com/adra-dev/python-web"),
                    link_icon("https://github.com/adra-dev/python-web"),
                ),
                align_items="start"
            ),
            spacing=Size.DEFAULT.value
        ),
        rx.flex(
            info_text("2", "años de experiencia"),
            rx.spacer(),
            info_text("2", "años de experiencia"),
            rx.spacer(),
            info_text("2", "años de experiencia"),
            width="100%"
        ),
        rx.text("""Soy ingeniero de software desde hace 2 años.
                Actualmente me dedico a mejorar mis perfiles como 
                Data Scientist, PostgresDBA, PythonDev. 
                Aqui podras encontrar todos mis enlaces de interes. ¡Bienvenid@!"""),
        spacing=Size.BIG.value,
        align_items="start"
    )
