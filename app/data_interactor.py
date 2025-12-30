import os
from models.contacts import *


class DataInteractor:
    def get_all_contacts()-> list[dict]:
        pass
    def create_contact(contact_data: dict)-> str:
        pass
    def update_contact(id: str, contact_data: dict)-> bool:
        pass
    def delete_contact(id: str)-> bool:
        pass
