import os
from models.contacts import *

from pymongo import MongoClient


def get_client(uri: str):
    try:
        client = MongoClient(uri)

        client.admin.command("ping")

        print("✅ MongoDB connected successfully")
        return client

    except Exception as e:
        return e




uri = "localhost:27017"
client = MongoClient(uri)

try:
    database = client.get_database("phonebook")
    contacts = database.get_collection("contacts")

    # Query for a movie that has the title 'Back to the Future'
    query = { "firstname": "nana" }
    contact = contacts.find()

    print(list(contact))

    client.close()

except Exception as e:
    raise Exception("Unable to find the document due to the following error: ", e)


class DataInteractor:
    def __init__(self,uri):
        self.uri = uri
        
    def get_all_contacts(self)-> list[dict]:

        try:
            client = MongoClient(self.uri)

            client.admin.command("ping")

            print("✅ MongoDB connected successfully")


                
            database = client.get_database("phonebook")
            contacts_col = database.get_collection("contacts")

            contacts = contacts_col.find()

            return list(contacts)


        except Exception as e:
            return f"Unable to find the document due to the following error: {e}" 
        
        finally:
            client.close()


    def create_contact(self,contact_data: dict)-> str:
        try:
            client = MongoClient(self.uri)

            client.admin.command("ping")

            print("✅ MongoDB connected successfully")


                
            database = client.get_database("phonebook")
            contacts_col = database.get_collection("contacts")

            contacts = contacts_col.insert_one(contact_data)

            first_key, first_value = next(iter(contact_data.items()))

            result = contacts_col.find_one({first_key:first_value})

            return result["_id"]


        except Exception as e:
            return f"Unable to find the document due to the following error: {e}" 
        
        finally:
            client.close()

    def update_contact(self,id: str, contact_data: dict)-> bool:
        
        try:
            client = MongoClient(self.uri)

            client.admin.command("ping")

            print("✅ MongoDB connected successfully")

                
            database = client.get_database("phonebook")

            contacts_col = database.get_collection("contacts")

            contacts_col.update_one({"_id": f"{id}"},{"$set": {contact_data}})   

            return True

        except Exception:
            return False 
           


    def delete_contact(id: str)-> bool:
        pass
