# main.py

import flet as ft
from database import init_db
from app_logic import display_contacts, add_contact


def main(page: ft.Page):
    page.title = "📖 Contact Book App"
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.window_width = 420
    page.window_height = 650

    db_conn = init_db()

    # ----- Scrollbar Theme
    page.theme = ft.Theme(
        scrollbar_theme=ft.ScrollbarTheme(
            track_color={
                "default": ft.Colors.TRANSPARENT,
            },
            track_visibility=False,
            thumb_visibility=False,
            thumb_color={
                "hovered": ft.Colors.BLUE_GREY_300,
                "default": ft.Colors.AMBER,
            },
            thickness=10, radius=15, main_axis_margin=5, cross_axis_margin=10,
        )
    )

    # ----- Theme Configurations
    dark_theme = {
        "bgcolor": ft.Colors.BLUE_GREY_900,
        "header": ft.Colors.WHITE,
        "border": ft.Colors.WHITE,
        "text": ft.Colors.WHITE,
        "hint": ft.Colors.WHITE70,
        "button_text": "Light Mode",
        "button_icon": ft.Icons.LIGHT_MODE,
    }

    light_theme = {
        "bgcolor": ft.Colors.RED_50,
        "header": ft.Colors.BLACK,
        "border": ft.Colors.BLACK,
        "text": ft.Colors.BLACK,
        "hint": ft.Colors.BLACK54,
        "button_text": "Dark Mode",
        "button_icon": ft.Icons.DARK_MODE,
    }

    # ----- Initial Theme (Dark Mode by default) -----
    current_theme = dark_theme
    page.bgcolor = current_theme["bgcolor"]
    text_color = current_theme["text"]
    hint_color = current_theme["hint"]
    border_color = current_theme["border"]

    # Input fields
    name_input = ft.TextField(
        label="Name",
        prefix_icon=ft.Icons.PERSON,
        width=350,
        border_color=border_color,
        color=text_color,
        hint_style=ft.TextStyle(color=hint_color),
        label_style=ft.TextStyle(color=text_color),
    )
    phone_input = ft.TextField(
        label="Phone",
        prefix_icon=ft.Icons.PHONE,
        width=350,
        border_color=border_color,
        color=text_color,
        hint_style=ft.TextStyle(color=hint_color),
        label_style=ft.TextStyle(color=text_color),
    )
    email_input = ft.TextField(
        label="Email",
        prefix_icon=ft.Icons.EMAIL,
        width=350,
        border_color=border_color,
        color=text_color,
        hint_style=ft.TextStyle(color=hint_color),
        label_style=ft.TextStyle(color=text_color),
    )

    # ✅ Contact list with vertical scrollbar
    contacts_list_view = ft.ListView(
        expand=True,
        spacing=10,
        auto_scroll=False,
        height=300
    )

    search_input = ft.TextField(
        label="Search Contacts",
        prefix_icon=ft.Icons.SEARCH,
        width=300,
        border_color=border_color,
        color=text_color,
        hint_style=ft.TextStyle(color=hint_color),
        label_style=ft.TextStyle(color=text_color),
        on_change=lambda e: display_contacts(
            page, contacts_list_view, db_conn, search_input.value
        ),
    )

    inputs = (name_input, phone_input, email_input)

    add_button = ft.ElevatedButton(
        text="Add Contact",
        icon=ft.Icons.ADD,
        bgcolor=ft.Colors.RED if dark_theme else ft.Colors.GREEN,
        color=ft.Colors.WHITE,
        on_click=lambda e: add_contact(page, inputs, contacts_list_view, db_conn),
    )

    # ----- Headers -----
    header1 = ft.Text(
        "Enter Contact Details:",
        size=22,
        weight=ft.FontWeight.BOLD,
        text_align=ft.TextAlign.CENTER,
        expand=True,
        color=text_color,
    )
    header2 = ft.Text(
        "Contacts:",
        size=22,
        weight=ft.FontWeight.BOLD,
        text_align=ft.TextAlign.CENTER,
        expand=True,
        color=text_color,
    )

    # ----- Theme Button (Defined Before toggle_theme) -----
    theme_button = ft.ElevatedButton(
        current_theme["button_text"],
        icon=current_theme["button_icon"],
        bgcolor=ft.Colors.AMBER,
        color=ft.Colors.BLACK,
    )

    # ----- Toggle Theme Function -----
    def toggle_theme(e):
        nonlocal current_theme

        current_theme = light_theme if current_theme == dark_theme else dark_theme

        page.bgcolor = current_theme["bgcolor"]

        for field in [name_input, phone_input, email_input, search_input]:
            field.border_color = current_theme["border"]
            field.color = current_theme["text"]
            field.hint_style = ft.TextStyle(color=current_theme["hint"])
            field.label_style = ft.TextStyle(color=current_theme["text"])

        header1.color = current_theme["header"]
        header2.color = current_theme["header"]
        theme_button.text = current_theme["button_text"]
        theme_button.icon = current_theme["button_icon"]

        theme_button.update()
        page.update()

    theme_button.on_click = toggle_theme

    # Page layout
    page.add(
        ft.Column(
            [
                header1,
                name_input,
                phone_input,
                email_input,
                add_button,
                ft.Divider(color=ft.Colors.AMBER, thickness=5, height=50),
                search_input,
                header2,
                contacts_list_view,
                theme_button,
            ],
            alignment=ft.MainAxisAlignment.START,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )

    # Load existing contacts
    display_contacts(page, contacts_list_view, db_conn)


if __name__ == "__main__":
    ft.app(target=main)
