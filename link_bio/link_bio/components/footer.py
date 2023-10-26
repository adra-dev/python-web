import reflex as rx
import datetime
import link_bio.constants as const
from link_bio.styles.styles import Size as Size
from link_bio.styles.colors import Color as Color
from link_bio.styles.colors import TextColor as TextColor


def footer() -> rx.Component:
    return rx.vstack(
        rx.image(
            src="GitHub_Logo_White.png",
            height=Size.VERYBIG.value
        ),
        rx.link(
            rx.box(
                f"@ 2021-{datetime.date.today().year}",
                rx.span("adradev by Adrian Rodriguez", color=Color.PRIMARY.value),
                "v3."
            ),
            href=const.GITHUB_URL,
            is_external=True,
            font_size=Size.MEDIUM.value
        ),
        rx.text(
            "BUILDING SOFTWARE TO FIND SOLUTIONS.",
            font_size=Size.MEDIUM.value,
            margin_top=Size.ZERO.value,
        ),
        margin_bottom=Size.BIG.value,
        padding_bottom=Size.BIG.value,
        spacing=Size.DEFAULT.value,
        color=TextColor.FOOTER.value,
    )
