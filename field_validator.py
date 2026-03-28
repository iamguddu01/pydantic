from pydantic import BaseModel, EmailStr, Field, field_validator
from typing import List, Dict

# Field validator works in 2 modes 1. Before mode, 2. After mode
# After Mode => It is default mode in field validator, in this case the value we will get is after type cohersion
# Before mode => In this mode the value we will get will be before type cohersion

class Patient(BaseModel):
    name : str
    email : EmailStr
    age : int
    weight : float
    married : bool = False


    @field_validator('email')
    @classmethod
    def email_validator(cls, value):
        valid_domains = ['hdfc.com', 'icici.com']
        domain_name = value.split('@')[-1]
        if domain_name not in valid_domains:
            raise ValueError('Not a valid domain')
        return value
    
    @field_validator('name')
    @classmethod
    def transform_name(cls, value):
        return value.upper()
    
    @field_validator('age', mode='before')
    @classmethod
    def validate_age(cls, value):
        if 0 < value < 100:
            return value
        else:
            raise ValueError('Age should be between 0 to 100')

def data(patient:Patient):
    print(patient.model_dump())


patient_info = {'name':'Govind', 'email':'abc@hdfc.com','weight':55.3,'age':20, 'married':False }
patient1 = Patient(**patient_info)
data(patient1)