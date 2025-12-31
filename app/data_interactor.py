from models.contacts import *
from pymongo import MongoClient 
from bson import ObjectId


class DataInteractor:
    def __init__(self,uri:str):
        self.uri = uri
        
    def get_all_contacts(self)-> list[dict]:

        try:
            client = MongoClient(self.uri)

            client.admin.command("ping")

            print("✅ MongoDB connected successfully")


                
            database = client.get_database("phonebook")
            contacts_col = database.get_collection("contacts")

            contacts = contacts_col.find()
            result = []
            for doc in contacts:
                doc["_id"] = str(doc["_id"])
                result.append(doc)

            print(result)
            return result
            



        except Exception as e:
            return f"Unable to find the document due to the following error: {e}" 
        
        finally:
            client.close()


    def create_contact(self,contact_data: dict)-> list:
        def cheack_phone_uniqe(contacts_col , phone:str):
            res = contacts_col.find_one({"phone_number":phone})
            return res is None

        try:
            client = MongoClient(self.uri)

                
            database = client.get_database("phonebook")
            contacts_col = database.get_collection("contacts")

            if cheack_phone_uniqe(contacts_col, contact_data["phone_number"]):

                result = contacts_col.insert_one(contact_data)

                return [True,result.inserted_id]
            
            return [False,"phone is not uniqe"]


        except Exception as e:
            return [False,f"Unable to find the document due to the following error: {e}" ]
        
        finally:
            client.close()

    def update_contact(self,id: str, contact_data: dict)-> bool:
        
        try:
            client = MongoClient(self.uri)

            client.admin.command("ping")

            print("✅ MongoDB connected successfully")

                
            database = client.get_database("phonebook")

            contacts_col = database.get_collection("contacts")

            contacts_col.update_one({"_id": ObjectId(id)},{"$set": contact_data})   

            return True

        except Exception as e:
            print(e)
            return False 
        
        finally:
            client.close()
           


    def delete_contact(self,id: str)-> bool:
        try:
            client = MongoClient(self.uri)

            client.admin.command("ping")

            print("✅ MongoDB connected successfully")

                
            database = client.get_database("phonebook")

            contacts_col = database.get_collection("contacts")

            contacts_col.delete_one({"_id": ObjectId(id)})   

            return True

        except Exception:
            return False 
        
        finally:
            client.close()
