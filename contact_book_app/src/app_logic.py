 # app_logic.py
import flet as ft 
from database import update_contact_db, delete_contact_db, add_contact_db, get_all_contacts_db 
def display_contacts(page, contacts_list_view, db_conn, search_term=""):
    """Fetches and displays all contacts in the ListView."""
    contacts_list_view.controls.clear()
    contacts = get_all_contacts_db(db_conn, search_term)

    for contact in contacts:
        contact_id, name, phone, email = contact
        contacts_list_view.controls.append(
    ft.Card(
        content=ft.ListTile(
            leading=ft.Icon(ft.Icons.PERSON),
            title=ft.Text(name),
            subtitle=ft.Text(f"📞 {phone} | ✉️ {email}"),
            trailing=ft.PopupMenuButton(
                icon=ft.Icons.MORE_VERT,
                items=[
                    ft.PopupMenuItem(text="Edit", icon=ft.Icons.EDIT,
                        on_click=lambda _, c=contact: open_edit_dialog(page, c, db_conn, contacts_list_view)),
                    ft.PopupMenuItem(text="Delete", icon=ft.Icons.DELETE,
                        on_click=lambda _, cid=contact_id: delete_contact(page, cid, db_conn, contacts_list_view)),
                ]
            )
        )
    )
)

    page.update() 
 
def add_contact(page, inputs, contacts_list_view, db_conn):
    """Adds a new contact and refreshes the list."""
    name_input, phone_input, email_input = inputs

    # Validation: check if name is empty
    if not name_input.value.strip():
        name_input.error_text = "Name cannot be empty!"
        page.update()
        return

    add_contact_db(db_conn, name_input.value, phone_input.value, email_input.value)

    # Clear inputs
    for field in inputs:
        field.value = ""
        field.error_text = None

    display_contacts(page, contacts_list_view, db_conn)
    page.update()

 
def delete_contact(page, contact_id, db_conn, contacts_list_view):
    """Shows a confirmation dialog and deletes only if user confirms."""

    def do_delete(e):
        delete_contact_db(db_conn, contact_id)
        display_contacts(page, contacts_list_view, db_conn)
        dialog.open = False
        page.update()

    dialog = ft.AlertDialog(
        modal=True,
        title=ft.Text("Confirm Delete"),
        content=ft.Text("Are you sure you want to delete this contact?"),
        actions=[
            ft.TextButton(
                "Cancel",
                on_click=lambda e: setattr(dialog, "open", False) or page.update(),
            ),
            ft.TextButton("Yes", on_click=do_delete),
        ],
    )

    # IMPORTANT: This is the same pattern used in your Edit dialog
    page.open(dialog)
 
 
def open_edit_dialog(page, contact, db_conn, contacts_list_view): 
    """Opens a dialog to edit a contact's details.""" 
    contact_id, name, phone, email = contact 
 
    edit_name = ft.TextField(label="Name", value=name) 
    edit_phone = ft.TextField(label="Phone", value=phone) 
    edit_email = ft.TextField(label="Email", value=email) 
 
    def save_and_close(e): 
        update_contact_db(db_conn, contact_id, edit_name.value, edit_phone.value, 
edit_email.value) 
        dialog.open = False 
        page.update() 
        display_contacts(page, contacts_list_view, db_conn) 
 
    dialog = ft.AlertDialog( 
        modal=True, 
        title=ft.Text("Edit Contact"), 
        content=ft.Column([edit_name, edit_phone, edit_email]), 
        actions=[ 
            ft.TextButton("Cancel", on_click=lambda e: setattr(dialog, 'open', False) 
or page.update()), 
            ft.TextButton("Save", on_click=save_and_close), 
        ], 
    ) 
 
    page.open(dialog)