#Imports flets and the hover animations python scripte
import flet as ft
from flet import TextField, ControlEvent
import hover_animations
import send_request

def main(page: ft.Page):
    #Makes page details and some collors
    page.title = 'Translator'
    page.bgcolor = "#121212"
    page.padding = 20
    page.theme_mode = 'dark'
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    #Makes tittle
    title = ft.Container(
        content=ft.Text(
            "Translator",
            size=32,
            weight=ft.FontWeight.BOLD,
            color="#ffffff"
        ),
        padding=20,
        alignment=ft.alignment.center
    )
    
    #Language select dropdown for users lang
    source_lang = ft.Dropdown(
        label="Base Language",
        width=200,
        options=[
            ft.dropdown.Option("en", "English"),
            ft.dropdown.Option("es", "Spanish"),
            ft.dropdown.Option("fr", "French"),
        ],
        bgcolor="#1E1E1E",
        label_style=ft.TextStyle(color="#8E8E93"),
        border_color="#BB86FC",
        color="#ffffff",
        value="en"
    )

    #Select language to translate to dropdown
    to_lang = ft.Dropdown(
        label="Target Language",
        label_style=ft.TextStyle(color="#8E8E93"),
        width=200,
        options=[
            ft.dropdown.Option("en", "English"),
            ft.dropdown.Option("es", "Spanish"),
            ft.dropdown.Option("fr", "French"),
        ],
        value="es",
        border_color="#03DAC6",
        bgcolor="#1E1E1E",
        color="#ffffff"
    )

    user_text = ft.TextField(
        label="Enter text to translate",
        multiline=True,
        label_style=ft.TextStyle(color="#8E8E93"),
        min_lines=10,
        max_lines=10,
        width=400,
        height=250,
        border_radius=20,
        bgcolor="#1E1E1E",
        color="#FFFFFF",
        border_color="#BB86FC"
    )

    output_text = ft.TextField(
        label = "Output Text",
        label_style=ft.TextStyle(color="#8E8E93"),
        multiline=True,
        max_lines=10,
        min_lines=10,
        bgcolor="#1E1E1E",
        border_radius=20,
        width=400,
        border_color="#03DAC6",
        color="#FFFFFF",
        height=250
    )

    def button_clicked(e):
        source = source_lang.value
        target = to_lang.value
        text = user_text.value
        print(text + " " + target + " " + source)
        result = send_request.send_request(text, target, source)
        output_text.value = result
        page.update()

    translate_button = ft.ElevatedButton(
        text="文A Translate",
        on_click=button_clicked,
        bgcolor="#BB86FC",
        color="#000000"
    )



    dropdown_row = ft.Row(
        [source_lang, to_lang],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=20
    )

    input_output_row = ft.Row(
        [user_text, output_text],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=20
    )

    translate_row = ft.Row(
        [translate_button],
        alignment=ft.MainAxisAlignment.CENTER,
    )

    page_column = ft.Column([
        title,
        dropdown_row,
        input_output_row,
        translate_row
    ],
    spacing=20,
    alignment=ft.MainAxisAlignment.START
    )

    page.add(page_column)

ft.app(target=main)