import reflex as rx
from link_bio.components.link_icon import link_icon
from link_bio.components.info_text import info_text
from link_bio.styles.styles import Size as Size
from link_bio.styles.colors import Color as Color
from link_bio.styles.colors import TextColor as TextColor
import link_bio.constants as const
import datetime


def header() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.avatar(
                name="Adrian Rodriguez", 
                size="xl",
                src="avatar.jpg",
                color=TextColor.BODY.value,
                bg=Color.CONTENT.value,
                padding="2px",
                border="4px",
                border_color=Color.PRIMARY.value
            ),
            rx.vstack(
                rx.heading(
                    "ADRIAN RODRIGUEZ", 
                    size="lg",
                ),
                rx.text(
                    "@adradev",
                    margin_top=Size.ZERO.value,
                    color=Color.PRIMARY.value,
                ),
                rx.hstack(
                    link_icon(
                        "icons/github.svg",
                        const.GITHUB_URL
                    ),
                    link_icon(
                        "icons/github.svg",
                        const.GITHUB_URL
                    ),
                    link_icon(
                        "icons/github.svg",
                        const.GITHUB_URL
                    ),
                    spacing=Size.LARGE.value
                ),
                align_items="start"
            ),
            spacing=Size.DEFAULT.value
        ),
        rx.flex(
            info_text(
                f"{experience()}+", 
                "años de experiencia"
            ),
            rx.spacer(),
            info_text(
                "2", "años de experiencia"
            ),
            rx.spacer(),
            info_text(
                "2", "años de experiencia"
            ),
            width="100%"
        ),
        rx.text(
            f"""
            Soy ingeniero de software desde hace {experience()} años.
            Actualmente me dedico a mejorar mis perfiles como 
            Data Scientist, PostgresDBA, PythonDev. 
            Aqui podras encontrar todos mis enlaces de interes. ¡Bienvenid@!
            """,
            font_size=Size.DEFAULT.value,
            color=TextColor.BODY.value,
        ),
        spacing=Size.BIG.value,
        align_items="start"
    )


def experience() -> int:
    return datetime.date.today().year - 2021