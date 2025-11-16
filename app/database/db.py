from typing import Tuple, Union, List
from pathlib import Path
from uuid import uuid4

from app.models.contact import ContactCreate, ContactResponse
from app.validators.contact import ContactValidator

import sqlite3 as sql
import os


class DatabaseEngine:
    
    def check_for_db_file(self) -> str:
        curr_dir = Path(__file__).parent
        one_up = curr_dir.parent
        data_dir = os.path.join(one_up, "data")

        if not os.path.isdir(data_dir):
            os.makedirs(data_dir, exist_ok=True)

        db_file = os.path.join(data_dir, "contacts.db")

        if not os.path.isfile(db_file):
            self.create_database(db_file)

        return db_file

    def get_database(self) -> sql.Connection:
        db_file_path = self.check_for_db_file()

        try:
            return sql.connect(db_file_path)
        except Exception as e:
            raise e

    def get_cursor(self) -> Tuple[sql.Connection, sql.Cursor]:
        mdb = self.get_database()

        try:
            return mdb, mdb.cursor()
        except Exception as e:
            raise e

    def create_database(self, file_path: str) -> None:
        try:
            with sql.connect(file_path) as mdb:
                cur = mdb.cursor()

                cur.execute('''CREATE TABLE IF NOT EXISTS contacts(
                    id TEXT NOT NULL PRIMARY KEY,
                    first_name TEXT,
                    last_name TEXT,
                    email_address TEXT,
                    home_phone TEXT,
                    cell_phone TEXT,
                    birthday TEXT,
                    street TEXT,
                    city TEXT,
                    state TEXT,
                    postal_code TEXT
                )''')

        except Exception as e:
            raise e

    def save_to_database(self, incoming_contact: ContactCreate) -> Tuple[bool, Union[str, ContactResponse]]:
        is_valid, message = ContactValidator.validate_contact(incoming_contact)
        
        if not is_valid:
            return False, message

        mdb, cur = self.get_cursor()

        existing = None
        
        if incoming_contact.email_address:
            existing = cur.execute(
                'SELECT * FROM contacts WHERE email_address=?',
                (incoming_contact.email_address.strip(),)
            ).fetchone()

        if existing:
            mdb.close()
            return False, "A contact with this email already exists."

        try:
            contact_id = str(uuid4())

            cur.execute(
                '''INSERT INTO contacts(
                    id, first_name, last_name, email_address,
                    home_phone, cell_phone, birthday, street,
                    city, state, postal_code
                ) VALUES (?,?,?,?,?,?,?,?,?,?,?)''',
                (
                    contact_id,
                    incoming_contact.first_name,
                    incoming_contact.last_name,
                    incoming_contact.email_address,
                    incoming_contact.home_phone,
                    incoming_contact.cell_phone,
                    incoming_contact.birthday,
                    incoming_contact.street,
                    incoming_contact.city,
                    incoming_contact.state,
                    incoming_contact.postal_code
                )
            )

            mdb.commit()

            contact_response = ContactResponse(
                id=contact_id,
                **incoming_contact.model_dump()
            )
            return True, contact_response

        except Exception as e:
            mdb.rollback()
            return False, f"An Exception Occurred: {e}"

        finally:
            mdb.close()

    def update_in_database(self, contact_id: str, updated_contact: ContactCreate) -> Tuple[bool, Union[str, ContactResponse]]:
        mdb, cur = self.get_cursor()

        is_valid, message = ContactValidator.validate_contact(updated_contact)
        
        if not is_valid:
            return False, message

        try:
            existing = cur.execute(
                'SELECT * FROM contacts WHERE id=?',
                (contact_id,)
            ).fetchone()

            if not existing:
                mdb.close()
                return False, "Contact not found."

            cur.execute(
                '''UPDATE contacts SET 
                    first_name=?, last_name=?, email_address=?,
                    home_phone=?, cell_phone=?, birthday=?, street=?,
                    city=?, state=?, postal_code=?
                WHERE id=?''',
                (
                    updated_contact.first_name,
                    updated_contact.last_name,
                    updated_contact.email_address,
                    updated_contact.home_phone,
                    updated_contact.cell_phone,
                    updated_contact.birthday,
                    updated_contact.street,
                    updated_contact.city,
                    updated_contact.state,
                    updated_contact.postal_code,
                    contact_id
                )
            )

            mdb.commit()

            contact_response = ContactResponse(
                id=contact_id,
                **updated_contact.model_dump()
            )
            return True, contact_response

        except Exception as e:
            mdb.rollback()
            return False, f"An Exception Occurred: {e}"

        finally:
            mdb.close()

    def delete_from_database(self, contact_id: str) -> bool:
        mdb, cur = self.get_cursor()

        try:
            result = cur.execute(
                'DELETE FROM contacts WHERE id=?',
                (contact_id,)
            )
            mdb.commit()

            return result.rowcount > 0

        except Exception:
            mdb.rollback()
            return False

        finally:
            mdb.close()

    def find_contact(self, contact_id: str) -> Union[ContactResponse, None]:
        mdb, cur = self.get_cursor()

        try:
            result = cur.execute(
                'SELECT * FROM contacts WHERE id=?',
                (contact_id,)
            ).fetchone()

            if not result:
                return None

            return ContactResponse(
                id=result[0],
                first_name=result[1],
                last_name=result[2],
                email_address=result[3],
                home_phone=result[4],
                cell_phone=result[5],
                birthday=result[6],
                street=result[7],
                city=result[8],
                state=result[9],
                postal_code=result[10]
            )

        except Exception:
            return None

        finally:
            mdb.close()

    def get_all_contacts(self) -> List[ContactResponse]:
        mdb, cur = self.get_cursor()

        try:
            results = cur.execute('SELECT * FROM contacts').fetchall()

            contacts = []
            for r in results:
                contacts.append(ContactResponse(
                    id=r[0],
                    first_name=r[1],
                    last_name=r[2],
                    email_address=r[3],
                    home_phone=r[4],
                    cell_phone=r[5],
                    birthday=r[6],
                    street=r[7],
                    city=r[8],
                    state=r[9],
                    postal_code=r[10]
                ))

            return contacts

        except Exception:
            return []

        finally:
            mdb.close()
