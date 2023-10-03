from fastapi import APIRouter, HTTPException, Depends, status
from typing import List
from sqlalchemy.orm import Session
from data.validation_schemes import Contact_in, Contact_out
from data.db.connect_db import get_db
from data.operations import operations_contacts as oper_contact

router = APIRouter(prefix="/contact", tags=["contacts"])

@router.post("/", response_model = Contact_out)
async def add_contacts(contact: Contact_in, db: Session = Depends(get_db)):
    return oper_contact.add_contact(contact, db)
