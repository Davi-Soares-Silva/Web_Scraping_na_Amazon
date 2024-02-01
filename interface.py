import flet as ft
from flet import *
from web_scraping import web_scraping


def main(page: ft.Page):
    page.bgcolor = '#b066ff'
    page.window_resizable = False
    page.window_width = 420
    page.window_height =  600
    #page.title = ""
    


    def enviar(e):
        
        nome_produto = produto.value
        nome_usuario = nome.value
        email_usuario = email.value
        #automacao.de.email@gmail.com
        page.clean()

        produto.value = ""
        nome.value = ""
        email.value = ""

        aviso_de_espera = Container(
            content=Row([
                        TextField(
                            read_only=True, 
                            value="Aguarde a confirmação do envio",
                            border="underline",
                            text_align= 'CENTER',
                            color=colors.BLACK
                        )  
                    ], alignment= "center"),
            width= 350,
            height=50,
            padding = padding.only(left=40)
        )
        aviso_de_espera.alignment = alignment.center

        
        aviso_de_envio = Container(
            content=Row([
                        TextField(
                            read_only=True, 
                            value="O e-mail foi enviado!",
                            border="underline",
                            text_align= 'CENTER',
                            color=colors.BLACK
                        )
                    ], alignment= "center"),
            width= 350,
            height=40,
            padding = padding.only(left=40),
        ) 
        aviso_de_envio.alignment = alignment.center
             
        page.add(campos, aviso_de_espera)
        page.update()
        web_scraping(nome_produto, nome_usuario, email_usuario)

        page.add(aviso_de_envio)
        page.update()
        
        
        


    nome = ft.TextField(
        hint_text="Digite seu nome",
        width=350,
        border="underline",
        border_color=colors.BLACK,
        color=colors.BLACK,
        cursor_color=colors.BLACK,
        content_padding=20,
        capitalization=ft.TextCapitalization.SENTENCES
    )
    
    
    email = ft.TextField(
        hint_text="Digite o e-mail para receber os dados",
        width=350,
        border="underline",
        border_color=colors.BLACK,
        color=colors.BLACK,
        cursor_color=colors.BLACK,
        content_padding=20
    )
    
    produto = ft.TextField(
        hint_text="Qual produto deseja buscar?",
        width=350,
        border="underline",
        border_color=colors.BLACK,
        color=colors.BLACK,
        cursor_color=colors.BLACK,
        content_padding=20,
        capitalization=ft.TextCapitalization.SENTENCES
    )
    

    campos = Container(
        content= Column([
            Row([
                ft.Icon(name=ft.icons.PERSON_2_OUTLINED, color=colors.BLACK),
                nome
            ], alignment="center"),

            Row([
                ft.Icon(name=ft.icons.EMAIL_OUTLINED, color=colors.BLACK),
                email
            ], alignment="center"),

            Row([
                ft.Icon(name=ft.icons.SHOPIFY_OUTLINED, color=colors.BLACK),
                produto
            ], alignment="center"),

            Row([
                ft.IconButton(
                    icon=ft.icons.SEARCH,
                    icon_color=colors.BLACK,
                    icon_size=30,
                    tooltip="Buscar preços",
                    on_click= enviar
                ),
            ], alignment="center")
        ], spacing=30),

        padding = padding.only(top=40),
        gradient=ft.LinearGradient(
            begin=ft.alignment.top_center,
            end=ft.alignment.bottom_center,
            colors=['#63a4ff','#b066ff' ]
        ),
        width= 420,
        height=400,
    )
    campos.margin = margin.only(left=-10, right=-20, top = -20)
    page.add(campos)

ft.app(target= main)
