from PySide6.QtWidgets import QApplication
from pathlib import Path
import sys
import os

from app.app import AddressBook
from app.database.db import DatabaseEngine

def get_app_styles() -> str:
    curr_dir = Path(__file__).parent
    styles_file = os.path.join(curr_dir, "app", "assets", "styles.qss")

    with open(styles_file, 'r') as f:
        return f.read()
 
if __name__ == '__main__':
    app_db = DatabaseEngine()
    app_db.check_for_db_file()

    app = QApplication(sys.argv)
    app.setStyleSheet(get_app_styles())
 
    mainwindow = AddressBook(app_db)
    mainwindow.show()
 
    sys.exit(app.exec())