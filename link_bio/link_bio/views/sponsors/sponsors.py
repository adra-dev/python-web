import reflex as rx
import link_bio.constants as const
from link_bio.styles.styles import Size as Size
from link_bio.components.title import title
from link_bio.components.link_sponsor import link_sponsors

def sponsors() -> rx.Component:
    return rx.stack(
        title("Colaboran"),
        rx.hstack(
            link_sponsors(
                "github-mark-white.png",
                const.GITHUB_URL
            ),
            link_sponsors(
                "GitHub_Logo_White.png",
                const.GITHUB_URL
            ),
            spacing=Size.BIG.value,
        ),
        width="100%",
        align_items="start",
        spacing=Size.MEDIUM.value,
    )