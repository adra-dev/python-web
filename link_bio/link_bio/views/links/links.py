import reflex as rx
from link_bio.components.link_button import link_button

def links() -> rx.Component:
    return rx.vstack(
        link_button("GitHub", "https://github.com/adra-dev"),
        link_button("Linkedin", "https://github.com/adra-dev"),
        link_button("CV.pdf", "https://github.com/adra-dev"),
        link_button("Kaggle", "https://github.com/adra-dev")
    )