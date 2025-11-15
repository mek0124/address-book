# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDateEdit, QFormLayout, QFrame,
    QGridLayout, QLabel, QLineEdit, QMainWindow,
    QPushButton, QScrollArea, QSizePolicy, QStatusBar,
    QWidget)

class Ui_w_MainWindow(object):
    def setupUi(self, w_MainWindow):
        if not w_MainWindow.objectName():
            w_MainWindow.setObjectName(u"w_MainWindow")
        w_MainWindow.resize(800, 600)
        self.centralwidget = QWidget(w_MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.scrollArea = QScrollArea(self.frame_2)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 356, 453))
        self.formLayout = QFormLayout(self.scrollAreaWidgetContents)
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label)

        self.le_first_name = QLineEdit(self.scrollAreaWidgetContents)
        self.le_first_name.setObjectName(u"le_first_name")
        self.le_first_name.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.le_first_name)

        self.label_2 = QLabel(self.scrollAreaWidgetContents)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_2)

        self.le_last_name = QLineEdit(self.scrollAreaWidgetContents)
        self.le_last_name.setObjectName(u"le_last_name")
        self.le_last_name.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.le_last_name)

        self.label_3 = QLabel(self.scrollAreaWidgetContents)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_3)

        self.le_email_address = QLineEdit(self.scrollAreaWidgetContents)
        self.le_email_address.setObjectName(u"le_email_address")
        self.le_email_address.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.le_email_address)

        self.label_4 = QLabel(self.scrollAreaWidgetContents)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.label_4)

        self.le_home_phone = QLineEdit(self.scrollAreaWidgetContents)
        self.le_home_phone.setObjectName(u"le_home_phone")
        self.le_home_phone.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.le_home_phone)

        self.label_5 = QLabel(self.scrollAreaWidgetContents)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.label_5)

        self.le_cell_phone = QLineEdit(self.scrollAreaWidgetContents)
        self.le_cell_phone.setObjectName(u"le_cell_phone")
        self.le_cell_phone.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.le_cell_phone)

        self.label_6 = QLabel(self.scrollAreaWidgetContents)
        self.label_6.setObjectName(u"label_6")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.LabelRole, self.label_6)

        self.de_birthday = QDateEdit(self.scrollAreaWidgetContents)
        self.de_birthday.setObjectName(u"de_birthday")
        self.de_birthday.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.de_birthday.setDateTime(QDateTime(QDate(2000, 1, 1), QTime(0, 0, 0)))
        self.de_birthday.setCalendarPopup(True)

        self.formLayout.setWidget(5, QFormLayout.ItemRole.FieldRole, self.de_birthday)

        self.label_7 = QLabel(self.scrollAreaWidgetContents)
        self.label_7.setObjectName(u"label_7")

        self.formLayout.setWidget(6, QFormLayout.ItemRole.LabelRole, self.label_7)

        self.le_street = QLineEdit(self.scrollAreaWidgetContents)
        self.le_street.setObjectName(u"le_street")
        self.le_street.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.formLayout.setWidget(6, QFormLayout.ItemRole.FieldRole, self.le_street)

        self.label_8 = QLabel(self.scrollAreaWidgetContents)
        self.label_8.setObjectName(u"label_8")

        self.formLayout.setWidget(7, QFormLayout.ItemRole.LabelRole, self.label_8)

        self.le_city = QLineEdit(self.scrollAreaWidgetContents)
        self.le_city.setObjectName(u"le_city")
        self.le_city.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.formLayout.setWidget(7, QFormLayout.ItemRole.FieldRole, self.le_city)

        self.label_9 = QLabel(self.scrollAreaWidgetContents)
        self.label_9.setObjectName(u"label_9")

        self.formLayout.setWidget(8, QFormLayout.ItemRole.LabelRole, self.label_9)

        self.le_state = QLineEdit(self.scrollAreaWidgetContents)
        self.le_state.setObjectName(u"le_state")
        self.le_state.setMaxLength(2)
        self.le_state.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.formLayout.setWidget(8, QFormLayout.ItemRole.FieldRole, self.le_state)

        self.label_10 = QLabel(self.scrollAreaWidgetContents)
        self.label_10.setObjectName(u"label_10")

        self.formLayout.setWidget(9, QFormLayout.ItemRole.LabelRole, self.label_10)

        self.le_postal_code = QLineEdit(self.scrollAreaWidgetContents)
        self.le_postal_code.setObjectName(u"le_postal_code")
        self.le_postal_code.setMaxLength(5)
        self.le_postal_code.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.formLayout.setWidget(9, QFormLayout.ItemRole.FieldRole, self.le_postal_code)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_3.addWidget(self.scrollArea, 0, 0, 1, 1)

        self.pb_save = QPushButton(self.frame_2)
        self.pb_save.setObjectName(u"pb_save")

        self.gridLayout_3.addWidget(self.pb_save, 1, 0, 1, 1)

        self.pb_delete = QPushButton(self.frame_2)
        self.pb_delete.setObjectName(u"pb_delete")

        self.gridLayout_3.addWidget(self.pb_delete, 2, 0, 1, 1)


        self.gridLayout_2.addWidget(self.frame_2, 0, 0, 1, 1)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_3)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.scrollArea_2 = QScrollArea(self.frame_3)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 356, 517))
        self.gridLayout_5 = QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.gridLayout_4.addWidget(self.scrollArea_2, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.frame_3, 0, 1, 1, 1)


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        w_MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QStatusBar(w_MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        w_MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(w_MainWindow)

        QMetaObject.connectSlotsByName(w_MainWindow)
    # setupUi

    def retranslateUi(self, w_MainWindow):
        w_MainWindow.setWindowTitle(QCoreApplication.translate("w_MainWindow", u"Address Book", None))
        self.label.setText(QCoreApplication.translate("w_MainWindow", u"First Name", None))
        self.le_first_name.setPlaceholderText(QCoreApplication.translate("w_MainWindow", u"John", None))
        self.label_2.setText(QCoreApplication.translate("w_MainWindow", u"Last Name", None))
        self.le_last_name.setPlaceholderText(QCoreApplication.translate("w_MainWindow", u"Doe", None))
        self.label_3.setText(QCoreApplication.translate("w_MainWindow", u"Email Address", None))
        self.le_email_address.setPlaceholderText(QCoreApplication.translate("w_MainWindow", u"john_doe@email.com", None))
        self.label_4.setText(QCoreApplication.translate("w_MainWindow", u"Home Phone", None))
        self.le_home_phone.setInputMask(QCoreApplication.translate("w_MainWindow", u"(999) 999-9999", None))
        self.le_home_phone.setPlaceholderText(QCoreApplication.translate("w_MainWindow", u"(123) 456-7890", None))
        self.label_5.setText(QCoreApplication.translate("w_MainWindow", u"Cell Phone", None))
        self.le_cell_phone.setInputMask(QCoreApplication.translate("w_MainWindow", u"(999) 999-9999", None))
        self.le_cell_phone.setPlaceholderText(QCoreApplication.translate("w_MainWindow", u"(123) 456-7890", None))
        self.label_6.setText(QCoreApplication.translate("w_MainWindow", u"Birthday", None))
        self.de_birthday.setDisplayFormat(QCoreApplication.translate("w_MainWindow", u"MM/dd/yyyy", None))
        self.label_7.setText(QCoreApplication.translate("w_MainWindow", u"Street", None))
        self.le_street.setPlaceholderText(QCoreApplication.translate("w_MainWindow", u"123 Example Lane", None))
        self.label_8.setText(QCoreApplication.translate("w_MainWindow", u"City", None))
        self.le_city.setPlaceholderText(QCoreApplication.translate("w_MainWindow", u"Austin", None))
        self.label_9.setText(QCoreApplication.translate("w_MainWindow", u"State", None))
        self.le_state.setPlaceholderText(QCoreApplication.translate("w_MainWindow", u"TX", None))
        self.label_10.setText(QCoreApplication.translate("w_MainWindow", u"Postal Code", None))
        self.le_postal_code.setInputMask(QCoreApplication.translate("w_MainWindow", u"99999", None))
        self.le_postal_code.setPlaceholderText(QCoreApplication.translate("w_MainWindow", u"12345", None))
        self.pb_save.setText(QCoreApplication.translate("w_MainWindow", u"Save", None))
        self.pb_delete.setText(QCoreApplication.translate("w_MainWindow", u"Delete", None))
    # retranslateUi

