from PySide6.QtWidgets import QApplication, QMessageBox
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
    
def get_agreement() -> bool:
    curr_dir = Path(__file__).parent
    data_dir = curr_dir / "app" / "data"
    os.makedirs(data_dir, exist_ok=True)
    agreed_file = data_dir / "agreed.txt"

    try:
        if agreed_file.exists():
            did_agree = agreed_file.read_text().strip()
            if did_agree == "True":
                return True

        reply = QMessageBox.question(
            None,
            "Permissions",
            "Allow the Address Book to read/write its database on your system?",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.Yes,
        )

        if reply == QMessageBox.Yes:
            agreed_file.write_text("True")
            return True

        QMessageBox.warning(
            None,
            "Permission Required",
            "The application cannot run without permission to manage its database.",
        )
        return False

    except Exception as e:
        QMessageBox.critical(None, "Error", f"An error occurred: {e}")
        return False

 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet(get_app_styles())

    if not get_agreement():
        sys.exit(1)

    app_db = DatabaseEngine()
    app_db.check_for_db_file()

    mainwindow = AddressBook(app_db)
    mainwindow.show()

    sys.exit(app.exec())