import reflex as rx
from alejoide.styles import styles
from alejoide.modules.constants import Links, App
from alejoide.components.logo import logo


def footer() -> rx.Component:
    return rx.vstack(
        logo(clickable=False),
        rx.text(
            "© 2023",
            rx.link(
                f" {App.NAME.value} by Alejo Sarmiento ",
                href=Links.APP_URL.value,
                color=styles.colors.Main.ACCENT.value,
                style=styles.DARK_LINKS,
            ),
            "v1."
        ),
        style=styles.FOOTER,
    )