import flet as ft


def main(page: ft.Page):
    page.title = "Contador interactivo"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    contador = 0

    texto_contador = ft.Text(
        value="0",
        size=50,
        weight=ft.FontWeight.BOLD,
    )

    def incrementar(e):
        nonlocal contador
        contador += 1
        texto_contador.value = str(contador)
        page.update()

    boton = ft.Button(
        "Incrementar",
        on_click=incrementar,
    )

    page.add(
        ft.Column(
            [
                texto_contador,
                boton,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )


ft.run(main)