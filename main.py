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


    def calcular(e):
        if peso.value=="" or altura.value=="" or genero.value=="":
            page.banner.open = True
            page.update()
        else:
            valor_peso = float(peso.value)
            valor_altura = float(altura.value)
            # Calcular o IMC
            imc = valor_peso / (valor_altura * valor_altura)
            imc = float(f"{imc:.2f}")
            # Exibir o valor do IMC
            IMC.value = f"Seu IMC é {imc}"
            if genero.value == "Feminino":
                if imc < 18.5:
                    img_resultado.src = f"w_slim.png"
                    detalhes.value = "Abaixo do peso"
                elif 18.5 <= imc < 24.9:
                    img_resultado.src = f"w_normal.png"
                    detalhes.value = "Peso saudável"
                elif 25 <= imc < 29.9:
                    img_resultado.src = f"w_fat.png"
                    detalhes.value = "Sobrepeso ou pré obeso"
                elif 30 <= imc < 34.9:
                    img_resultado.src = f"w_fat.png"
                    detalhes.value = "Obeso"
                else:
                    img_resultado.src = f"w_fat.png"
                    detalhes.value = "Severamente obeso"
            else:
                if imc < 18.5:
                    img_resultado.src = f"m_slim.png"
                    detalhes.value = "Abaixo do peso"
                elif 18.5 <= imc < 24.9:
                    img_resultado.src = f"m_normal.png"
                    detalhes.value = "Peso saudável"
                elif 25 <= imc < 29.9:
                    img_resultado.src = f"m_fat.png"
                    detalhes.value = "Sobrepeso ou pré obeso"
                elif 30 <= imc < 34.9:
                    img_resultado.src = f"m_fat.png"
                    detalhes.value = "Obeso"
                else:
                    img_resultado.src = f"m_fat.png"
                    detalhes.value = "Severamente obeso"
        # limpar os campos
        peso.value = ""
        altura.value = ""
        genero.value = ""
        # Atualizar a página
        page.update()

    
    # Configurando a página
    page.banner = ft.Banner(
        bgcolor=ft.colors.SURFACE_VARIANT,
        leading=ft.Icon(ft.icons.WARNING_AMBER_OUTLINED, color=ft.colors.RED, size=40),
        content=ft.Text("Ops, preencha todos os campos!", color=ft.colors.YELLOW, weight=ft.FontWeight.BOLD),
        actions=[
            ft.TextButton("OK", on_click=close_banner),
        ],
    )

    altura = ft.TextField(label="Altura", hint_text="Por favor insira a sua altura")
    peso = ft.TextField(label="Peso", hint_text="Por favor insira o seu peso")
    genero = ft.Dropdown(
        label="Genero",
        hint_text="Escolha o seu genero",
        options=[
            ft.dropdown.Option("Masculino"),
            ft.dropdown.Option("Feminino")
        ]
    )

    # Botão calcular IMC
    b_calcular = ft.ElevatedButton(text="Calcular IMC", on_click=calcular)

    # Exibir o IMC e resultado
    IMC = ft.Text("Seu IMC é ...", size=30)
    detalhes = ft.Text("Insira seus dados", size=20)
    img_capa = ft.Image(
        src=f"logo.png",
        width=100,
        height=100,
        fit=ft.ImageFit.CONTAIN,
    )
    info_app_resultado = ft.Column(
        controls=[
            IMC,
            detalhes,
        ]
    )
    img_resultado = ft.Image(
        src=f"logo.png",
        width=100,
        height=100,
        fit=ft.ImageFit.CONTAIN,
    )
    info = ft.Row(
        controls=[
            info_app_resultado,
            img_resultado,
        ]
    )

    # Layout da pagina
    layout = ft.ResponsiveRow(
        [
            ft.Container(
                info,
                padding=5,
                col={"sm":4, "md":4, "xl":1},
                alignment=ft.alignment.center,
            ),
            ft.Container(
                altura,
                padding=5,
                # bgcolor=ft.colors.WHITE,
                col={"sm":12, "md":3, "xl":3},
            ),
            ft.Container(
                peso,
                padding=5,
                # bgcolor=ft.colors.WHITE,
                col={"sm":12, "md":3, "xl":3},
            ),
            ft.Container(
                genero,
                padding=5,
                # bgcolor=ft.colors.WHITE,
                col={"sm":12, "md":3, "xl":3},
            ),
            ft.Container(
                b_calcular,
                padding=5,
                # bgcolor=ft.colors.WHITE,
                col={"sm":12, "md":3, "xl":3},
            ),
            ft.Container(
                padding=5,
                bgcolor=ft.colors.WHITE,
                col={"sm":12, "md":3, "xl":3},
            ),
        ]
    )

    page.add(layout)

    page.update()


ft.app(target=main)
