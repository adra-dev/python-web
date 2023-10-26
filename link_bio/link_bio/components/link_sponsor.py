import reflex as rx
import link_bio.styles.styles as styles
from link_bio.styles.styles import Size as Size


def link_sponsors(imagen: str, url: str) -> rx.Component:
    return rx.link(
        rx.image(
            height=Size.VERYBIG.value,
            src=imagen
        ),
        href=url,
        is_external=True
    )
