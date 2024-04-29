import flet as ft

def main(page:ft.Page):
    page.appbar = ft.AppBar(
        leading= ft.Icon(ft.icons.MULTILINE_CHART),
        leading_width=40,
        title=ft.Text("Calculadora IMC", weight=ft.FontWeight.BOLD),
        center_title=False,
        bgcolor=ft.colors.SURFACE_VARIANT,
    )

    page.window_width = 400
    page.window_height = 550

    # Configuração do banner de notificação
    def close_banner(e):
        page.banner.open = False
        page.update()


    page.banner = ft.Banner(
        bgcolor=ft.colors.SURFACE_VARIANT,
        leading=ft.Icon(ft.icons.WARNING_AMBER_OUTLINED, color=ft.colors.RED, size=40),
        content=ft.Text("Ops, preencha todos os campos!", color=ft.colors.YELLOW, weight=ft.FontWeight.BOLD),
        actions=[
            ft.TextButton("OK", on_click=close_banner),
        ],
    )



    page.add()

    page.update()


ft.app(target=main)
