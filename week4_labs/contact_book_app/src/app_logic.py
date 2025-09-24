import flet as ft 
from database import update_contact_db, delete_contact_db, add_contact_db, get_all_contacts_db 

def display_contacts(page, contacts_list_view, db_conn, search_term=""):
    """Fetches and displays all contacts in the ListView."""
    contacts_list_view.controls.clear()
    contacts = get_all_contacts_db(db_conn, search_term)
    
    for contact in contacts:
        contact_id, name, phone, email = contact
        contacts_list_view.controls.append(
            ft.Container(
                content=ft.ListTile(
                    title=ft.Text(name,weight=ft.FontWeight.BOLD), 
                    subtitle=ft.Column([        
                        ft.Text(f"📞 {phone}"),
                        ft.Text(f"✉️ {email}")
                    ], 
                    spacing=2, tight=True),
                    on_click=lambda e, c=contact: open_view_dialog(page, c),
                    trailing=ft.PopupMenuButton(
                        icon=ft.Icons.MORE_VERT,  
                        items=[
                            ft.PopupMenuItem(
                                text="Edit",
                                icon=ft.Icons.EDIT,
                                on_click=lambda _, c=contact: open_edit_dialog(page, c, db_conn, contacts_list_view),
                            ),
                            ft.PopupMenuItem(
                                text="Delete",
                                icon=ft.Icons.DELETE,
                                on_click=lambda _, cid=contact_id: delete_contact(page, cid, db_conn, contacts_list_view),
                            ),
                        ],
                    ),
                ),
                padding=5,
                margin=5,
                border=ft.border.all(2, "black"),
                border_radius=10,
                bgcolor="#FFFFFF",
            )
        )
    page.update()


def add_contact(page, inputs, contacts_list_view, db_conn):
    """Adds a new contact and refreshes the list."""
    name_input, phone_input, email_input = inputs

    # Check if name is empty
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
        title=ft.Text("Confirm Delete",weight=ft.FontWeight.BOLD, text_align="center"),
        content=ft.Text("Are you sure you want to delete this contact?"),
        actions=[
            ft.Row(
            [
                ft.TextButton(
                    "Cancel",
                    on_click=lambda e: setattr(dialog, "open", False) or page.update(),
                ),
                ft.TextButton("Yes", on_click=do_delete),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )   
    ]
)

    page.open(dialog) 
 
def open_edit_dialog(page, contact, db_conn, contacts_list_view): 
    """Opens a dialog to edit a contact's details.""" 
    contact_id, name, phone, email = contact 
 
    edit_name = ft.TextField(label="Name", value=name) 
    edit_phone = ft.TextField(label="Phone", value=phone) 
    edit_email = ft.TextField(label="Email", value=email) 
 
    def save_and_close(e): 
        update_contact_db(db_conn, contact_id, edit_name.value, edit_phone.value, edit_email.value) 
        dialog.open = False 
        page.update() 
        display_contacts(page, contacts_list_view, db_conn) 
 
    dialog = ft.AlertDialog( 
        modal=True, 
        title=ft.Text("Edit Contact"), 
        content=ft.Column([edit_name, edit_phone, edit_email]), 
        actions=[ 
            ft.TextButton("Cancel", on_click=lambda e: setattr(dialog, 'open', False) or page.update()), 
            ft.TextButton("Save", on_click=save_and_close), 
        ], 
    ) 
 
    page.open(dialog)


def open_view_dialog(page, contact):
    """Opens a popup dialog showing contact details."""
    contact_id, name, phone, email = contact

    dialog = ft.AlertDialog(
        modal=True,
        title=ft.Text("Contact Details", size=20, weight="bold", text_align="center"),
        content=ft.Column(
            controls=[
                ft.Row([ft.Icon(ft.Icons.PERSON, color="pink"), ft.Text(name)]),
                ft.Row([ft.Icon(ft.Icons.PHONE, color="red"), ft.Text(phone if phone else "No phone")]),
                ft.Row([ft.Icon(ft.Icons.EMAIL, color="indigo"), ft.Text(email if email else "No email")]),
            ],
            spacing=10,
            height=70,

        ),
        actions=[
            ft.TextButton("Close", on_click=lambda e: setattr(dialog, "open", False) or page.update())
        ],
    )

    page.open(dialog)
