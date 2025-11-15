from sqlalchemy import Column, String
from app.database.db import Base


class Contact(Base):
    __tablename__ = "contacts"

    id: str
    first_name: str
    last_name: str = None
    email_address: str = None
    home_phone: str = None
    cell_phone: str
    birthday: str = None
    street: str = None
    city: str = None
    state: str = None
    postal_code: str = None