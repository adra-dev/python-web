import reflex as rx
import datetime

def footer() -> rx.Component:
    return rx.vstack(
        rx.image(src="favicon.ico"),
        rx.link(
            f"@ 2021-{datetime.date.today().year} ADRADEV BY ADRIAN RODRIGUEZ V1.",
            href="https://github.com/adra-dev",
            is_external=True
        ),
        rx.text("BUILDING SOFTWARE TO FIND SOLUTIONS.")
    )