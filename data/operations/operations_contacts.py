from typing import List
from sqlalchemy.orm import Session
from data.db.db_models import DBContact
from data.validation_schemes import Contact_in, Contact_out

async def add_contact(contact: Contact_in, db: Session):
    new_contact = DBContact(
        name=contact.name,
        surname=contact.surname,
        email=contact.email,
        phone=contact.phone,
        birthday=contact.birthday,
        text=contact.text
    )
    if new_contact:
        print(new_contact)
    else:
        print("-----------------")
    db.add(new_contact)
    db.commit()
    db.refresh(new_contact)
    return new_contact
