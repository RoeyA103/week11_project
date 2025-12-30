from fastapi import APIRouter
from models.contacts import Contact, ContactUpdate
from data_interactor import DataInteractor

dti= DataInteractor(uri = "localhost:27017")

router = APIRouter(prefix="/contacts", tags=["Contacts"])


@router.get("/")
def list_contacts():
    """Get all contacts"""
    return dti.get_all_contacts()


@router.post("/")
def create_contact(contact: Contact):
    """Create new contact"""
    id = dti.create_contact(contact.model_dump())
    response = {"message": "Contact created successfully","id": f"{id}"}
    return response


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
