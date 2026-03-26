from pydantic import BaseModel
from typing import List, Dict, Optional # Import optional and use where you want to be that field optional  

#  Notes -> If you are declaring a field optional then you have to give a default value like None.
class Patient(BaseModel):
    name : str
    age : int
    weight : float
    married : bool = False
    allergies : Optional[List[str]] = None
    contact_details : Dict[str, str]
    

def insert_patient_data(patient:Patient):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details['email'])
    print(patient.contact_details['phone'])
    print("DATA INSERTED")


patient_info = {'name':'Govind', 'age':22, 'weight':52.6, 'married':False, 'contact_details':{'email':'abc@mail.com', 'phone':'234567'}}
patient1 = Patient(**patient_info)
insert_patient_data(patient1) 
# In this data we don't have allergies so it will because it's optional and the value will considered none 