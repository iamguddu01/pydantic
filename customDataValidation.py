from pydantic import BaseModel, Field # Field is used in many operations of validation 
from typing import List, Dict, Optional, Annotated

# By using Annotated and field we attach meta deta (Check example in age)
# We can set default values using Field function (Check exapmle in married)
# To stop type cohersion we can use strict that will not allow for type cohersion (Check example in age)

class Patient(BaseModel):
    name : str = Field(max_length=150) # Length of the name should be 150 maximum
    weight : float = Field(gt=0, lt=120) # Now weight should be greater than 0 and less than 120 can't be negative
    age : Annotated[int, Field(gt=0, lt=70, strict=True, title='Age of the patient', description="Give the age of the patient between 0 to 70", examples=[45,67])]
    married : Annotated[bool, Field(default=None, description='Is the patient married or not')]
    allergies : Optional[List[str]] = Field(max_length=5, default=None) # Only 5 allergies allowed
    contact_details : Optional[Dict[str, str]] = None

def data(patient:Patient):
    print(patient.model_dump())
    
patient_info = {'name':'Govind','weight':23.56,'age':20, 'married':False }
patient1 = Patient(**patient_info)
data(patient1)