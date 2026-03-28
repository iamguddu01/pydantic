from pydantic import BaseModel, EmailStr # Custom inbuilt data type for email validation
from pydantic import AnyUrl # It is used for url validation (Throws error if url format is not valid)
from typing import List, Dict, Optional

class Patient(BaseModel):
    name : str
    email : EmailStr
    linkedIn_url : AnyUrl
    weight : float
    age : int
    married : bool
    allergies : Optional[List[str]] = None
    contact_details : Optional[Dict[str, str]] = None
    
def data(patient : Patient):
   print(patient.model_dump())
    
patient_info = {'name':'Govind', 'email':'abc@gmail.com','linkedIn_url':'https://linkedin.com', 'weight':55.3,'age':20, 'married':False }
patient1 = Patient(**patient_info)
data(patient1)