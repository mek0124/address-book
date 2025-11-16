from PySide6.QtWidgets import QFrame, QVBoxLayout, QLabel, QGraphicsDropShadowEffect
from PySide6.QtCore import Signal, Qt

class ClickableCard(QFrame):
    clicked = Signal(str)

    def __init__(self, contact_id: str, parent=None):
        super().__init__(parent)
        self.contact_id = contact_id
        self.setup_ui()

    def setup_ui(self):
        self.setStyleSheet("""
            QFrame {
                background-color: rgba(109, 60, 93, 0.85);
                border: 1px solid #a86ea4;
                border-radius: 12px;
                padding: 10px;
            }
            QFrame:hover {
                background-color: rgba(168, 110, 164, 0.95);
            }
        """)
        self.setCursor(Qt.PointingHandCursor)

        shadow = QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(16)
        shadow.setOffset(0, 4)
        shadow.setColor(Qt.black)
        self.setGraphicsEffect(shadow)
        
        layout = QVBoxLayout(self)
        layout.setContentsMargins(8, 6, 8, 6)
        
        self.name_label = QLabel()
        self.name_label.setStyleSheet("color: #f7ebff; font-size: 16px; font-weight: bold;")
        layout.addWidget(self.name_label)
        
        self.phone_label = QLabel()
        self.phone_label.setStyleSheet("color: #f7ebff; font-size: 14px;")
        layout.addWidget(self.phone_label)
        
        self.email_label = QLabel()
        self.email_label.setStyleSheet("color: #e9d3ff; font-size: 13px;")
        layout.addWidget(self.email_label)

    def set_contact_info(self, contact):
        full_name = f"{contact.first_name or ''} {contact.last_name or ''}".strip()
        self.name_label.setText(full_name if full_name else "(No name)")
        
        phones = []
        target = "() -"
        if contact.cell_phone != target:
            phones.append(contact.cell_phone)
        if contact.home_phone != target:
            phones.append(contact.home_phone)
        self.phone_label.setText(", ".join(phones) if phones else "No phone")
        
        self.email_label.setText(contact.email_address or "No email")

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.clicked.emit(self.contact_id)
        super().mousePressEvent(event)