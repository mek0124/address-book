from PySide6.QtWidgets import QApplication
from pathlib import Path

from app.app import AddressBook
from app.database.db import Base, engine

import sys
import os


def check_for_data_folder() -> None:
    curr_dir = Path(__file__).parent
    data_folder = os.path.join(curr_dir, "app", "data")

    if not os.path.isdir(data_folder):
        os.makedirs(data_folder, exist_ok=True)


def check_for_data_file() -> None:
    curr_dir = Path(__file__).parent
    data_file = os.path.join(curr_dir, "app", "data", "contacts.db")

    if not os.path.isfile(data_file):
        Base.metadata.create_all(bind=engine)
 
 
if __name__ == '__main__':
    check_for_data_folder()
    check_for_data_file()

    app = QApplication(sys.argv)
 
    mainwindow = AddressBook()
    mainwindow.show()

    center_point = QApplication.primaryScreen().availableGeometry().center()
    window_frame = mainwindow.frameGeometry()
    window_frame.moveCenter(center_point)
    mainwindow.move(window_frame.topLeft())
 
    sys.exit(app.exec())