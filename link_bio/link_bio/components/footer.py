import reflex as rx
import datetime
from link_bio.styles.styles import Size as Size

def footer() -> rx.Component:
    return rx.vstack(
        rx.image(src="favicon.ico"),
        rx.link(
            f"@ 2021-{datetime.date.today().year} adradev by Adrian Rodriguez v1.",
            href="https://github.com/adra-dev",
            is_external=True,
            font_size=Size.MEDIUM.value
        ),
        rx.text(
            "BUILDING SOFTWARE TO FIND SOLUTIONS.",
            font_size=Size.MEDIUM.value,
            margin_top="0px !important"
        ),
        margin_bottom=Size.BIG.value
    )