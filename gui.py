import flet as ft

def main(page: ft.Page):
    page.title = "Language Translater"
    t = ft.Text(value="Hello, world!", color="blue")
    page.controls.append(t)
    page.update()

ft.app(main)