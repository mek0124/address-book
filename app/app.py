from PySide6.QtWidgets import QMainWindow
from datetime import date
from uuid import uuid4
from app.ui.main_window import Ui_w_MainWindow


class AddressBook(QMainWindow, Ui_w_MainWindow):
    def __init__(self):
        super().__init__()
 
        self.setupUi(self)
        self.setMinimumWidth(800)
        self.setMinimumHeight(600)

        self.de_birthday.setDate(date.today())

        self.pb_save.clicked.connect(self.save_contact)
        self.pb_delete.clicked.connect(self.delete_contact)

    def save_contact(self) -> None:
        if self.le_first_name.text().strip() is None:
            self.statusBar.showMessage("First Name Is Required")

        if self.le_cell_phone.text().strip() is None and self.le_home_phone.text().strip() is None:
            self.statusBar.showMessage("Cell Phone or Home Phone Is Required")

        new_contact_id = str(uuid4())

        self.statusBar.showMessage("Contact Saved Successfully!")

    def delete_contact(self) -> None:
        self.statusBar.showMessage("Contact Deleted Successfully!")