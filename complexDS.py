from pydantic import BaseModel
from typing import List, Dict   # We import complex DS because if we dont use it then pydantic will expect the of list from us 
# so using List from typig will help us to tell what kind of DS will be store in our DS Like in list we can store string, integer etc

class Patient(BaseModel):
    name : str
    age : int
    weight : float
    married : bool
    allergies : List[str] # List will contain string data only 
    contact_details : Dict[str, str] # This dict will constain both key and value as string  
    

def insert_patient_data(patient:Patient):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details['email'])
    print(patient.contact_details['phone'])
    print("DATA INSERTED")


patient_info = {'name':'Govind', 'age':22, 'weight':52.6, 'married':False, 'allergies':['polen', 'dust'], 'contact_details':{'email':'abc@mail.com', 'phone':'234567'}}
patient1 = Patient(**patient_info)
insert_patient_data(patient1)