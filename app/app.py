from PySide6.QtWidgets import QMainWindow, QLabel, QVBoxLayout, QWidget
from PySide6.QtCore import QTimer, Qt
from datetime import date

from app.models.contact import ContactCreate
from app.ui.main_window import Ui_w_MainWindow
from app.services.contact import ContactService
from app.ui.components.clickable_card import ClickableCard


class AddressBook(QMainWindow, Ui_w_MainWindow):
    def __init__(self, db):
        super().__init__()

        self.db = db
        
        self.contact_service = ContactService(db)
        self.contacts = []
        
        self.current_contact_id = None
        
        self.setupUi(self)
        self.setMinimumWidth(800)
        self.setMinimumHeight(600)
        
        self.de_birthday.setDate(date.today())
        
        self.pb_save.clicked.connect(self.save_contact)
        self.pb_delete.clicked.connect(self.delete_contact)
        
        self.clear_timer = QTimer()
        self.clear_timer.setSingleShot(True)
        self.clear_timer.timeout.connect(self.clear_status)
        
        self.refresh_screen()

    def clear_status(self) -> None:
        self.statusBar.clearMessage()
        self.statusBar.setStyleSheet("background-color: transparent;")

    def show_error_success(self, is_error: bool, message: str) -> None:
        self.statusBar.showMessage(message)
        self.statusBar.setStyleSheet(
            f"background-color: {'red' if is_error else 'green'}; color: black;"
        )
        self.start_clear_timer()

    def start_clear_timer(self) -> None:
        self.clear_timer.start(3000)

    def clear_form(self) -> None:
        self.le_first_name.clear()
        self.le_last_name.clear()
        self.le_email_address.clear()
        self.le_home_phone.clear()
        self.le_cell_phone.clear()
        self.de_birthday.setDate(date.today())
        self.le_street.clear()
        self.le_city.clear()
        self.le_state.clear()
        self.le_postal_code.clear()
        self.current_contact_id = None
        self.pb_save.setText("Save")

    def refresh_screen(self) -> None:
        container = self.scrollAreaWidgetContents_2
        layout = container.layout()
        
        if layout is None or not isinstance(layout, QVBoxLayout):
            layout = QVBoxLayout()
            layout.setContentsMargins(6, 6, 6, 6)
            layout.setSpacing(10)
        
            QWidget().setLayout(container.layout()) if container.layout() else None
            container.setLayout(layout)
        
        for i in reversed(range(layout.count())):
            item = layout.itemAt(i)
            widget = item.widget()
        
            if widget:
                widget.setParent(None)
        
            else:
                layout.removeItem(item)
        
        try:
            contacts = self.contact_service.get_all_contacts()
        
        except Exception as e:
            self.show_error_success(True, f"Failed to load contacts: {e}")
            return
        
        if not contacts:
            empty_label = QLabel("No contacts saved yet.")
            empty_label.setStyleSheet("color: #FFD3D5; font-size: 14px;")
            empty_label.setAlignment(Qt.AlignCenter)
            layout.addWidget(empty_label)
            layout.addStretch()
            return
        
        for contact in contacts:
            card = ClickableCard(contact.id)
            card.set_contact_info(contact)
            card.clicked.connect(self.populate_form_with_contact)
            layout.addWidget(card)
        
        layout.addStretch()
        self.contacts = contacts

    def populate_form_with_contact(self, contact_id: str) -> None:
        contact = self.contact_service.get_contact(contact_id)
        
        if not contact:
            self.show_error_success(True, "Contact not found.")
            return
        
        self.le_first_name.setText(contact.first_name or "")
        self.le_last_name.setText(contact.last_name or "")
        self.le_email_address.setText(contact.email_address or "")
        self.le_home_phone.setText(contact.home_phone or "")
        self.le_cell_phone.setText(contact.cell_phone or "")
        
        if contact.birthday:
            try:
                y, m, d = map(int, contact.birthday.split("-"))
                self.de_birthday.setDate(date(y, m, d))
        
            except Exception:
                self.de_birthday.setDate(date.today())
        
        else:
            self.de_birthday.setDate(date.today())
        
        self.le_street.setText(contact.street or "")
        self.le_city.setText(contact.city or "")
        self.le_state.setText(contact.state or "")
        self.le_postal_code.setText(contact.postal_code or "")
        self.current_contact_id = contact.id
        self.pb_save.setText("Update")
        
        self.show_error_success(False, f"Editing {contact.first_name} {contact.last_name}")

    def save_contact(self) -> None:
        first_name = self.le_first_name.text().strip()
        last_name = self.le_last_name.text().strip()
        email = self.le_email_address.text().strip()
        home_phone = self.le_home_phone.text().strip()
        cell_phone = self.le_cell_phone.text().strip()
        birthday = self.de_birthday.date().toString("yyyy-MM-dd")
        street = self.le_street.text().strip()
        city = self.le_city.text().strip()
        state = self.le_state.text().strip()
        postal_code = self.le_postal_code.text().strip()
        
        if (
            not first_name and \
                not last_name and \
                    not email and \
                        not home_phone and \
                            not cell_phone and \
                                not street and \
                                    not city and \
                                        not state and \
                                            not postal_code
            ):
            return
            
        if not first_name:
            self.show_error_success(True, "First Name is required.")
            return
            
        if not cell_phone and not home_phone:
            self.show_error_success(True, "Provide at least a cell or home phone.")
            return
            
        if state and len(state) != 2:
            self.show_error_success(True, "State must be a 2-letter abbreviation.")
            return
            
        if postal_code and (not postal_code.isdigit() or len(postal_code) != 5):
            self.show_error_success(True, "Postal code must be 5 digits.")
            return
            
        if email and ("@" not in email or "." not in email):
            self.show_error_success(True, "Email address appears invalid.")
            return

        new_contact = ContactCreate(
            first_name=first_name,
            last_name=last_name or None,
            email_address=email or None,
            home_phone=home_phone or None,
            cell_phone=cell_phone or None,
            birthday=birthday or None,
            street=street or None,
            city=city or None,
            state=state or None,
            postal_code=postal_code or None,
        )
        
        is_valid, message = self.contact_service.validate_contact(new_contact)
        
        if not is_valid:
            self.show_error_success(True, message)
            return
            
        if self.current_contact_id:
            did_save, result = self.contact_service.update_contact(self.current_contact_id, new_contact)
            action = "updated"
            self.current_contact_id = None
            self.pb_save.setText("Save")
        
        else:
            did_save, result = self.contact_service.save_contact(new_contact)
            action = "saved"
            
        if did_save:
            self.clear_form()
            self.refresh_screen()
            self.show_error_success(False, f"Contact {action} successfully!")
        
        else:
            self.show_error_success(True, result)

    def delete_contact(self) -> None:
        if not self.current_contact_id:
            self.show_error_success(True, "Select a contact to delete first.")
            return
            
        contact = self.contact_service.get_contact(self.current_contact_id)
        
        if not contact:
            self.show_error_success(True, "Contact not found.")
            return
            
        success = self.contact_service.delete_contact(self.current_contact_id)
        
        if success:
            self.clear_form()
            self.refresh_screen()
            self.show_error_success(False, f"Contact {contact.first_name} {contact.last_name} deleted successfully!")
        
        else:
            self.show_error_success(True, "Failed to delete contact.")
