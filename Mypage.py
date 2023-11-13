import flet as ft

def main(page: ft.Page):
    page.title = "Pagina de Prueba"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    
    page.appbar = ft.AppBar(
        title = ft.Text(" Acordemos no estas de acuerdo")
    )
    
    page.add(
        ft.Text("Aplicacion de Prueba")
    )
ft.app(target=main)