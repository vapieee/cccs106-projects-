import flet as ft
import mysql.connector
from db_connection import connect_db


def main(page: ft.Page):
    # Window configuration
    page.title = "User Login"
    page.window_frameless = True
    page.window_height = 350
    page.window_width = 400
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.bgcolor = ft.Colors.AMBER_ACCENT

    # Input fields (without prefix_icon)
    username_field = ft.TextField(
        label="User name",
        hint_text="Enter your user name",
        helper_text="This is your unique identifier",
        width=250,
        autofocus=True,
        bgcolor=ft.Colors.LIGHT_BLUE_ACCENT
    )

    password_field = ft.TextField(
        label="Password",
        hint_text="Enter your password",
        helper_text="This is your secret key",
        width=250,
        password=True,
        can_reveal_password=True,
        bgcolor=ft.Colors.LIGHT_BLUE_ACCENT
    )

    # Title
    title = ft.Text(
        value="User Login",
        size=20,
        weight=ft.FontWeight.BOLD,
        text_align=ft.TextAlign.CENTER,
        font_family="Arial"
    )

    # Login logic
    def login_click(e):
        # Dialogs
        success_dialog = ft.AlertDialog(
            modal=True,
            title=ft.Text("Login Successful", text_align=ft.TextAlign.CENTER),
            content=ft.Text(f"Welcome, {username_field.value}!", text_align=ft.TextAlign.CENTER),
            icon=ft.Icon(ft.Icons.CHECK_CIRCLE, color=ft.Colors.GREEN),
            actions=[ft.TextButton("OK", on_click=lambda e: page.close(success_dialog))],
        )

        failure_dialog = ft.AlertDialog(
            modal=True,
            title=ft.Text("Login Failed", text_align=ft.TextAlign.CENTER),
            content=ft.Text("Invalid username or password", text_align=ft.TextAlign.CENTER),
            icon=ft.Icon(ft.Icons.ERROR, color=ft.Colors.RED),
            actions=[ft.TextButton("OK", on_click=lambda e: page.close(failure_dialog))],
        )

        input_error_dialog = ft.AlertDialog(
            modal=True,
            title=ft.Text("Input Error", text_align=ft.TextAlign.CENTER),
            content=ft.Text("Please enter username and password", text_align=ft.TextAlign.CENTER),
            icon=ft.Icon(ft.Icons.INFO, color=ft.Colors.BLUE),
            actions=[ft.TextButton("OK", on_click=lambda e: page.close(input_error_dialog))],
        )

        database_error_dialog = ft.AlertDialog(
            modal=True,
            title=ft.Text("Database Error", text_align=ft.TextAlign.CENTER),
            content=ft.Text("An error occurred while connecting to the database", text_align=ft.TextAlign.CENTER),
            actions=[ft.TextButton("OK", on_click=lambda e: page.close(database_error_dialog))],
        )

        # Step 1: Input validation
        if username_field.value.strip() == "" or password_field.value.strip() == "":
            page.open(input_error_dialog)
            return

        # Step 2: Database check
        try:
            conn = connect_db()
            cursor = conn.cursor()

            query = "SELECT * FROM users WHERE username=%s AND password=%s"
            cursor.execute(query, (username_field.value, password_field.value))
            result = cursor.fetchone()

            cursor.close()
            conn.close()

            if result:
                page.open(success_dialog)
            else:
                page.open(failure_dialog)

        except mysql.connector.Error:
            page.open(database_error_dialog)

    # Login button
    login_button = ft.ElevatedButton(
        text="Login",
        icon=ft.Icons.LOGIN,
        width=100,
        on_click=login_click
    )

    # Rows for icons outside the box
    username_row = ft.Row(
        controls=[ft.Icon(ft.Icons.PERSON), username_field],
        alignment=ft.MainAxisAlignment.CENTER
    )

    password_row = ft.Row(
        controls=[ft.Icon(ft.Icons.LOCK), password_field],
        alignment=ft.MainAxisAlignment.CENTER
    )

    # Add controls to layout
    page.add(
        title,
        ft.Container(
            content=ft.Column(
                controls=[username_row, password_row],
                spacing=20
            )
        ),
        ft.Container(
            content=login_button,
            alignment=ft.alignment.top_right,
            margin=ft.margin.only(top=20, right=40)
        )
    )


# App entry point
ft.app(target=main)
