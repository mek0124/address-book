from pydantic import BaseModel


class ContactCreate(BaseModel):
    first_name: str
    last_name: str = None
    email_address: str = None
    home_phone: str = None
    cell_phone: str = None
    birthday: str = None
    street: str = None
    city: str = None
    state: str = None
    postal_code: str = None


class ContactResponse(BaseModel):
    id: str
    first_name: str
    last_name: str = None
    email_address: str = None
    home_phone: str = None
    cell_phone: str = None
    birthday: str = None
    street: str = None
    city: str = None
    state: str = None
    postal_code: str = None