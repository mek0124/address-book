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
    
def get_agreement() -> bool:
    try:
        with open("./agreed.txt", 'r') as f:
            did_agree = f.read()

            if did_agree == "False":
                user_agrees = input("\nDo you agree to allow this application to read/write data to your system? (Y/N):\n")
                valid_options = ['y', 'n']

                while not user_agrees in valid_options:
                    print("\nInvalid Option. Try Again")
                    user_agrees = input("\nDo you agree to allow this application to read/write data to your system? (Y/N):\n")

                    if user_agrees in valid_options:
                        break

                if user_agrees == 'y':
                    with open("./agreed.txt", 'w') as f:
                        f.write("True")

                else:
                    print("Application cannot run without permissions to read/write to it's own database")
                    sys.exit(1)

    except FileNotFoundError:
        with open("./agreed.txt", 'w+') as new_file:
            new_file.write("False")

        get_agreement()

    except Exception as e:
        raise e

 
if __name__ == '__main__':
    get_agreement()

    app_db = DatabaseEngine()
    app_db.check_for_db_file()

    app = QApplication(sys.argv)
    app.setStyleSheet(get_app_styles())
 
    mainwindow = AddressBook(app_db)
    mainwindow.show()
 
    sys.exit(app.exec())