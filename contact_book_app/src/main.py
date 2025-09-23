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

    # ----- Initial Theme (Dark Mode by default) -----
    dark_mode = True
    page.bgcolor = ft.Colors.BLUE_GREY_900
    text_color = ft.Colors.WHITE
    hint_color = ft.Colors.WHITE70
    border_color = ft.Colors.WHITE

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

    contacts_list_view = ft.ListView(expand=1, spacing=10, auto_scroll=True)

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
        bgcolor=ft.Colors.BLUE,
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

    # ----- Toggle Theme Function -----
    def toggle_theme(e):
        nonlocal dark_mode

        if dark_mode:
            # Switch to Light Mode
            page.bgcolor = ft.Colors.WHITE
            header_color = ft.Colors.BLACK
            border = ft.Colors.BLACK
            text = ft.Colors.BLACK
            hint = ft.Colors.BLACK54
        else:
            # Switch to Dark Mode
            page.bgcolor = ft.Colors.BLUE_GREY_900
            header_color = ft.Colors.WHITE
            border = ft.Colors.WHITE
            text = ft.Colors.WHITE
            hint = ft.Colors.WHITE70

        # Update input fields (text + placeholder + label + border)
        for field in [name_input, phone_input, email_input, search_input]:
            field.border_color = border
            field.color = text
            field.hint_style = ft.TextStyle(color=hint)
            field.label_style = ft.TextStyle(color=text)   # ✅ label updates too

        # Update headers
        header1.color = header_color
        header2.color = header_color

        page.update()
        dark_mode = not dark_mode

    theme_button = ft.ElevatedButton(
        "Toggle Theme",
        icon=ft.Icons.BRIGHTNESS_6,
        bgcolor=ft.Colors.AMBER,
        color=ft.Colors.BLACK,
        on_click=toggle_theme,
    )

    # Page layout
    page.add(
        ft.Column(
            [
                header1,
                name_input,
                phone_input,
                email_input,
                add_button,
                ft.Divider(color=border_color),
                search_input,
                theme_button,
                header2,
                contacts_list_view,
            ],
            alignment=ft.MainAxisAlignment.START,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )

    # Initial load
    display_contacts(page, contacts_list_view, db_conn)


if __name__ == "__main__":
    ft.app(target=main)
