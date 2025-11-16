from typing import Tuple
from app.models.contact import ContactCreate


class ContactValidator:
    @staticmethod
    def validate_contact(new_contact: ContactCreate) -> Tuple[bool, str]:
        if not new_contact.first_name or not new_contact.first_name.strip():
            return False, "First name is required."

        home = (new_contact.home_phone or "").strip()
        cell = (new_contact.cell_phone or "").strip()
        home_digits = "".join(ch for ch in home if ch.isdigit())
        cell_digits = "".join(ch for ch in cell if ch.isdigit())

        if not home_digits and not cell_digits:
            return False, "You must provide at least one phone number."

        if new_contact.email_address:
            email = new_contact.email_address.strip()
        
            if "@" not in email or "." not in email:
                return False, "Email address is not valid."

        if new_contact.state:
            state = new_contact.state.strip()
            if len(state) != 2:
                return False, "State must be a 2-letter abbreviation."

        if new_contact.postal_code:
            if not new_contact.postal_code.isdigit() or len(new_contact.postal_code) != 5:
                return False, "Postal code must be 5 digits."

        return True, ""
