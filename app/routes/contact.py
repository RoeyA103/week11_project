from fastapi import APIRouter
from models.contacts import Contact, ContactUpdate
from data_interactor import DataInteractor
import os
uri = os.getenv("MONGO_URL")

dti= DataInteractor(uri)

router = APIRouter(prefix="/contacts", tags=["Contacts"])


@router.get("/")
def list_contacts():
    """Get all contacts"""
    return dti.get_all_contacts()


@router.post("/")
def create_contact(contact: Contact):
    """Create new contact"""
    res = dti.create_contact(contact.model_dump())
    if res[0]:
        message = {"message": "Contact created successfully","id": f"{res[1]}"}
        return message
    return res[1]


@router.put("/{id}")
def update_contact(id: str, contact: ContactUpdate):
    """Update existing contact"""
    result =  dti.update_contact(id=id,contact_data=contact.model_dump(exclude_none=True))
    if result:
        return {"The contact was successfully updated"}
    return ("The contact was not updated successfully")


@router.delete("/{id}")
def delete_contact(id: str):
    """Delete contact"""
    result = dti.delete_contact(id)
    if result:
        return {"The contact was successfully deleted"}
    return ("The contact was not deleted successfully")
