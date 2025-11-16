from typing import Tuple, Union
from app.models.contact import ContactCreate, ContactResponse
from app.validators.contact import ContactValidator

class ContactService:
    def __init__(self, db):
        self.db = db

    def validate_contact(self, contact: ContactCreate) -> Tuple[bool, str]:
        return ContactValidator.validate_contact(contact)

    def save_contact(self, contact: ContactCreate) -> Tuple[bool, Union[str, ContactResponse]]:
        return self.db.save_to_database(contact)

    def update_contact(self, contact_id: str, contact: ContactCreate) -> Tuple[bool, Union[str, ContactResponse]]:
        return self.db.update_in_database(contact_id, contact)

    def delete_contact(self, contact_id: str) -> bool:
        return self.db.delete_from_database(contact_id)

    def get_contact(self, contact_id: str) -> Union[ContactResponse, None]:
        return self.db.find_contact(contact_id)

    def get_all_contacts(self) -> list[ContactResponse]:
        return self.db.get_all_contacts()