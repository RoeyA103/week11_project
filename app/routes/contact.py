from fastapi import APIRouter
from models.contacts import Contact, ContactUpdate
from data_interactor import DataInteractor

dti= DataInteractor()

router = APIRouter(prefix="/contacts", tags=["Contacts"])


@router.get("/")
def list_contacts():
    """Get all contacts"""
    return dti.get_all_contacts()


@router.post("/")
def create_contact(contact: Contact):
    """Create new contact"""
    return dti.create_contact(contact.model_dump())


@router.put("/{id}")
def update_contact(id: str, contact: ContactUpdate.model_dump()):
    """Update existing contact"""
    return dti.update_contact(contact_id=id, contact=contact)


@router.delete("/{id}")
def delete_contact(id: str):
    """Delete contact"""
    return dti.del_contact(id)
