from pydantic import BaseModel, EmailStr, Field, model_validator
from typing import Dict


class Patient(BaseModel):
    name : str
    email : EmailStr
    age : int
    weight : float
    married : bool = False
    contact_details: Dict[str, str]
    
    @model_validator(mode='after')
    def validate_emergency_contact(cls, model):
        if model.age > 60 and 'emergency' not in model.contact_details:
            raise ValueError('Patients older than 60 must have emergency contact')
        return model
    
def data(patient : Patient):
    print(patient.model_dump())
        
patient_info = {'name':'Govind', 'email':'abc@hdfc.com','weight':55.3,'age':70, 'married':False, 'contact_details' : {'phone':'123456', 'emergency':'98765432'} }
patient1 = Patient(**patient_info)
data(patient1)
