import reflex as rx

def header() -> rx.Component:
    return rx.vstack(
        rx.avatar(name="Adrian Rodriguez", size="xl"),
        rx.text("@adradev"),
        rx.text("HOLA MI NOMBRE ES ADRIAN RODRIGUEZ"),
        rx.text("""Soy ingeniero de software desde hace 2 años.
                Actualmente me dedico a mejorar mis perfiles como 
                Data Scientist, PostgresDBA, PythonDev. 
                Aqui podras encontrar todos mis enlaces de interes. ¡Bienvenid@!"""),
    )
